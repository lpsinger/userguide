Online pipelines and alert distribution 	
=======================================

.. toctree::
   :maxdepth: 1
   :caption: Contents:


Should mention:

  * References to O2 paper for the online and few lines about the pipelines + joint searchs (RAVEN)
  * Threshold for public alerts (purity for CBC, equivalent for Burst)

Pipelines
=========

During the third LIGO observation run a number of search pipelines will be running in a low latency, online mode. These can be divided into two groups, modeled and unmodeled. The modeled (CBC) searches specifically look for signals from compact binary mergers of neutron stars and black holes (BNS, NS-BH, and BBH systems). The unmodeled (Burst) searches on the other hand, are capable of detecting signals from a wide variety of astrophysical sources in addition to compact binary mergers: core-collapse of massive stars, magnetar starquakes, and more speculative sources such as intersecting cosmic strings or as-yet unknown GW sources.

* Modeled (CBC): GstLAL, MBTAOnline (MultiBand Template Analysis) and PyCBC Live are matched-filtering based analysis pipelines that rapidly identify compact binary merger events, with sub-minute to ∼1 minute latencies. They use discrete banks of waveform templates to cover the target parameter space of compact binaries, with all pipelines covering the mass ranges corresponding to BNS, NS-BH, and stellar mass BBH systems. However, GstLAL and PyCBC Live also include intermediatemass BBH systems and the O2 banks differ in detail from pipeline to pipeline.
        A coincident analysis is performed by each pipeline, where candidate events are extracted separately at each detector via matched-filtering and later combined across
detectors. Of the three pipelines, GstLAL and MBTAOnline use several matched filters to cover the detector bandwidth, i.e., the matched filter is split across multiple frequency bands. All pipelines also implement different kinds of signal-based vetoes to reject instrumental transients which cause large SNR values but can otherwise be easily distinguished from compact binary coalescence signals.

 * Gstlal-inspiral: The gstlal-based inspiral pipeline is a matched-filter pipeline designed to find gravitational-waves from compact binaries in low-latency. It uses the likelihood-ratio, which increases monotonically with signal probability, to rank candidates, and then uses Monte Carlo sampling methods to estimate the distribution of likelihood-ratios in noise. This distribution can then be used to compute a false alarm rate and p-value. [1] [2] [3]
 * Gstlal-spiir: 
 * MBTA (MultiBand Template Analysis): MBTAOnline constructs its background by making every possible coincidence from single detector triggers over few hours of recent data. It then folds in the probability of a pair of triggers passing the time coincidence test. 
 * Pycbc: PyCBC Live estimates the background of accidental coincidences through the process of time slides between single-detector triggers. Triggers are time shifted by every possible multiple of 100 ms that is greater than the ∼10 ms of light travel time between the two LIGO detectors. All coincidences are recorded and assigned a ranking statistic in the same way a candidate event would be.

* Unmodeled (Burst)

 * cWB: cWB is a power excess algorithm focused to identify gravitational-like signals with short time duration. It uses a wavelet transformation to identify time-frequency pixels which can be grouped in a single cluster if they satisfy neighbouring conditions. A tuned version for compact-binary coalescences chooses the time-frequency pixels if they mainly follow a frequency increasing pattern. A maximum-likelihood-statistics calculated over the cluster is used to identify the proper parameter of the event, in particular the probability of the source direction and the coherent network signal-to-noise ratio. The last one is used to assign detection significance to the found events.
 * oLIB: oLIB uses Q transform to decompose GW strain data into several time-frequency planes of constant quality factors Q, where Q ∼ τf0. The pipeline flags data segments containing excess power and searches for clusters of these segments with identical f0 and Q spaced within 100 ms of each other. Coincidences among the detector network of clusters with a time-of-flight window up to 10 ms are then analyzed with a coherent (i.e., correlated across the detector network) signal model to identify possible GW candidate events.

Gstlal:
[1] Messick, C., Blackburn, K., Brady, P., et al. 2017, Phys. Rev. D, 95, 042001, doi: 10.1103/PhysRevD.95.042001
[2] https://dcc.ligo.org/LIGO-P1700411
[3] https://dcc.ligo.org/LIGO-P1700412

Gstlal-spiir:


MBTA:
Adams, T., Buskulic, D., Germain, V., et al. 2016, Classical and Quantum Gravity, 33, 175012

Pycbc:
Nitz, A. H., Dent, T., Dal Canton, T., Fairhurst, S., & Brown, D. A. 2017, The Astrophysical Journal, 849, 118
Dal Canton, T., & Harry, I. W. 2017. https://arxiv.org/abs/1705.01845

cWB:
S. Klimenko, G. Vedovato, M. Drago, F. Salemi, V. Tiwari, G. A. Prodi, C. Lazzaro, S. Tiwari, F. Da Silva, and G. Mitselmakher. Method for detection and reconstruction of gravitational wave transients with networks of advanced detectors. Phys. Rev. D 93, 042004, 2015.

oLIB:
Lynch, R., Vitale, S., Essick, R., Katsavounidis, E., & Robinet, F. 2017, Phys. Rev. D, 95, 104046, doi: 10.1103/PhysRevD.95.104046

