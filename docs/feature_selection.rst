.. _feature_selection:
.. currentmodule:: msmbuilder.feature_selection

msmbuilder.feature_selection
============================

Source: `msmbuilder/feature_selection/ <https://github.com/msmbuilder/msmbuilder2022/tree/main/msmbuilder/feature_selection>`__ 

Tools for combining feature sets and choosing which features to keep.

.. list-table::
   :header-rows: 1

   * - Class
     - Input
     - Description
   * - ``FeatureSelector(features, which_feat=None)``
     - Trajectories
     - Runs several named featurizers and concatenates their outputs column-wise
   * - ``FeatureSlicer(feat, indices)``
     - Trajectories
     - Runs one featurizer and keeps only the columns in ``indices``
   * - ``VarianceThreshold(threshold=0.0)``
     - Feature arrays
     - scikit-learn's :class:`~msmbuilder.feature_selection.VarianceThreshold`, adapted to lists of sequences; drops columns whose variance is below ``threshold``

FeatureSelector
---------------

``features`` is a list of ``(name, featurizer)`` tuples. ``which_feat`` picks the
active featurizers by name: a single string, a list of names, or ``None`` for
all of them. You can change it after construction:

- a string is wrapped into a one-element list;
- a ``dict`` raises ``TypeError``;
- a name that is not in ``features`` raises ``ValueError``.

Columns appear in the order of ``which_feat``, and ``describe_features`` follows
the same order, so its rows line up with the output columns.

.. code-block:: python

    from msmbuilder.example_datasets import AlanineDipeptide
    from msmbuilder.featurizer import DihedralFeaturizer, AtomPairsFeaturizer, get_atompair_indices
    from msmbuilder.feature_selection import FeatureSelector

    trajs = AlanineDipeptide().get().trajectories
    _, pairs = get_atompair_indices(trajs[0])     # returns (atom_indices, pair_indices)

    selector = FeatureSelector([
        ("dihedrals", DihedralFeaturizer()),
        ("distances", AtomPairsFeaturizer(pairs)),
    ])
    X_all = selector.transform(trajs)

    selector.which_feat = "dihedrals"       # keep only the dihedral block
    X_dih = selector.transform(trajs)

Combined feature sets usually have very different scales (radians vs nm), so
follow a :class:`~msmbuilder.feature_selection.FeatureSelector` with ``msmbuilder.preprocessing.StandardScaler``.

FeatureSlicer
-------------

Keeps a subset of one featurizer's columns. ``indices`` may be an ``int``, a list
or a NumPy array; a single integer gives a 1D output per trajectory.

.. code-block:: python

    from msmbuilder.feature_selection import FeatureSlicer

    slicer = FeatureSlicer(DihedralFeaturizer(), indices=[0, 2])
    X = slicer.transform(trajs)                 # sin(phi), sin(psi) columns only
    print(slicer.describe_features(trajs[0]))   # descriptions of those two columns


