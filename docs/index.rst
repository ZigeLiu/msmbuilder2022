.. _msmbuilder:

msmbuilder Introduction
=======================

``msmbuilder`` builds Markov state models (MSMs) and related kinetic models from
molecular dynamics (MD) trajectories. Each subpackage covers one stage of that
workflow, and every stage follows the scikit-learn estimator API, so the stages
can be chained by hand or in an ``sklearn.pipeline.Pipeline``.

The analysis pipeline
---------------------

.. code-block:: text

    MD trajectories (mdtraj.Trajectory)
       │  featurizer / feature_extraction      → per-frame feature vectors
       │  feature_selection                    → combine or subset feature sets
       │  preprocessing                        → scale, smooth, filter
       │  decomposition                        → tICA / PCA: slow, low-dimensional coordinates
       │  cluster                              → discrete microstate labels
       │  msm / hmm                            → kinetic model (transition or rate matrix)
       │  lumping                              → coarse-grain into macrostates
       ▼  tpt                                  → pathways, committors, MFPTs, error bars

The analysis tools
---------------------

.. list-table::
   :header-rows: 1

   * - Tool
     - Tool candidates
   * - :doc:`Featurizer <featurizer>`
     - Turn trajectories into feature vectors (dihedrals, contacts, distances, RMSD, SASA, ...)
   * - :doc:`feature_selection <feature_selection>`
     - Combine featurizers, slice features, drop low-variance features
   * - :doc:`preprocessing <preprocessing>`
     - Scalers, normalizers and time-series smoothing filters that work on lists of trajectories
   * - :doc:`decomposition <decomposition>`
     - tICA (plain, sparse, kernel), PCA, ICA, factor analysis, Nyström kernel maps
   * - :doc:`cluster <cluster>`
     - K-means, k-centers, k-medoids, regular spatial, grid, landmark agglomerative, APM, ...
   * - :doc:`msm <msm>`
     - Discrete-time and continuous-time MSMs, Bayesian MSMs, implied timescales, validation tools
   * - :doc:`lumping <lumping>`
     - Coarse-graining microstates into macrostates: PCCA, PCCA+, BACE, MVCA
   * - :doc:`tpt <tpt>`
     - Transition path theory: committors, fluxes, top pathways, MFPTs, hub scores
   * - :doc:`commands <commands>`
     - The ``msmb`` command-line tool and its subcommands, such as ``msmb TemplateProject``

Conventions shared by every estimator
-------------------------------------

- **Input is a list of sequences.** ``fit(sequences)`` takes a list where each
  element is one trajectory: an ``mdtraj.Trajectory`` for featurizers, or a 2D
  array of shape ``(n_frames_i, n_features)`` for everything downstream.
  Trajectories may have different lengths. Keeping them separate matters
  because transitions are only counted within a trajectory.
- **partial_transform vs transform.** ``partial_transform(x)`` processes a
  single sequence; ``transform(xs)`` maps it over a list and returns a list.
- **summarize()** returns a text report for most fitted models.


Requirements
------------

Python 3.10 or later and NumPy 1.23 or later (NumPy 2 is supported). Building
from source needs Cython 3 and setuptools 69 or later, because several
subpackages (``msm``, ``hmm``, ``cluster``, ``decomposition``, ``libdistance``,
``example_datasets``) contain compiled extensions.

For full analysis examples, see `analysis notebooks <https://github.com/xuhuihuang/GME_tutorials/tree/main/tutorials>`_

.. toctree::
    :maxdepth: 1
    :hidden:

    featurizer
    feature_selection
    preprocessing
    decomposition
    cluster
    msm
    lumping
    tpt
    hmm
    example_datasets
    commands
    publications