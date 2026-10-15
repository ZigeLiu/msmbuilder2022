.. _msm:
.. currentmodule:: msmbuilder.msm

msmbuilder.msm
==============

Source: `msmbuilder/msm/ <https://github.com/msmbuilder/msmbuilder2022/tree/main/msmbuilder/msm>`__ 

Markov state models (MSMs) are a class of models that describe the dynamics 
of a system by discretizing its conformational space into a set of states and 
modeling the transitions between them. The input to an MSM is a set of trajectories 
(the label sequences produced by :ref:`cluster <cluster>`).
State labels can be any orderable values since models map them to internal
indices ``0 .. n_states_ - 1``.

Models
------

.. list-table::
   :header-rows: 1

   * - Class
     - Description
   * - ``MarkovStateModel(lag_time=1, n_timescales=None, reversible_type='mle', ergodic_cutoff='on', prior_counts=0, sliding_window=True, verbose=True)``
     - Discrete-time MSM. The standard choice
   * - ``BayesianMarkovStateModel(lag_time=1, n_samples=100, n_steps=0, n_chains=None, reversible=True, ...)``
     - Samples transition matrices from the posterior with MCMC (Metzner sampler); gives uncertainty on every derived quantity
   * - ``ContinuousTimeMSM(lag_time=1, n_timescales=None, ergodic_cutoff=1, sliding_window=True, guess='log')``
     - Reversible rate-matrix (master equation) model fitted by maximum likelihood
   * - ``BayesianContinuousTimeMSM(lag_time=1, n_samples=2000, n_steps=25, epsilon=0.0005, ...)``
     - Posterior sampling of rate matrices with Hamiltonian Monte Carlo

Important MarkovStateModel parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **lag_time** (frames): transitions are counted between frames ``t`` and
  ``t + lag_time``. Choose it where implied timescales have leveled off.
- **reversible_type**: ``'mle'`` (maximum-likelihood reversible estimate,
  default), ``'transpose'`` (symmetrize the counts) or ``None`` (non-reversible).
- **ergodic_cutoff**: states not in the largest strongly connected set are
  trimmed. ``'on'`` uses the smallest count threshold, a number sets the
  threshold, ``'off'`` or ``0`` disables trimming. Trimmed states are absent from
  ``mapping_``.
- **prior_counts**: pseudocounts added to every element of the count matrix
  after trimming.
- **sliding_window**: count transitions starting at every frame (``True``) or
  only every ``lag_time`` frames (``False``).

Fitted attributes
~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Attribute
     - Meaning
   * - ``n_states_``
     - Number of states kept after ergodic trimming
   * - ``mapping_``
     - Dict from input label to internal index
   * - ``countsmat_``, ``transmat_``
     - Count and transition matrices, shape ``(n_states_, n_states_)``
   * - ``populations_``
     - Stationary distribution
   * - ``timescales_``
     - Implied timescales ``-lag_time / ln(λ_i)``, in frames of the input data
   * - ``eigenvalues_``, ``left_eigenvectors_``, ``right_eigenvectors_``
     - Eigensystem of ``transmat_``
   * - ``score_``
     - GMRQ on the training data

Methods
~~~~~~~

.. list-table::
   :header-rows: 1

   * - Method
     - Description
   * - ``transform(sequences, mode='clip')``
     - Map labels to internal indices. ``'clip'`` drops trimmed states (splitting trajectories if needed); ``'fill'`` replaces them with NaN
   * - ``inverse_transform(sequences)``
     - Map internal indices back to the original labels
   * - ``eigtransform(sequences, right=True, mode='clip')``
     - Project trajectories onto the dynamical eigenvectors
   * - ``score(sequences)``
     - GMRQ of the model on new data, for cross-validation
   * - ``score_ll(sequences)``
     - Log-likelihood of sequences under the model
   * - ``sample_discrete(state=None, n_steps=100, random_state=None)``
     - Generate a synthetic state trajectory. ``sample()`` is a deprecated alias
   * - ``draw_samples(sequences, n_samples)``
     - Pick ``(trajectory, frame)`` pairs from each state
   * - ``uncertainty_eigenvalues()``, ``uncertainty_timescales()``
     - Analytic standard errors
   * - ``summarize()``
     - Text report

Functions
---------

.. list-table::
   :header-rows: 1

   * - Function
     - Description
   * - ``implied_timescales(sequences, lag_times, n_timescales=10, msm=None, n_jobs=1)``
     - Fit one MSM per lag time and return an array of timescales, shape ``(len(lag_times), n_timescales)``, in frames. Plot it to choose the lag time

Validation (``msm.validation``)
-------------------------------

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - ``BootStrapMarkovStateModel(n_samples=10, n_procs=None, msm_args=None, save_all_models=False)``
     - Refits MSMs on trajectories resampled with replacement. Gives means, standard deviations and standard errors of populations (``mapped_populations_mean_``, ``_std_``, ``_sem_``) and train/test GMRQ scores
   * - ``transmat_errorbar.create_perturb_params(countsmat, transmat=None)``
     - Returns the transition matrix and the standard error of each element, treating each row's counts as Bernoulli trials
   * - ``transmat_errorbar.perturb_tmat(transmat, scale)``
     - Draws a transition matrix by perturbing each element with Gaussian noise of that standard error, then renormalizing rows. Use it repeatedly to bootstrap any derived quantity

Example
-------

.. code-block:: python

    import numpy as np
    from msmbuilder.example_datasets import AlanineDipeptide
    from msmbuilder.featurizer import DihedralFeaturizer
    from msmbuilder.cluster import MiniBatchKMeans
    from msmbuilder.msm import MarkovStateModel, implied_timescales
    from msmbuilder.msm.validation.transmat_errorbar import create_perturb_params, perturb_tmat

    trajs = AlanineDipeptide().get().trajectories
    X = DihedralFeaturizer().transform(trajs)
    labels = MiniBatchKMeans(n_clusters=50, random_state=0).fit_transform(X)

    its = implied_timescales(labels, lag_times=[1, 5, 10, 20], n_timescales=3)

    msm = MarkovStateModel(lag_time=10, verbose=False).fit(labels)
    print(msm.summarize())

    T, scale = create_perturb_params(msm.countsmat_)
    T_sample = perturb_tmat(T, scale)            # one bootstrap draw
