.. _publications:

Publications
=============================

The following published works use MSMBuilder. To add your publication
to the list, open an issue on GitHub with the relevant information or
edit ``docs/publications.rst`` and submit a pull request.


Accurate Estimation of Protein Folding and Unfolding Times: Beyond Markov State Models
------------------------------------------------------------------------------------------

 * Ernesto Suárez; Joshua L. Adelman; Daniel M. Zuckerman
 * *J. Chem. Theory Comput.* **2016**,  
 * `doi: 10.1021/acs.jctc.6b00339 <http://dx.doi.org/10.1021/acs.jctc.6b00339>`_

Because standard molecular dynamics (MD) simulations are unable to access time
scales of interest in complex biomolecular systems, it is common to "stitch
together" information from multiple shorter trajectories using approximate
Markov state model (MSM) analysis. However, MSMs may require significant tuning
and can yield biased results. Here, by analyzing some of the longest protein MD
data sets available (>100 μs per protein), we show that estimators constructed
based on exact non-Markovian (NM) principles can yield significantly improved
mean first-passage times (MFPTs) for protein folding and unfolding. In some
cases, MSM bias of more than an order of magnitude can be corrected when
identical trajectory data are reanalyzed by non-Markovian approaches. The NM
analysis includes "history" information, higher order time correlations
compared to MSMs, that is available in every MD trajectory. The NM strategy is
insensitive to fine details of the states used and works well when a fine time-
discretization (i.e., small "lag time") is used.


Stochastic steps in secondary active sugar transport
--------------------------------------------------------------------------------

 * Adelman, Joshua L.; Ghezzi, Chiara; Bisignano, Paola; Loo, Donald D. F.; Choe, Seungho; Abramson, Jeff; Rosenberg, John M.; Wright, Ernest M.; Grabe, Michael
 * *Proc. Natl. Acad. Sci. USA* **2016**, 113 E3960--E3966
 * `doi: 10.1073/pnas.1525378113 <http://dx.doi.org/10.1073/pnas.1525378113>`_

Secondary active transporters, such as those that adopt the leucine-transporter
fold, are found in all domains of life, and they have the unique capability of
harnessing the energy stored in ion gradients to accumulate small molecules
essential for life as well as expel toxic and harmful compounds. How these
proteins couple ion binding and transport to the concomitant flow of substrates
is a fundamental structural and biophysical question that is beginning to be
answered at the atomistic level with the advent of high-resolution structures
of transporters in different structural states. Nonetheless, the dynamic
character of the transporters, such as ion/substrate binding order and how
binding triggers conformational change, is not revealed from static structures,
yet it is critical to understanding their function. Here, we report a series of
molecular simulations carried out on the sugar transporter vSGLT that lend
insight into how substrate and ions are released from the inward-facing state
of the transporter. Our simulations reveal that the order of release is
stochastic. Functional experiments were designed to test this prediction on the
human homolog, hSGLT1, and we also found that cytoplasmic release is not
ordered, but we confirmed that substrate and ion binding from the extracellular
space is ordered. Our findings unify conflicting published results concerning
cytoplasmic release of ions and substrate and hint at the possibility that
other transporters in the superfamily may lack coordination between ions and
substrate in the inward-facing state.


Conformational heterogeneity of the calmodulin binding interface
--------------------------------------------------------------------------------

 * Diwakar Shukla; Ariana Peck; Vijay S. Pande
 * *Nature Communications* **2016**, 7 10910
 * `doi: 10.1038/ncomms10910 <http://dx.doi.org/10.1038/ncomms10910>`_

Calmodulin (CaM) is a ubiquitous Ca2+ sensor and a crucial signalling hub in
many pathways aberrantly activated in disease. However, the mechanistic basis
of its ability to bind diverse signalling molecules including G-protein-coupled
receptors, ion channels and kinases remains poorly understood. Here we harness
the high resolution of molecular dynamics simulations and the analytical power
of Markov state models to dissect the molecular underpinnings of CaM binding
diversity. Our computational model indicates that in the absence of Ca2+, sub-
states in the folded ensemble of CaM's C-terminal domain present chemically and
sterically distinct topologies that may facilitate conformational selection.
Furthermore, we find that local unfolding is off-pathway for the exchange
process relevant for peptide binding, in contrast to prior hypotheses that
unfolding might account for binding diversity. Finally, our model predicts a
novel binding interface that is well-populated in the Ca2+-bound regime and,
thus, a candidate for pharmacological intervention.


Optimized parameter selection reveals trends in Markov state models for protein folding
-------------------------------------------------------------------------------------------------

 * Brooke E. Husic; Robert T. McGibbon; Mohammad M. Sultan; Vijay S. Pande
 * *J. Chem. Phys.* **2016**, 145 194103
 * `doi: 10.1063/1.4967809 <http://dx.doi.org/10.1063/1.4967809>`_

As molecular dynamics simulations access increasingly longer time scales,
complementary advances in the analysis of biomolecular time-series data are 
necessary. Markov state models offer a powerful framework for this analysis by
describing a system’s states and the transitions between them. A recently
established variational theorem for Markov state models now enables modelers to
systematically determine the best way to describe a system’s dynamics. In the
context of the variational theorem, we analyze ultra-long folding simulations
for a canonical set of twelve proteins [K. Lindorff-Larsen et al., Science 334,
517 (2011)] by creating and evaluating many types of Markov state models. We
present a set of guidelines for constructing Markov state models of protein
folding; namely, we recommend the use of cross-validation and a kinetically
motivated dimensionality reduction step for improved descriptions of folding
dynamics. We also warn that precise kinetics predictions rely on the features
chosen to describe the system and pose the description of kinetic uncertainty
across ensembles of models as an open issue.


Conserve Water: A Method for the Analysis of Solvent in Molecular Dynamics
--------------------------------------------------------------------------------

 * Matthew P. Harrigan; Diwakar Shukla; Vijay S. Pande
 * *J. Chem. Theory Comput.* **2015**, 11 1094--1101
 * `doi: 10.1021/ct5010017 <http://dx.doi.org/10.1021/ct5010017>`_

Molecular dynamics with explicit solvent is favored for its ability to more
correctly simulate aqueous biological processes and has become routine thanks
to increasingly powerful computational resources. However, analysis techniques
including Markov state models (MSMs) ignore solvent atoms and focus solely on
solute coordinates despite solvent being implicated in myriad biological
phenomena. We present a unified framework called “solvent-shells featurization”
for including solvent degrees of freedom in analysis and show that this method
produces better models. We apply this method to simulations of dewetting in the
two-domain protein BphC to generate a predictive MSM and identify functional
water molecules. Furthermore, the proposed methodology could be easily extended
for building MSMs of any systems with indistinguishable components.


Cloud-based simulations on Google Exacycle reveal ligand modulation of GPCR activation pathways
------------------------------------------------------------------------------------------------

 * Kai Kohlhoff; Diwakar Shukla; Morgan Lawrenz; Gregory Bowman; David Konerding; Dan Belov; Russ Altman; Vijay Pande
 * *Nat. Chem.* **2014**, 6 15--21
 * `doi: 10.1038/nchem.1821 <http://dx.doi.org/10.1038/nchem.1821>`_

Simulations can provide tremendous insight into the atomistic details of
biological mechanisms, but micro- to millisecond timescales are historically
only accessible on dedicated supercomputers. We demonstrate that cloud
computing is a viable alternative that brings long-timescale processes within
reach of a broader community. We used Google's Exacycle cloud-computing
platform to simulate two milliseconds of dynamics of a major drug target, the
G-protein-coupled receptor β2AR. Markov state models aggregate independent
simulations into a single statistical model that is validated by previous
computational and experimental results. Moreover, our models provide an
atomistic description of the activation of a G-protein-coupled receptor and
reveal multiple activation pathways. Agonists and inverse agonists interact
differentially with these pathways, with profound implications for drug design.


Equilibrium thermodynamics and folding kinetics of a short, fast-folding, beta-hairpin
---------------------------------------------------------------------------------------

 * Jimenez-Cruz, Camilo A.; Garcia, Angel E.
 * *Phys. Chem. Chem. Phys.* **2014**,  
 * `doi: 10.1039/C3CP54336F <http://dx.doi.org/10.1039/C3CP54336F>`_

Equilibrium thermodynamics of a short beta-hairpin are studied using unbiased
all-atom replica exchange molecular dynamics simulations in explicit solvent.
An exploratory analysis of the free energy landscape of the system is provided
in terms of various structural characteristics, for both the folded and
unfolded ensembles. We find that the favorable interactions between the ends
introduced by the tryptophan cap, along with the flexibility of the turn
region, explain the remarkable stability of the folded state. Charging of the N
termini results in effective roughening of the free energy landscape and
stabilization of non-native contacts. Folding-unfolding dynamics are further
discussed using a set of 2413 independent molecular dynamics simulations, 2 ns
to 20 ns long, at the melting temperature of the beta-hairpin. A novel method
for the construction of Markov models consisting of an iterative refinement of
the discretization in reduced dimensionality is presented and used to generate
a detailed kinetic network of the system. The hairpin is found to fold
heterogeneously on sub-microsecond timescales, with the relative position of
the tryptophan side chains driving the selection of the specific pathway.


Structure-guided simulations illuminate the mechanism of ATP transport through VDAC1
------------------------------------------------------------------------------------

 * Om P Choudhary; Aviv Paz; Joshua L Adelman; Jacques-Philippe Colletier; Jeff Abramson; Michael Grabe
 * *Nat. Struct. Mol. Biol.* **2014**, 21 626--632
 * `doi: 10.1038/nsmb.2841 <http://dx.doi.org/10.1038/nsmb.2841>`_

The voltage-dependent anion channel (VDAC) mediates the flow of metabolites and
ions across the outer mitochondrial membrane of all eukaryotic cells. The open
channel passes millions of ATP molecules per second, whereas the closed state
exhibits no detectable ATP flux. High-resolution structures of VDAC1 revealed a
19-stranded β-barrel with an α-helix partially occupying the central pore. To
understand ATP permeation through VDAC, we solved the crystal structure of
mouse VDAC1 (mVDAC1) in the presence of ATP, revealing a low-affinity binding
site. Guided by these coordinates, we initiated hundreds of molecular dynamics
simulations to construct a Markov state model of ATP permeation. These
simulations indicate that ATP flows through VDAC through multiple pathways, in
agreement with our structural data and experimentally determined physiological
rates.


Native States of Fast-Folding Proteins Are Kinetic Traps
--------------------------------------------------------------------------------

 * Dickson, Alex; Brooks, Charles L.
 * *J. Am. Chem. Soc.* **2013**, 135 4729--4734
 * `doi: 10.1021/ja311077u <http://dx.doi.org/10.1021/ja311077u>`_

It has been suggested that the native state of a protein acts as a kinetic hub
that can facilitate transitions between nonnative states. Using recently
developed tools to quantify mediation probabilities (“hub scores”), we quantify
hub-like behavior in atomic resolution trajectories for the first time. We use
a data set of trajectory ensembles for 12 fast-folding proteins previously
published by D. E. Shaw Research (Lindorff-Larsen, K.; et al. How Fast-Folding
Proteins Fold. Science2011, 334, 517) with an aggregate simulation time of over
8.2 ms. We visualize the free-energy landscape of each molecule using
configuration space networks, and show that dynamic quantities can be
qualitatively understood from visual inspection of the networks. Modularity
optimization is used to provide a parameter-free means of tessellating the
network into a group of communities. Using hub scores, we find that the
percentage of trajectories that are mediated by the native state is 31% when
averaged over all molecules, and reaches a maximum of 52% for the homeodomain
and chignolin. Furthermore, for these mediated transitions, we use Markov
models to determine whether the native state acts as a facilitator for the
transition, or as a trap (i.e., an off-pathway detour). Although instances of
facilitation are found in 4 of the 12 molecules, we conclude that the native
state acts primarily as a trap, which is consistent with the idea of a funnel-
like landscape.


Hierarchical Nyström methods for constructing Markov state models for conformational dynamics
----------------------------------------------------------------------------------------------

 * Yao, Yuan; Cui, Raymond Z.; Bowman, Gregory R.; Silva, Daniel-Adriano; Sun, Jian; Huang, Xuhui
 * *J. Chem. Phys.* **2013**, 138 
 * `doi: 10.1063/1.4802007 <http://dx.doi.org/10.1063/1.4802007>`_

Markov state models (MSMs) have become a popular approach for investigating the
conformational dynamics of proteins and other biomolecules. MSMs are typically
built from numerous molecular dynamics simulations by dividing the sampled
configurations into a large number of microstates based on geometric criteria.
The resulting microstate model can then be coarse-grained into a more
understandable macrostate model by lumping together rapidly mixing microstates
into larger, metastable aggregates. However, finite sampling often results in
the creation of many poorly sampled microstates. During coarse-graining, these
states are mistakenly identified as being kinetically important because
transitions to/from them appear to be slow. In this paper, we propose a
formalism based on an algebraic principle for matrix approximation, i.e., the
Nyström method, to deal with such poorly sampled microstates. Our scheme builds
a hierarchy of microstates from high to low populations and progressively
applies spectral clustering on sets of microstates within each level of the
hierarchy. It helps spectral clustering identify metastable aggregates with
highly populated microstates rather than being distracted by lowly populated
states. We demonstrate the ability of this algorithm to discover the major
metastable states on two model systems, the alanine dipeptide and trpzip2
peptide.


Quantitative comparison of alternative methods for coarse-graining biological networks
----------------------------------------------------------------------------------------

 * Bowman, Gregory R.; Meng, Luming; Huang, Xuhui
 * *J. Chem. Phys.* **2013**, 139 
 * `doi: 10.1063/1.4812768 <http://dx.doi.org/10.1063/1.4812768>`_

Markov models and master equations are a powerful means of modeling dynamic
processes like protein conformational changes. However, these models are often
difficult to understand because of the enormous number of components and
connections between them. Therefore, a variety of methods have been developed
to facilitate understanding by coarse-graining these complex models. Here, we
employ Bayesian model comparison to determine which of these coarse-graining
methods provides the models that are most faithful to the original set of
states. We find that the Bayesian agglomerative clustering engine and the
hierarchical Nyström expansion graph (HNEG) typically provide the best
performance. Surprisingly, the original Perron cluster cluster analysis (PCCA)
method often provides the next best results, outperforming the newer PCCA+
method and the most probable paths algorithm. We also show that the differences
between the models are qualitatively significant, rather than being minor
shifts in the boundaries between states. The performance of the methods
correlates well with the entropy of the resulting coarse-grainings, suggesting
that finding states with more similar populations (i.e., avoiding low
population states that may just be noise) gives better results.


Learning Kinetic Distance Metrics for Markov State Models of Protein Conformational Dynamics
------------------------------------------------------------------------------------------------

 * McGibbon, Robert T.; Pande, Vijay S.
 * *J. Chem. Theory Comput.* **2013**, 9 2900--2906
 * `doi: 10.1021/ct400132h <http://dx.doi.org/10.1021/ct400132h>`_

Statistical modeling of long timescale dynamics with Markov state models (MSMs)
has been shown to be an effective strategy for building quantitative and
qualitative insight into protein folding processes. Existing methodologies,
however, rely on geometric clustering using distance metrics such as root mean
square deviation (RMSD), assuming that geometric similarity provides an
adequate basis for the kinetic partitioning of phase space. Here, inspired by
advances in the machine learning community, we introduce a new approach for
learning a distance metric explicitly constructed to model kinetic similarity.
This approach enables the construction of models, especially in the regime of
high anisotropy in the diffusion constant, with fewer states than was
previously possible. Application of this technique to the analysis of two
ultralong molecular dynamics simulations of the FiP35 WW domain identifies
discrete near-native relaxation dynamics in the millisecond regime that were
not resolved in previous analyses.


Persistent Topology and Metastable State in Conformational Dynamics
--------------------------------------------------------------------------------

 * Chang, Huang-Wei; Bacallado, Sergio; Pande, Vijay S.; Carlsson, Gunnar E.
 * *PLoS ONE* **2013**, 8 e58699
 * `doi: 10.1371/journal.pone.0058699 <http://dx.doi.org/10.1371/journal.pone.0058699>`_

The large amount of molecular dynamics simulation data produced by modern
computational models brings big opportunities and challenges to researchers.
Clustering algorithms play an important role in understanding biomolecular
kinetics from the simulation data, especially under the Markov state model
framework. However, the ruggedness of the free energy landscape in a
biomolecular system makes common clustering algorithms very sensitive to
perturbations of the data. Here, we introduce a data-exploratory tool which
provides an overview of the clustering structure under different parameters.
The proposed Multi-Persistent Clustering analysis combines insights from recent
studies on the dynamics of systems with dominant metastable states with the
concept of multi-dimensional persistence in computational topology. We propose
to explore the clustering structure of the data based on its persistence on
scale and density. The analysis provides a systematic way to discover clusters
that are robust to perturbations of the data. The dominant states of the system
can be chosen with confidence. For the clusters on the borderline, the user can
choose to do more simulation or make a decision based on their structural
characteristics. Furthermore, our multi-resolution analysis gives users
information about the relative potential of the clusters and their hierarchical
relationship. The effectiveness of the proposed method is illustrated in three
biomolecules: alanine dipeptide, Villin headpiece, and the FiP35 WW domain.


Atomistic Simulations of Wimley–White Pentapeptides: Sampling of Structure and Dynamics in Solution
------------------------------------------------------------------------------------------------------------

 * Singh, Gurpreet; Tieleman, D. Peter
 * *J. Chem. Theory Comput.* **2013**, 9 1657--1666
 * `doi: 10.1021/ct3008217 <http://dx.doi.org/10.1021/ct3008217>`_

Wimley–White pentapeptides (Ac-WLXLL) can be used as a model system to study
lipid–protein interactions as they bind to lipid/water interfaces, like many
antimicrobial peptides, and thermodynamic experimental data on their
interactions with lipids are available, making them useful for both force field
and method testing and development. Here we present a detailed simulation study
of Wimley–White (WW) peptides in bulk water to investigate sampling,
conformations, and differences due to the different X residue with an eye to
future simulations at the lipid/water interface where sampling problems so far
have hindered free energy calculations to reproduce the experimental
thermodynamic data. We investigate the conformational preferences and slowest
relaxation time of WW peptides in bulk water by building Markov State Models
(MSM) from Molecular Dynamics (MD) simulation data. We show that clustering
based on binning of backbone $\phi$, $\psi$ dihedrals in combination with the
community detection algorithm of Blondel et al. provides a quick way of
building MSM from large data sets. Our results show that in some cases, implied
times even in these small peptides range from 224 to 547 ns. The implications
of these slow transitions on determining the potential of mean force profiles
of peptide interactions with a lipid bilayer are discussed.


Simple few-state models reveal hidden complexity in protein folding
--------------------------------------------------------------------------------

 * Beauchamp, Kyle A.; McGibbon, Robert; Lin, Yu-Shan; Pande, Vijay S.
 * *Proc. Natl. Acad. Sci. U.S.A.* **2012**, 109 17807--17813
 * `doi: 10.1073/pnas.1201810109 <http://dx.doi.org/10.1073/pnas.1201810109>`_

Markov state models constructed from molecular dynamics simulations have
recently shown success at modeling protein folding kinetics. Here we introduce
two methods, flux PCCA+ (FPCCA+) and sliding constraint rate estimation (SCRE),
that allow accurate rate models from protein folding simulations. We apply
these techniques to fourteen massive simulation datasets generated by Anton and
Folding@home. Our protocol quantitatively identifies the suitability of
describing each system using two-state kinetics and predicts experimentally
detectable deviations from two-state behavior. An analysis of the villin
headpiece and FiP35 WW domain detects multiple native substates that are
consistent with experimental data. Applying the same protocol to GTT, NTL9, and
protein G suggests that some beta containing proteins can form long-lived
native-like states with small register shifts. Even the simplest protein
systems show folding and functional dynamics involving three or more states.


Investigating How Peptide Length and a Pathogenic Mutation Modify the Structural Ensemble of Amyloid Beta Monomer 
-------------------------------------------------------------------------------------------------------------------------

 * Yu-Shan Lin; Gregory R. Bowman; Kyle A. Beauchamp; Vijay S. Pande
 * *Biophys. J.* **2012**, 102 315--324
 * `doi: 10.1016/j.bpj.2011.12.002 <http://dx.doi.org/10.1016/j.bpj.2011.12.002>`_

The aggregation of amyloid beta (Aβ) peptides plays an important role in the
development of Alzheimer's disease. Despite extensive effort, it has been
difficult to characterize the secondary and tertiary structure of the Aβ
monomer, the starting point for aggregation, due to its hydrophobicity and high
aggregation propensity. Here, we employ extensive molecular dynamics
simulations with atomistic protein and water models to determine structural
ensembles for Aβ42, Aβ40, and Aβ42-E22K (the Italian mutant) monomers in
solution. Sampling of a total of >700 microseconds in all-atom detail with
explicit solvent enables us to observe the effects of peptide length and a
pathogenic mutation on the disordered Aβ monomer structural ensemble. Aβ42 and
Aβ40 have crudely similar characteristics but reducing the peptide length from
42 to 40 residues reduces β-hairpin formation near the C-terminus. The
pathogenic Italian E22K mutation induces helix formation in the region of
residues 20–24. This structural alteration may increase helix-helix
interactions between monomers, resulting in altered mechanism and kinetics of
Aβ oligomerization.


Equilibrium fluctuations of a single folded protein reveal a multitude of potential cryptic allosteric sites
------------------------------------------------------------------------------------------------------------------

 * Bowman, Gregory R.; Geissler, Phillip L.
 * *Proc. Natl. Acad. Sci. U.S.A.* **2012**, 109 11681--11686
 * `doi: 10.1073/pnas.1209309109 <http://dx.doi.org/10.1073/pnas.1209309109>`_

Cryptic allosteric sites—transient pockets in a folded protein that are
invisible to conventional experiments but can alter enzymatic activity via
allosteric communication with the active site—are a promising opportunity for
facilitating drug design by greatly expanding the repertoire of available drug
targets. Unfortunately, identifying these sites is difficult, typically
requiring resource-intensive screening of large libraries of small molecules.
Here, we demonstrate that Markov state models built from extensive computer
simulations (totaling hundreds of microseconds of dynamics) can identify
prospective cryptic sites from the equilibrium fluctuations of three medically
relevant proteins—β-lactamase, interleukin-2, and RNase H—even in the absence
of any ligand. As in previous studies, our methods reveal a surprising variety
of conformations—including bound-like configurations—that implies a role for
conformational selection in ligand binding. Moreover, our analyses lead to a
number of unique insights. First, direct comparison of simulations with and
without the ligand reveals that there is still an important role for an induced
fit during ligand binding to cryptic sites and suggests new conformations for
docking. Second, correlations between amino acid sidechains can convey
allosteric signals even in the absence of substantial backbone motions. Most
importantly, our extensive sampling reveals a multitude of potential cryptic
sites—consisting of transient pockets coupled to the active site—even in a
single protein. Based on these observations, we propose that cryptic allosteric
sites may be even more ubiquitous than previously thought and that our methods
should be a valuable means of guiding the search for such sites.


Improved coarse-graining of Markov state models via explicit consideration of statistical uncertainty
------------------------------------------------------------------------------------------------------

 * Bowman, Gregory R.
 * *J. Chem. Phys.* **2012**, 137 
 * `doi: 10.1063/1.4755751 <http://dx.doi.org/10.1063/1.4755751>`_

Markov state models (MSMs)–or discrete-time master equation models–are a
powerful way of modeling the structure and function of molecular systems like
proteins. Unfortunately, MSMs with sufficiently many states to make a
quantitative connection with experiments (often tens of thousands of states
even for small systems) are generally too complicated to understand. Here, I
present a Bayesian agglomerative clustering engine (BACE) for coarse-graining
such Markovmodels, thereby reducing their complexity and making them more
comprehensible. An important feature of this algorithm is its ability to
explicitly account for statistical uncertainty in model parameters that arises
from finite sampling. This advance builds on a number of recent works
highlighting the importance of accounting for uncertainty in the analysis of
MSMs and provides significant advantages over existing methods for coarse-
graining Markov state models. The closed-form expression I derive here for
determining which states to merge is equivalent to the generalized Jensen-
Shannon divergence, an important measure from information theory that is
related to the relative entropy. Therefore, the method has an appealing
information theoretic interpretation in terms of minimizing information loss.
The bottom-up nature of the algorithm likely makes it particularly well suited
for constructing mesoscale models. I also present an extremely efficient
expression for Bayesian model comparison that can be used to identify the most
meaningful levels of the hierarchy of models from BACE.


Quantifying Hub-like Behavior in Protein Folding Networks
--------------------------------------------------------------------------------

 * Dickson, Alex; Brooks, Charles L.
 * *J. Chem. Theory Comput.* **2012**, 8 3044--3052
 * `doi: 10.1021/ct300537s <http://dx.doi.org/10.1021/ct300537s>`_

The free energy landscape of a protein is a function of many interdependent
degrees of freedom. For this reason, conceptual constructs (e.g., funnels) have
been useful to visualize these landscapes. One relatively new construct is the
idea of a hub-like native state that is the final destination of many
noninterconverting folding pathways. This is in contrast to the idea of a
single predominant folding pathway connecting the native state to a rapidly
interconverting ensemble of unfolded states. The key quantity to distinguish
between these two ideas is the connectivity of the unfolded ensemble. We
present a metric to determine this connectivity for a given network, which can
be calculated either from continuous folding trajectories, or a Markov model.
The metric determines how often a region of space is used as an intermediate on
transition paths that connect two other regions of space, and we use it here to
determine how often two parts of the unfolded ensemble are connected directly
versus how often these transitions are mediated by the native state.


Markov State Model Reveals Folding and Functional Dynamics in Ultra-Long MD Trajectories
-----------------------------------------------------------------------------------------

 * Lane, Thomas J.; Bowman, Gregory R.; Beauchamp, Kyle; Voelz, Vincent A.; Pande, Vijay S.
 * *J. Am. Chem. Soc.* **2011**, 133 18413--18419
 * `doi: 10.1021/ja207470h <http://dx.doi.org/10.1021/ja207470h>`_

Two strategies have been recently employed to push molecular simulation to
long, biologically relevant time scales: projection-based analysis of results
from specialized hardware producing a small number of ultralong trajectories
and the statistical interpretation of massive parallel sampling performed with
Markov state models (MSMs). Here, we assess the MSM as an analysis method by
constructing a Markov model from ultralong trajectories, specifically two
previously reported 100 $\mu$s trajectories of the FiP35 WW domain ( Shaw, D.
E. Science 2010, 330, 341-346 ). We find that the MSM approach yields novel
insights. It discovers new statistically significant folding pathways, in which
either beta-hairpin of the WW domain can form first. The rates of this process
approach experimental values in a direct quantitative comparison (time scales
of 5.0 $\mu$ s and 100 ns), within a factor of $\sim$2. Finally, the hub-like
topology of the MSM and identification of a holo conformation predicts how WW
domains may function through a conformational selection mechanism.


