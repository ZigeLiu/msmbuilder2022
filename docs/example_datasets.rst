.. _example_datasets:
.. currentmodule:: msmbuilder.example_datasets

msmbuilder.example_datasets
===========================

Source: `msmbuilder/example_datasets/ <https://github.com/msmbuilder/msmbuilder2022/tree/main/msmbuilder/example_datasets>`__ ·

Small data sets for tutorials, tests and trying out methods: real MD
trajectories downloaded on first use, and toy systems simulated with Brownian
dynamics.

Using a dataset
---------------

Every dataset is a class with the same interface:

.. code-block:: python

    from msmbuilder.example_datasets import AlanineDipeptide

    ds = AlanineDipeptide()        # MD datasets: AlanineDipeptide(data_home=None, verbose=True)
    bunch = ds.get()               # download (or simulate) if needed, then load
    trajs = bunch.trajectories     # list of mdtraj.Trajectory or np.ndarray
    print(bunch.DESCR)             # description and citation

.. list-table::
   :header-rows: 1

   * - Method
     - Description
   * - ``get()``
     - Cache the data if needed, then load it. Returns a bunch with ``trajectories`` and ``DESCR``
   * - ``cache()``
     - Only download or simulate
   * - ``get_cached()``
     - Load data that is already cached; does not download or simulate

MD datasets (downloaded from figshare)
--------------------------------------

.. list-table::
   :header-rows: 1

   * - Class
     - Trajectories
     - Frames per trajectory
     - Atoms
     - Notes
   * - :class:`~msmbuilder.example_datasets.AlanineDipeptide`
     - 10
     - 9,999
     - 22
     - Implicit solvent; ``.dcd`` files
   * - :class:`~msmbuilder.example_datasets.MetEnkephalin`
     - 10
     - 9,979
     - 75
     - 
   * - :class:`~msmbuilder.example_datasets.FsPeptide`
     - 28
     - 10,000
     - 264
     - Fs peptide, implicit solvent; ``.xtc`` files
   * - ``MinimalFsPeptide``
     - 28
     - 50
     - 264
     - The same 500 ns trajectories saved every 10 ns, for fast tests (importable, but not listed in ``__all__``)

The function forms ``fetch_alanine_dipeptide()``, ``fetch_met_enkephalin()`` and
``fetch_fs_peptide()`` are equivalent to ``Class().get()``.

Toy systems (simulated locally)
-------------------------------

.. list-table::
   :header-rows: 1

   * - Class
     - Trajectories
     - Shape
     - Description
   * - ``DoubleWell(random_state=None)``
     - 10
     - ``(100001, 1)``
     - 1D Brownian dynamics on a double-well potential
   * - ``QuadWell(random_state=None)``
     - 100
     - ``(1001, 1)``
     - 1D Brownian dynamics on a four-well potential
   * - ``MullerPotential(random_state=None)``
     - 10
     - ``(10000, 2)``
     - 2D Brownian dynamics on the Müller–Brown potential

``random_state`` controls caching:

- an **integer** simulates once and caches the result under
  ``<data_home>/<name>/version-1/randomstate-<n>/``, so later calls load the same
  data;
- **None** runs a new simulation every time and caches nothing. In
  particular ``DoubleWell(random_state=None).get_cached()`` fails, because there
  is nothing to load.

``doublewell_eigs(n_grid, lag_time=1)`` and ``quadwell_eigs(n_grid, lag_time=1)``
return the reference eigenvalues and eigenvectors of the 1D systems, computed
on a grid, for checking estimated models. :func:`~msmbuilder.example_datasets.load_doublewell`, :func:`~msmbuilder.example_datasets.load_quadwell`
and :func:`~msmbuilder.example_datasets.load_muller` are function forms of the classes.

Where data is stored
--------------------

``get_data_home(data_home=None)`` returns the cache directory:

1. the ``data_home`` argument, if given;
2. otherwise the ``MSMBUILDER_DATA`` environment variable;
3. otherwise ``~/msmbuilder_data``.

``clear_data_home()`` deletes the cache. If the ``msmb_data`` conda package is
installed (``has_msmb_data()`` returns its path), the MD datasets are copied
from it instead of downloaded.

To pre-fetch every data set used by the tests, run
``python msmbuilder/tests/data_init.py``.

