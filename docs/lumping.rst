.. _lumping:
.. currentmodule:: msmbuilder.lumping

msmbuilder.lumping
==================

Source: `msmbuilder/lumping/ <https://github.com/msmbuilder/msmbuilder2022/tree/main/msmbuilder/lumping>`__

Coarse-graining ("lumping") of a microstate MSM into a few kinetically
meaningful macrostates. Microstate models need hundreds of states to be
accurate; lumping groups them into the handful of metastable states that are
easier to interpret.

Every lumper is a subclass of :class:`~msmbuilder.msm.MarkovStateModel`, so after fitting it has the
usual MSM attributes (``transmat_``, ``populations_``, ...) for the **microstate**
model, plus:

- ``microstate_mapping_``: array giving the macrostate of each microstate
  (internal microstate index → macrostate index);
- ``transform(sequences)`` / ``partial_transform(sequence)``: map microstate label
  trajectories to macrostate label trajectories.

There are two ways to use them:

.. code-block:: python

    # 1. Fit directly on microstate label sequences (fits the MSM internally)
    lumper = PCCAPlus(n_macrostates=4, lag_time=10).fit(labels)

    # 2. Reuse an MSM you already fit
    lumper = PCCAPlus.from_msm(msm, n_macrostates=4)

    macro_labels = lumper.transform(labels)

Keyword arguments not consumed by the lumper (``lag_time``, ``reversible_type``,
``ergodic_cutoff``, ...) are passed to :class:`~msmbuilder.msm.MarkovStateModel`.

Methods
-------

.. list-table::
   :header-rows: 1

   * - Class
     - Method
     - Key parameters
   * - ``PCCA(n_macrostates, pcca_tolerance=1e-05)``
     - Perron cluster analysis: splits states by the sign structure of the slowest right eigenvectors. Fast, but assignments can be fragile near boundaries
     - 
   * - ``PCCAPlus(n_macrostates, do_minimization=True, objective_function='crisp_metastability')``
     - Robust PCCA+: finds fuzzy memberships by optimizing an objective, then assigns each microstate to its most likely macrostate
     - ``objective_function`` in ``{'crisp_metastability', 'metastability', 'crispness'}``; ``from_msm(msm, n_macrostates, objective_function=None)`` also accepts it, and ``None`` means ``'crisp_metastability'``
   * - ``BACE(n_macrostates, filter=1.1, save_all_maps=True, n_proc=1, chunk_size=100)``
     - Bayesian agglomerative clustering: repeatedly merges the pair of states with the smallest Bayes factor
     - ``filter`` prunes poorly sampled states first. With ``save_all_maps=True``, ``map_dict[n]`` holds the mapping for every number of macrostates down to ``n_macrostates``, and ``bayesFactors[n]`` the corresponding Bayes factor
   * - ``MVCA(n_macrostates, metric=js_metric_array, fit_only=False, n_landmarks=None, landmark_strategy='stride', random_state=None)``
     - Minimum variance cluster analysis: agglomerative (Ward) clustering of the rows of the transition matrix, compared with a Jensen–Shannon metric
     - ``n_landmarks`` clusters only a subset of rows to save memory

Example
-------

.. code-block:: python

    from msmbuilder.example_datasets import AlanineDipeptide
    from msmbuilder.featurizer import DihedralFeaturizer
    from msmbuilder.cluster import MiniBatchKMeans
    from msmbuilder.msm import MarkovStateModel
    from msmbuilder.lumping import PCCAPlus

    trajs = AlanineDipeptide().get().trajectories
    X = DihedralFeaturizer().transform(trajs)
    labels = MiniBatchKMeans(n_clusters=50, random_state=0).fit_transform(X)

    msm = MarkovStateModel(lag_time=10, verbose=False).fit(labels)
    pccap = PCCAPlus.from_msm(msm, n_macrostates=3)
    print(pccap.microstate_mapping_)          # macrostate of each microstate
    macro_trajs = pccap.transform(labels)


References
----------

- PCCA+: Deuflhard & Weber, *Linear Algebra Appl.* 398, 161 (2005).
- BACE: Bowman, *J. Chem. Phys.* 137, 134111 (2012).
- MVCA: Husic, McKiernan, Wayment-Steele, Sultan & Pande, *J. Chem. Theory Comput.* 14, 1071 (2018).
