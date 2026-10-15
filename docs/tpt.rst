.. _tpt:
.. currentmodule:: msmbuilder.tpt

msmbuilder.tpt
==============

Source: `msmbuilder/tpt/ <https://github.com/msmbuilder/msmbuilder2022/tree/main/msmbuilder/tpt>`__ 
Transition path theory (TPT) and related analyses of a fitted MSM: which
states lead from a set of *sources* (for example, unfolded) to a set of
*sinks* (folded), how much reactive flux flows along each route, and how long
the transitions take.

Every function takes a fitted :class:`~msmbuilder.msm.MarkovStateModel` (or a model with the same
attributes, such as a lumped model). States are given as internal MSM indices
(``0 .. n_states_ - 1``); use ``msm.mapping_`` to convert from cluster labels.

Functions
---------

.. list-table::
   :header-rows: 1

   * - Function
     - Returns
   * - ``committors(sources, sinks, msm)``
     - Forward committor of each state: probability of reaching ``sinks`` before ``sources``. Shape ``(n_states,)``
   * - ``conditional_committors(source, sink, waypoint, msm)``
     - Probability of reaching ``sink`` before ``source`` *and* visiting ``waypoint`` on the way
   * - ``fluxes(sources, sinks, msm, for_committors=None)``
     - Reactive flux matrix, shape ``(n_states, n_states)``. Pass precomputed committors in ``for_committors`` to save time
   * - ``net_fluxes(sources, sinks, msm, for_committors=None)``
     - Net flux matrix (flux i→j minus j→i, clipped at zero)
   * - ``top_path(sources, sinks, net_flux)``
     - ``(path, flux)``: the highest-flux path (Dijkstra on the net flux) and its bottleneck flux
   * - ``paths(sources, sinks, net_flux, remove_path='subtract', num_paths=inf, flux_cutoff=1-1e-10)``
     - ``(paths, fluxes)``: successive top paths, removing each found path with ``'subtract'`` or ``'bottleneck'`` until ``num_paths`` or ``flux_cutoff`` of the total flux is reached
   * - ``mfpts(msm, sinks=None, lag_time=1.0, errors=False, n_samples=100)``
     - Mean first passage times. With ``sinks=None``, a matrix ``mfpts[i, j]`` from state *i* to *j*; with sinks, a vector of times from each state to the sink set. Times are in units of ``lag_time`` (pass the MSM lag time in ns to get ns)
   * - ``hub_scores(msm, waypoints=None)``
     - Hub score of each waypoint: how often transitions between other states pass through it
   * - ``fraction_visited(source, sink, waypoint, msm)``
     - Fraction of source→sink transitions that pass through ``waypoint``

Uncertainty in MFPTs
~~~~~~~~~~~~~~~~~~~~

``mfpts(..., errors=True, n_samples=N)`` draws ``N`` transition matrices with
:ref:`msm.validation.transmat_errorbar <msm>` (Gaussian perturbation of each
element by its finite-sampling standard error) and returns an array of ``N``
MFPT results; take its mean and standard deviation. For a
:class:`~msmbuilder.msm.BayesianMarkovStateModel` (which has ``all_transmats_``), :func:`~msmbuilder.tpt.mfpts` returns the
median over the posterior samples.

Example
-------

.. code-block:: python

    import numpy as np
    from msmbuilder.tpt import committors, net_fluxes, top_path, mfpts

    # msm: a fitted MarkovStateModel; pick source and sink states by index
    sources, sinks = [0], [msm.n_states_ - 1]

    q = committors(sources, sinks, msm)
    F = net_fluxes(sources, sinks, msm, for_committors=q)
    path, flux = top_path(sources, sinks, F)

    t = mfpts(msm, sinks=sinks, lag_time=msm.lag_time)       # in frames
    t_samples = mfpts(msm, sinks=sinks, lag_time=msm.lag_time, errors=True, n_samples=50)
    print(t[sources[0]], np.std(t_samples[:, sources[0]]))

References
----------

- Weinan & Vanden-Eijnden 2006
- Metzner, Schütte & Vanden-Eijnden 2009
- Berezhkovskii, Hummer & Szabo 2009
- Noé et al. 2009