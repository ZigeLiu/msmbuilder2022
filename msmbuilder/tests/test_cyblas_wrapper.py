# Collect the tests that are defined in the cython module test_cyblas
import pytest

from msmbuilder.tests import test_cyblas

CYBLAS_TESTS = sorted(name for name in dir(test_cyblas)
                      if name.startswith('test'))


def test_cyblas_tests_found():
    assert len(CYBLAS_TESTS) > 0


@pytest.mark.parametrize("name", CYBLAS_TESTS)
def test_cyblas_function(name):
    getattr(test_cyblas, name)()
