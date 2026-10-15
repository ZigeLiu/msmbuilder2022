.. _guide-commands:

msmbuilder.commands
===================

Source: `msmbuilder/commands/ <https://github.com/msmbuilder/msmbuilder2022/tree/main/msmbuilder/commands>`__ 
The subcommands of the ``msmb`` command-line tool. Each subcommand wraps one
estimator class, and its options are generated automatically from that
class's ``__init__`` signature and numpydoc docstring (see ``cmdline.py``). Run
``msmb -h`` for the list and ``msmb <Command> -h`` for the options of one
command.

How the commands fit together
-----------------------------

Commands read and write **datasets**: lists of arrays stored on disk, opened
with ``msmbuilder.dataset.dataset()``. Featurizer commands write a directory of
``.npy`` files (one per trajectory). Fit-and-transform commands (preprocessing,
decomposition, clustering) write a single HDF5 file and append ``.h5`` to the
name you give with ``-t``. A typical command-line workflow:

.. code-block:: bash

    msmb AlanineDipeptide --data_home ./data            # download example data
    msmb DihedralFeaturizer --top data/alanine_dipeptide/ala2.pdb \
         --trjs "data/alanine_dipeptide/*.dcd" --transformed diheds      # -> diheds/
    msmb tICA -i diheds -t tica_trajs --n_components 4 --lag_time 2     # -> tica_trajs.h5
    msmb KMeans -i tica_trajs.h5 -t labels --n_clusters 100 --n_init 10 # -> labels.h5
    msmb MarkovStateModel -i labels.h5 -o msm.pkl --lag_time 2

Fitted models are pickled; load them in Python with
``from msmbuilder.utils import load``.

Command groups
--------------

.. list-table::
   :header-rows: 1

   * - Group
     - Commands
     - Defined in
   * - Setup
     - ``AtomIndices`` (write atom or atom-pair index files), ``ConvertChunkedProject`` (merge chunked trajectories), :class:`~msmbuilder.io.TemplateProject` (generate an analysis project)
     - ``atom_indices.py``, ``convert_chunked_project.py``, ``template_project.py``
   * - Example data
     - :class:`~msmbuilder.example_datasets.AlanineDipeptide`, :class:`~msmbuilder.example_datasets.FsPeptide`, :class:`~msmbuilder.example_datasets.MetEnkephalin`, :class:`~msmbuilder.example_datasets.DoubleWell`, :class:`~msmbuilder.example_datasets.QuadWell`, :class:`~msmbuilder.example_datasets.MullerPotential`
     - ``example_datasets.py``
   * - Featurizers
     - :class:`~msmbuilder.featurizer.DihedralFeaturizer`, :class:`~msmbuilder.featurizer.AlphaAngleFeaturizer`, :class:`~msmbuilder.featurizer.KappaAngleFeaturizer`, :class:`~msmbuilder.featurizer.AngleFeaturizer`, :class:`~msmbuilder.featurizer.AtomPairsFeaturizer`, :class:`~msmbuilder.featurizer.ContactFeaturizer`, :class:`~msmbuilder.featurizer.BinaryContactFeaturizer`, :class:`~msmbuilder.featurizer.LogisticContactFeaturizer`, :class:`~msmbuilder.featurizer.DRIDFeaturizer`, :class:`~msmbuilder.featurizer.RMSDFeaturizer`, :class:`~msmbuilder.featurizer.LandMarkRMSDFeaturizer`, :class:`~msmbuilder.featurizer.SuperposeFeaturizer`, :class:`~msmbuilder.featurizer.RawPositionsFeaturizer`, :class:`~msmbuilder.featurizer.SASAFeaturizer`, :class:`~msmbuilder.featurizer.VonMisesFeaturizer`, :class:`~msmbuilder.featurizer.GaussianSolventFeaturizer`, :class:`~msmbuilder.featurizer.LigandContactFeaturizer`, :class:`~msmbuilder.featurizer.BinaryLigandContactFeaturizer`, :class:`~msmbuilder.featurizer.LigandRMSDFeaturizer`
     - ``featurizer.py``
   * - Preprocessing
     - :class:`~msmbuilder.preprocessing.Butterworth`, :class:`~msmbuilder.preprocessing.DoubleEWMA`, :class:`~msmbuilder.preprocessing.StandardScaler`, :class:`~msmbuilder.preprocessing.RobustScaler`
     - ``fit_transform.py``
   * - Clustering
     - :class:`~msmbuilder.cluster.KMeans`, :class:`~msmbuilder.cluster.MiniBatchKMeans`, :class:`~msmbuilder.cluster.KCenters`, :class:`~msmbuilder.cluster.KMedoids`, :class:`~msmbuilder.cluster.MiniBatchKMedoids`, :class:`~msmbuilder.cluster.RegularSpatial`, :class:`~msmbuilder.cluster.LandmarkAgglomerative`, :class:`~msmbuilder.cluster.GMM`, :class:`~msmbuilder.cluster.MeanShift`, :class:`~msmbuilder.cluster.NDGrid`, :class:`~msmbuilder.cluster.SpectralClustering`, :class:`~msmbuilder.cluster.AffinityPropagation`, :class:`~msmbuilder.cluster.AgglomerativeClustering`, :class:`~msmbuilder.cluster.APM`
     - ``fit_transform.py``
   * - Decomposition
     - :class:`~msmbuilder.decomposition.tICA`, :class:`~msmbuilder.decomposition.SparseTICA`, :class:`~msmbuilder.decomposition.KSparseTICA`, :class:`~msmbuilder.decomposition.KernelTICA`, :class:`~msmbuilder.decomposition.PCA`, :class:`~msmbuilder.decomposition.SparsePCA`, :class:`~msmbuilder.decomposition.MiniBatchSparsePCA`, :class:`~msmbuilder.decomposition.FastICA`, :class:`~msmbuilder.decomposition.FactorAnalysis`
     - ``fit_transform.py``
   * - Models
     - :class:`~msmbuilder.msm.MarkovStateModel`, :class:`~msmbuilder.msm.BayesianMarkovStateModel`, :class:`~msmbuilder.msm.ContinuousTimeMSM`, :class:`~msmbuilder.msm.BayesianContinuousTimeMSM`, :class:`~msmbuilder.hmm.GaussianHMM`, ``ImpliedTimescales``
     - ``fit.py``, ``implied_timescales.py``
   * - Apply a fitted model
     - ``TransformDataset``
     - ``transform.py``

Common options
--------------

.. list-table::
   :header-rows: 1

   * - Command kind
     - Options
   * - Featurizers
     - ``--trjs`` (glob of trajectory files), ``--top`` (topology), ``--transformed`` (output dataset), ``-o/--out`` (pickle the featurizer), ``--stride``, ``--chunk``
   * - Fit-and-transform commands (preprocessing, clustering, decomposition)
     - ``-i/--inp`` (input dataset), ``-t/--transformed`` (output dataset), ``-o/--out`` (pickle the fitted model); at least one of ``-t``/``-o``
   * - RMSD-capable clusterers (:class:`~msmbuilder.cluster.KCenters`, :class:`~msmbuilder.cluster.KMedoids`, :class:`~msmbuilder.cluster.MiniBatchKMedoids`, :class:`~msmbuilder.cluster.RegularSpatial`, :class:`~msmbuilder.cluster.LandmarkAgglomerative`)
     - With ``--metric rmsd``, ``-i`` is a glob of trajectories, plus ``--top``, ``--stride`` and ``--atom_indices``
   * - Model commands
     - ``-i/--inp`` (label dataset), ``-o/--out`` (pickle the model)
   * - ``TransformDataset``
     - ``-i/--inp`` (dataset), ``-m/--model`` (a pickled fitted model), ``-t/--transformed`` (output dataset)
   * - ``ImpliedTimescales``
     - ``-i/--inp``, ``-l/--lag_times`` (range such as ``1:50``), ``--n_timescales``, ``--out``, ``--fmt {csv,json,excel}``

All estimator parameters appear as ``--<parameter>`` options with the
estimator's defaults.

