.. _decomposition:
.. currentmodule:: msmbuilder.decomposition

msmbuilder.decomposition
========================

Source: `msmbuilder/decomposition/ <https://github.com/msmbuilder/msmbuilder2022/tree/main/msmbuilder/decomposition>`__ 

Dimensionality reduction for feature trajectories. The main tool is
**tICA** (time-lagged independent component analysis), which finds the linear
combinations of features that decorrelate most slowly. Projecting onto the
first few tICA components before clustering gives MSMs that resolve the slow
dynamics much better than raw features.

All estimators take a list of 2D arrays (one per trajectory) and return a
list of 2D arrays with ``n_components`` columns.

tICA family
-----------

.. list-table::
   :header-rows: 1

   * - Class
     - Description
   * - ``tICA(n_components=None, lag_time=1, shrinkage=None, kinetic_mapping=False, commute_mapping=False)``
     - Standard tICA. Solves the generalized eigenproblem between the time-lagged correlation matrix and the covariance matrix
   * - ``SparseTICA(n_components=None, lag_time=1, rho=0.01, kinetic_mapping=False, epsilon=1e-06, shrinkage=None, tolerance=1e-06, maxiter=10000, verbose=False)``
     - tICA with an L1 penalty (``rho``) so each component uses only a few features
   * - ``KSparseTICA(n_components=None, lag_time=1, k=5, shrinkage=None, kinetic_mapping=True)``
     - Sparse tICA where each eigenvector has at most ``k`` nonzero entries
   * - ``KernelTICA(n_components=None, lag_time=1, kernel='rbf', gamma=None, degree=3, coef0=1.0, stride=1, landmarks=None, ...)``
     - Nonlinear tICA using a Nyström kernel approximation. Landmarks are taken every ``stride`` frames unless given explicitly

Key options
~~~~~~~~~~~

- **lag_time** (in frames) sets which timescale tICA looks for. Use a lag
  comparable to the MSM lag time you plan to use.
- **shrinkage**: covariance shrinkage intensity between 0 and 1. ``None``
  (default) estimates it with the Rao–Blackwellized Ledoit–Wolf formula,
  which helps when there are many features and few frames.
- **kinetic_mapping=True** scales each projected coordinate by its
  eigenvalue, so Euclidean distances in tICA space approximate kinetic
  distances. Recommended before clustering.
- **commute_mapping=True** scales by ``sqrt(timescale / 2)`` instead, giving
  commute distances. Only available on :class:`~msmbuilder.decomposition.tICA` (not on :class:`~msmbuilder.decomposition.SparseTICA`).

Fitted attributes (tICA)
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Attribute
     - Meaning
   * - ``components_``
     - Shape ``(n_components, n_features)``: the projection vectors
   * - ``eigenvalues_``, ``eigenvectors_``
     - Full generalized eigensystem, sorted slowest first
   * - ``timescales_``
     - Implied timescales ``-lag_time / ln(eigenvalue)``, in frames
   * - ``means_``, ``covariance_``, ``offset_correlation_``
     - Accumulated statistics
   * - ``score_``
     - GMRQ score on the training data

:class:`~msmbuilder.decomposition.tICA` also supports ``partial_fit(sequence)`` to accumulate statistics one
trajectory at a time, and ``score(sequences)`` to compute the GMRQ
(generalized matrix Rayleigh quotient) on held-out data for cross-validation.

Other decompositions
--------------------

scikit-learn estimators wrapped to accept lists of sequences:

.. list-table::
   :header-rows: 1

   * - Class
     - Description
   * - :class:`~msmbuilder.decomposition.PCA`, :class:`~msmbuilder.decomposition.SparsePCA`, :class:`~msmbuilder.decomposition.MiniBatchSparsePCA`
     - Principal component analysis (no time information)
   * - :class:`~msmbuilder.decomposition.FastICA`
     - Independent component analysis
   * - :class:`~msmbuilder.decomposition.FactorAnalysis`
     - Factor analysis

In ``decomposition.kernel_approximation`` (not re-exported from the package):

.. list-table::
   :header-rows: 1

   * - Class
     - Description
   * - :class:`~msmbuilder.decomposition.kernel_approximation.Nystroem`
     - scikit-learn's Nyström kernel map, adapted to lists of sequences
   * - ``LandmarkNystroem(landmarks=None, ...)``
     - Nyström map with user-supplied landmark frames; used by :class:`~msmbuilder.decomposition.KernelTICA`

Example
-------

.. code-block:: python

    from msmbuilder.example_datasets import AlanineDipeptide
    from msmbuilder.featurizer import DihedralFeaturizer
    from msmbuilder.decomposition import tICA

    trajs = AlanineDipeptide().get().trajectories
    X = DihedralFeaturizer().transform(trajs)

    tica = tICA(n_components=2, lag_time=10, kinetic_mapping=True)
    Y = tica.fit_transform(X)          # list of (n_frames, 2) arrays
    print(tica.timescales_)            # in frames
    print(tica.summarize())

