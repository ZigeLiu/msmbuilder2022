.. _preprocessing:
.. currentmodule:: msmbuilder.preprocessing

msmbuilder.preprocessing
========================

Source: `msmbuilder/preprocessing/ <https://github.com/msmbuilder/msmbuilder2022/tree/main/msmbuilder/preprocessing>`__

Transforms applied to feature arrays between featurization and
decomposition/clustering. Everything in this package takes a **list of 2D arrays** (one
per trajectory) and returns a list of the same shapes, so trajectory
boundaries are preserved.

scikit-learn transformers, adapted to lists of sequences
--------------------------------------------------------

These are the scikit-learn classes of the same name, wrapped so that ``fit``
accepts a list of arrays. They learn their statistics from all trajectories
together, then transform each trajectory separately.

.. list-table::
   :header-rows: 1

   * - Class
     - Typical use
   * - :class:`~msmbuilder.preprocessing.StandardScaler`
     - Zero mean, unit variance per feature. Recommended after combining feature sets with different units
   * - :class:`~msmbuilder.preprocessing.RobustScaler`
     - Scale with median and interquartile range (less sensitive to outliers)
   * - :class:`~msmbuilder.preprocessing.MinMaxScaler`, :class:`~msmbuilder.preprocessing.MaxAbsScaler`
     - Scale each feature to a fixed range
   * - :class:`~msmbuilder.preprocessing.Normalizer`
     - Scale each frame (row) to unit norm
   * - :class:`~msmbuilder.preprocessing.Binarizer`
     - Threshold features to 0/1
   * - :class:`~msmbuilder.preprocessing.PolynomialFeatures`
     - Add polynomial and interaction terms
   * - :class:`~msmbuilder.preprocessing.Imputer`
     - Fill missing values (``sklearn.impute.SimpleImputer``)
   * - :class:`~msmbuilder.preprocessing.KernelCenterer`, :class:`~msmbuilder.preprocessing.FunctionTransformer`, :class:`~msmbuilder.preprocessing.LabelBinarizer`, :class:`~msmbuilder.preprocessing.MultiLabelBinarizer`
     - As in scikit-learn


Time-series smoothing filters
-----------------------------

Each trajectory is filtered independently, so smoothing never crosses a trajectory boundary.

.. list-table::
   :header-rows: 1

   * - Class
     - Description
   * - ``Butterworth(width=5, order=3)``
     - Zero-delay low-pass Butterworth filter (forward–backward ``filtfilt``). ``width`` behaves like a moving-average window and is rounded up to an odd integer; it must be an integer > 1
   * - ``EWMA(com=None, span=None, halflife=None, min_periods=0, adjust=True)``
     - Exponentially weighted moving average via ``pandas.DataFrame.ewm``. Specify exactly one of ``com``, ``span`` or ``halflife``
   * - ``DoubleEWMA(...)``
     - Same parameters as :class:`~msmbuilder.preprocessing.EWMA`. Intended to average a forward and a backward EWMA so the result has no time lag; see the caveat below

Example
-------

.. code-block:: python

    from msmbuilder.example_datasets import AlanineDipeptide
    from msmbuilder.featurizer import DihedralFeaturizer
    from msmbuilder.preprocessing import StandardScaler, Butterworth

    trajs = AlanineDipeptide().get().trajectories
    X = DihedralFeaturizer().transform(trajs)

    X_scaled = StandardScaler().fit_transform(X)
    X_smooth = Butterworth(width=11).fit_transform(X_scaled)
