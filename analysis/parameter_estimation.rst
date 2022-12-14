Sky Localization and Parameter Estimation
=========================================

Immediately after one of the :doc:`search pipelines <searches>` reports an
event, sky localization and parameter estimation analyses begin. These analyses
all use Bayesian inference to calculate the posterior probability distribution
over the parameters (sky location, distance, and/or intrinsic properties of the
source) given the observed gravitational-wave signal.

There are different parameter estimation methods for modeled (CBC) and
unmodeled (:term:`burst`) events. However, in both cases there is a rapid
analysis that estimates only the sky localization, and is ready in seconds, and
a refined analysis that explores a larger parameter space and completes up to
hours or a day later.

Modeled Events
--------------

**BAYESTAR** [#BAYESTAR]_ is the rapid CBC sky localization algorithm. It reads
in the matched-filter time series from the :doc:`search pipeline <searches>`
and calculates the posterior probability distribution over the sky location and
distance of the source by coherently modeling the response of the
gravitational-wave detector network. It explores the parameter space using
Gaussian quadrature, lookup tables, and sampling on an adaptively refined
:term:`HEALPix` grid. The sky localization takes tens of seconds and is
included in the preliminary alert.

**Bilby** [#Bilby]_ is a full CBC parameter estimation pipeline.
It explores a greatly expanded parameter space including sky location,
distance, masses, and spins, and performs full forward modeling of the
gravitational-wave signal and the strain calibration of the gravitational-wave
detectors. It explores the parameter space using :term:`MCMC` and nested
sampling. For all events, there is an automated Bilby analysis that uses
the least expensive CBC waveform models and completes within hours and may be
included in a subsequent alert. More time-consuming analyses with more
sophisticated waveform models are started at the discretion of human analysts,
and will complete days or weeks later.

Unmodeled Events
----------------

**cWB**, the burst :doc:`search pipeline <searches>`, also performs a rapid sky
localization based on its coherent reconstruction of the gravitational-wave
signal using a wavelet basis and the response of the gravitational-wave
detector network [#cWBLocalization]_. The cWB sky localization is included in
the preliminary alert.

Refined sky localizations for unmodeled bursts are provided by two algorithms
that :term:`MCMC` and nested sampling methodologies, like Bilby.
**LALInference Burst (LIB)** [#oLIB]_ models the signal as a single
sinusoidally modulated Gaussian. **BayesWave** [#BayesWave]_ models the signal
as a superposition of wavelets and jointly models the background with both a
stationary noise component and glitches composed of wavelets that are present
in individual detectors.

.. include:: /journals.rst

.. [#BAYESTAR]
   Singer, L. P., & Price, L. R. 2016, |PRD|, 93, 024013.
   :doi:`10.1103/PhysRevD.93.024013`

.. [#Bilby]
   Ashton, G., Hübner, M., Lasky, P. D., Talbot, C., et al. 2019, |ApJS|, 241, 27.
   :doi:`10.3847/1538-4365/ab06fc`

.. [#cWBLocalization]
   Klimenko, S., Vedovato, G., Drago, M., et al. 2011, |PRD|, 83, 102001.
   :doi:`10.1103/PhysRevD.83.102001`

.. [#oLIB]
   Lynch, R., Vitale, S., Essick, R., Katsavounidis, E., & Robinet, F. 2017, |PRD|, 95, 104046.
   :doi:`10.1103/PhysRevD.95.104046`

.. [#BayesWave]
   Cornish, N. J., & Littenberg, T. B. 2015, |CQG|, 32, 135012.
   :doi:`10.1088/0264-9381/32/13/135012`
