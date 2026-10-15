.. _hmm:
.. currentmodule:: msmbuilder.hmm

msmbuilder.hmm
==============

Source: `msmbuilder/hmm/ <https://github.com/msmbuilder/msmbuilder2022/tree/main/msmbuilder/hmm>`__ 

Hidden Markov models (HMMs) fitted directly to continuous feature
trajectories. Instead of clustering first and then counting transitions, an
HMM learns a small number of hidden states, each with its own emission
distribution, together with a reversible transition matrix. HMMs are useful
when you want a few-state kinetic model and the states overlap in feature
space.

Both models are implemented in C++ (Cython extensions ``gaussian.pyx`` and
``vonmises.pyx``) and accept lists of ``float32`` or ``float64`` arrays of shape
``(n_frames_i, n_features)``.

GaussianHMM
-----------

Reversible HMM with Gaussian emissions (diagonal covariances) and an optional
L1 "fusion" penalty that pulls the state means together, so features that do
not distinguish states are shared.

.. code-block:: text

    GaussianHMM(n_states, n_init=10, n_iter=10, n_lqa_iter=10, fusion_prior=0.01,
                thresh=0.01, reversible_type='mle', vars_prior=0.001, vars_weight=1,
                random_state=None, timing=False, n_hotstart='all', init_algo='kmeans')

.. list-table::
   :header-rows: 1

   * - Parameter
     - Meaning
   * - ``n_states``
     - Number of hidden states
   * - ``n_init``, ``n_iter``, ``thresh``
     - Number of random restarts, EM iterations per restart, and convergence threshold on the log-likelihood
   * - ``fusion_prior``, ``n_lqa_iter``
     - Strength of the L1 fusion penalty on the means, and the inner iterations used to solve it
   * - ``reversible_type``
     - ``'mle'`` or ``'transpose'``, as for :class:`~msmbuilder.msm.MarkovStateModel`
   * - ``vars_prior``, ``vars_weight``
     - Prior that keeps variances from collapsing in undersampled states
   * - ``init_algo``
     - ``'kmeans'`` (MiniBatchKMeans) or ``'GMM'`` (``sklearn.mixture.GaussianMixture`` with diagonal covariances) to initialize means and variances
   * - ``n_hotstart``
     - Number of sequences used for that initialization (``'all'`` by default)

Attributes after ``fit``: ``means_``, ``vars_``, ``transmat_``, ``populations_``,
``timescales_`` (in frames), ``fit_logprob_`` (log-likelihood per EM iteration).

VonMisesHMM
-----------

HMM with von Mises emissions, for **angular** data (dihedral angles in
radians, without sin/cos transformation).

.. code-block:: text

    VonMisesHMM(n_states, n_init=10, n_iter=10, thresh=0.01, reversible_type='mle', random_state=None)

Attributes after ``fit``: ``means_`` and ``kappas_`` (location and concentration
of each state's distribution), ``transmat_``, ``populations_``, ``timescales_``,
``fit_logprob_``, and ``overlap_`` (normalized log-overlap integrals between the
state distributions).

Methods (both models)
---------------------

.. list-table::
   :header-rows: 1

   * - Method
     - Returns
   * - ``fit(sequences)``
     - ``self``
   * - ``score(sequences)``
     - Total log-likelihood
   * - ``predict(sequences)``
     - **A tuple** ``(viterbi_logprob, hidden_sequences)``: the log-probability of the Viterbi path and a list of state-index arrays. This differs from scikit-learn, where ``predict`` returns only labels
   * - ``fit_predict(sequences)``
     - Same tuple as ``predict``, after fitting
   * - ``summarize()``
     - Text report

:class:`~msmbuilder.hmm.GaussianHMM` also has:

- ``draw_centroids(sequences)``: for each state, the ``(trajectory, frame)`` pair
  closest to its mean;
- ``draw_samples(sequences, n_samples, scheme='even', match_vars=False)``:
  ``(trajectory, frame)`` pairs sampled from each state. ``'maxent'`` uses the
  maximum-entropy discrete approximation in ``discrete_approx.py``.

Example
-------

.. code-block:: python

    from msmbuilder.example_datasets import AlanineDipeptide
    from msmbuilder.featurizer import DihedralFeaturizer
    from msmbuilder.hmm import GaussianHMM, VonMisesHMM

    trajs = AlanineDipeptide().get().trajectories

    X = DihedralFeaturizer(sincos=True).transform(trajs)
    ghmm = GaussianHMM(n_states=3, random_state=0).fit(X)
    logprob, states = ghmm.predict(X)
    print(ghmm.timescales_)

    angles = DihedralFeaturizer(sincos=False).transform(trajs)
    vmhmm = VonMisesHMM(n_states=3, random_state=0).fit(angles)
    print(vmhmm.means_, vmhmm.kappas_)

Notes
-----

- Both classes work inside ``sklearn.pipeline.Pipeline`` with scikit-learn 1.8
  and later (they accept dynamic attributes since v3.9.1).
- Results depend on ``random_state``; set it for reproducible states.
