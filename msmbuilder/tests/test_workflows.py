from __future__ import print_function, division, absolute_import

import os
import shlex
import shutil
import subprocess
import tempfile
from importlib.resources import files

import pytest


class tempdir(object):
    def __enter__(self):
        self._curdir = os.path.abspath(os.curdir)
        self._tempdir = tempfile.mkdtemp()
        os.chdir(self._tempdir)

    def __exit__(self, *exc_info):
        os.chdir(self._curdir)
        shutil.rmtree(self._tempdir)


def shell_lines(resource):
    fn = str(files('msmbuilder') / resource)
    buf = ''
    with open(fn) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if line.endswith('\\'):
                buf += line.rstrip('\\')
            else:
                yield buf + ' ' + line
                buf = ''


def check_call(tokens):
    try:
        subprocess.check_output(tokens, stderr=subprocess.STDOUT,
                                universal_newlines=True)
    except subprocess.CalledProcessError as e:
        print(e.cmd)
        print(e.output)
        raise


@pytest.mark.parametrize("fn", [
    'basic.sh',
    'rmsd.sh',
    'ghmm.sh',
])
def test_workflows(fn):
    path = "tests/workflows/{}".format(fn)
    with tempdir():
        for line in shell_lines(path):
            check_call(shlex.split(line, posix=False))
