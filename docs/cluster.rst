.. _cluster:
.. currentmodule:: msmbuilder.cluster

msmbuilder.cluster
==================

Source: `msmbuilder/cluster/ <https://github.com/msmbuilder/msmbuilder2022/tree/main/msmbuilder/cluster>`__ 

Clustering turns continuous trajectories (feature arrays, tICA coordinates or raw ``mdtraj.Trajectory`` objects) into discrete state labels.
All clusterers follow the same multi-sequence API:

.. list-table::
   :header-rows: 1

   * - Method
     - Description
   * - ``fit(sequences)``
     - Fit the cluster module on all input trajectories
   * - ``predict(sequences)`` / ``transform(sequences)``
     - Return a list of 1D cluster label arrays, one per trajectory with fitted cluster module
   * - ``partial_predict(X)`` / ``partial_transform(X)``
     - Return cluster label array for single input trajectory
   * - ``fit_predict(sequences)`` / ``fit_transform(sequences)``
     - Fit the cluster module and return cluster label arrays


Clusterers implemented in msmbuilder
------------------------------------

These support ``metric`` in `{"euclidean", "sqeuclidean", "cityblock",
"chebyshev", "canberra", "braycurtis", "hamming", "jaccard", "rmsd"}`. With
``metric="rmsd"`` the input must be a list of ``mdtraj.Trajectory`` objects and
cluster centers are trajectories too.

.. list-table::
   :header-rows: 1

   * - Class
     - Description
   * - ``KCenters(n_clusters=8, metric='euclidean', random_state=None)``
     - Greedy farthest-point clustering. Fast; clusters have roughly equal radius. Attributes: ``cluster_centers_``, ``cluster_ids_``, ``distances_``, ``inertia_``
   * - ``KMedoids(n_clusters=8, n_passes=1, metric='euclidean', random_state=None)``
     - K-medoids (centers are actual data points)
   * - ``MiniBatchKMedoids(n_clusters=8, max_iter=5, batch_size=100, metric='euclidean', ...)``
     - Mini-batch k-medoids for large data sets
   * - ``RegularSpatial(d_min, metric='euclidean')``
     - Adds a new center whenever a point is farther than ``d_min`` from all existing centers
   * - ``LandmarkAgglomerative(n_clusters, n_landmarks=None, linkage='average', metric='euclidean', landmark_strategy='stride', ...)``
     - Hierarchical clustering. With ``n_landmarks``, only a subset of points is clustered and the rest are assigned to the nearest landmark, which saves memory

Other clusterers implemented here:

.. list-table::
   :header-rows: 1

   * - Class
     - Description
   * - ``NDGrid(n_bins_per_feature, min=None, max=None)``
     - Splits each feature into equal bins and labels frames by grid cell. Useful for 1–2D toy systems
   * - ``APM(metric='rmsd', n_macrostates=6, max_iter=50, lag_time=10, sub_clus=2, random_state=None)``
     - Automatic state Partitioning for Multibody systems: repeatedly splits states with k-centers and lumps them with PCCA until macrostates are metastable. Sets ``labels_`` (microstates) and ``MacroAssignments_`` (macrostates)

scikit-learn clusterers, adapted to lists of sequences
------------------------------------------------------

:class:`~msmbuilder.cluster.KMeans`, :class:`~msmbuilder.cluster.MiniBatchKMeans`, :class:`~msmbuilder.cluster.GMM` (``sklearn.mixture.GaussianMixture``),
:class:`~msmbuilder.cluster.MeanShift`, :class:`~msmbuilder.cluster.SpectralClustering`, :class:`~msmbuilder.cluster.AffinityPropagation` and
:class:`~msmbuilder.cluster.AgglomerativeClustering`. They take the same parameters as in scikit-learn.
:class:`~msmbuilder.cluster.KMeans` and :class:`~msmbuilder.cluster.MiniBatchKMeans` also accept ``sample_weight`` in ``fit``.

Example
-------

.. code-block:: python

    from msmbuilder.example_datasets import AlanineDipeptide
    from msmbuilder.featurizer import DihedralFeaturizer
    from msmbuilder.decomposition import tICA
    from msmbuilder.cluster import KCenters, MiniBatchKMeans

    trajs = AlanineDipeptide().get().trajectories
    Y = tICA(n_components=2, lag_time=10).fit_transform(DihedralFeaturizer().transform(trajs))

    kmeans = MiniBatchKMeans(n_clusters=100, random_state=0)
    labels = kmeans.fit_transform(Y)            # list of 1D int arrays

    # RMSD-based clustering directly on trajectories
    kc = KCenters(n_clusters=20, metric="rmsd", random_state=0).fit(trajs)
    print(kc.cluster_centers_)                  # an mdtraj.Trajectory of 20 frames


Notes
-----

- **jaccard metric:** since v3.9.1 it matches
  ``scipy.spatial.distance.jaccard``. Inputs are treated as boolean
  (nonzero means true), so it is only meaningful for 0/1-like features.
- Results of :class:`~msmbuilder.cluster.KCenters`, :class:`~msmbuilder.cluster.KMedoids` and :class:`~msmbuilder.cluster.MiniBatchKMeans` depend on
  ``random_state``. Set it for reproducible state definitions.
