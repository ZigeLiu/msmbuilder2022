.. _featurizer:
.. currentmodule:: msmbuilder.featurizer

msmbuilder.featurizer
=====================

Source: `msmbuilder/featurizer/ <https://github.com/msmbuilder/msmbuilder2022/tree/main/msmbuilder/featurizer>`__ 

Featurizers turn MD trajectories (``mdtraj.Trajectory``) into numeric feature
vectors, one vector per frame. This is the first step of an MSM analysis: the
choice of features decides which motions the downstream tICA, clustering and
MSM can see.

The Featurizer interface
------------------------

Every featurizer provides the same interface, so they can be swapped in and out of a pipeline. :

.. list-table::
   :header-rows: 1

   * - Method
     - Description
   * - ``partial_transform(traj)``
     - Featurize one trajectory. Returns an array of shape ``(traj.n_frames, n_features)``
   * - ``transform(trajs)``
     - Featurize a list of trajectories. Returns a list of arrays
   * - ``describe_features(traj)``
     - Dictionary describing each feature with the atoms participating in each feature


Available featurizers
---------------------

Angles
~~~~~~

.. list-table::
   :header-rows: 1

   * - Class
     - Features
     - Key parameters
   * - :class:`~msmbuilder.featurizer.DihedralFeaturizer`
     - Backbone/side-chain dihedrals
     - ``types=['phi', 'psi']`` (also ``omega``, ``chi1``\ –\ ``chi4``); ``sincos=True`` outputs sin and cos of each angle (2 columns per angle)
   * - :class:`~msmbuilder.featurizer.VonMisesFeaturizer`
     - Dihedrals soft-binned on the circle with von Mises kernels
     - ``types``, ``n_bins=18``, ``kappa=20.0``. Outputs ``n_bins`` columns per angle
   * - :class:`~msmbuilder.featurizer.AlphaAngleFeaturizer`
     - Dihedrals between consecutive Cα atoms
     - ``sincos=True``
   * - :class:`~msmbuilder.featurizer.KappaAngleFeaturizer`
     - Angle between Cα(i−offset), Cα(i), Cα(i+offset)
     - ``cos=True``, ``offset=2``
   * - :class:`~msmbuilder.featurizer.AngleFeaturizer`
     - Arbitrary angles between atom triplets
     - ``angle_indices`` (array of ``(i, j, k)``), ``cos=True``

Distances and contacts
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Class
     - Features
     - Key parameters
   * - :class:`~msmbuilder.featurizer.AtomPairsFeaturizer`
     - Distances between atom pairs
     - ``pair_indices`` (shape ``(n_pairs, 2)``), ``periodic=False``, ``exponent=1.0``
   * - :class:`~msmbuilder.featurizer.ContactFeaturizer`
     - Residue–residue distances
     - ``contacts='all'`` or an array of residue pairs, ``scheme`` in ``{'ca', 'closest', 'closest-heavy'}``, ``ignore_nonprotein=True``, ``soft_min=False``, ``periodic=True``
   * - :class:`~msmbuilder.featurizer.BinaryContactFeaturizer`
     - 1 if a contact is below ``cutoff`` (nm), else 0
     - ``cutoff=0.8`` plus the :class:`~msmbuilder.featurizer.ContactFeaturizer` options
   * - :class:`~msmbuilder.featurizer.LogisticContactFeaturizer`
     - Logistic transform of contact distances
     - ``center=0.8``, ``steepness=20``
   * - :class:`~msmbuilder.featurizer.DRIDFeaturizer`
     - Distribution of reciprocal interatomic distances
     - ``atom_indices``
   * - :class:`~msmbuilder.featurizer.GaussianSolventFeaturizer`
     - Gaussian-weighted solute–solvent distances
     - ``solute_indices``, ``solvent_indices``, ``sigma``, ``periodic=False``
   * - :class:`~msmbuilder.featurizer.CommonContactFeaturizer`
     - Contacts between residues aligned across different sequences
     - ``alignment`` (list or dict), same options as :class:`~msmbuilder.featurizer.ContactFeaturizer`

Structural similarity and coordinates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Class
     - Features
     - Key parameters
   * - :class:`~msmbuilder.featurizer.RMSDFeaturizer`
     - RMSD to each frame of a reference trajectory
     - ``reference_traj``, ``atom_indices``
   * - :class:`~msmbuilder.featurizer.LandMarkRMSDFeaturizer`
     - Gaussian kernel of RMSD to landmark frames
     - ``reference_traj``, ``atom_indices``, ``sigma=0.3``
   * - :class:`~msmbuilder.featurizer.SuperposeFeaturizer`
     - Per-atom distances to a reference after superposition
     - ``atom_indices``, ``reference_traj``, ``superpose_atom_indices``
   * - :class:`~msmbuilder.featurizer.RawPositionsFeaturizer`
     - Cartesian coordinates (optionally after superposing on ``ref_traj``)
     - ``atom_indices``, ``ref_traj``
   * - :class:`~msmbuilder.featurizer.SASAFeaturizer`
     - Solvent-accessible surface area per residue or per atom
     - ``mode='residue'`` or ``'atom'``; extra keyword arguments go to ``mdtraj.shrake_rupley``

Protein–ligand systems (``multichain.py``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Class
     - Features
   * - :class:`~msmbuilder.featurizer.LigandFeaturizer`
     - Base class. Detects the protein and ligand chains (``protein_chain='auto'``, ``ligand_chain='auto'``) using ``reference_frame``
   * - :class:`~msmbuilder.featurizer.LigandContactFeaturizer`
     - Ligand–residue distances, optionally restricted to a ``binding_pocket`` radius; ``periodic=True``
   * - :class:`~msmbuilder.featurizer.BinaryLigandContactFeaturizer`
     - Binary ligand–residue contacts below ``cutoff``
   * - :class:`~msmbuilder.featurizer.LigandRMSDFeaturizer`
     - RMSD of the ligand (or protein, or custom atoms) after aligning on the protein, ligand or custom atoms

Example
-------

.. code-block:: python

    import pandas as pd
    from msmbuilder.example_datasets import AlanineDipeptide
    from msmbuilder.featurizer import DihedralFeaturizer

    trajs = AlanineDipeptide().get().trajectories
    feat = DihedralFeaturizer(types=["phi", "psi"], sincos=True)

    X = feat.transform(trajs)            # list of arrays, one per trajectory
    print(X[0].shape)                    # (n_frames, 4): sin/cos of phi and psi

    desc = pd.DataFrame(feat.describe_features(trajs[0]))
    print(desc[["featuregroup", "otherinfo", "resnames"]])


Notes and caveats
-----------------

- **VonMisesFeaturizer.n_bins**: the bin centers (``loc``) are computed in
  ``__init__``. Changing ``n_bins`` later with ``set_params(n_bins=...)`` (for
  example in a grid search) does not recompute them. Create a new featurizer
  instead.
- **SASAFeaturizer on Windows**: mdtraj's ``shrake_rupley`` has a data race in
  its OpenMP loop, so on builds with OpenMP (the Windows wheels) results for
  multi-frame trajectories can occasionally be wrong. Featurize one frame at a
  time or set ``OMP_NUM_THREADS=1`` if you need exact, reproducible values.
- **Periodic boundaries**: :class:`~msmbuilder.featurizer.ContactFeaturizer` and the ligand featurizers
  default to ``periodic=True`` (minimum-image distances), matching
  ``mdtraj.compute_contacts``. :class:`~msmbuilder.featurizer.AtomPairsFeaturizer` defaults to
  ``periodic=False``.
- **Units** follow mdtraj: distances in nm, angles in radians, SASA in nm².
