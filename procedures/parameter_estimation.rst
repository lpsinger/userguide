Localization and Parameter Estimation
=====================================

Immediately after one of the :doc:`search pipelines <searches>` reports an
event, localization and parameter estimation analyses begin. These analyses all
use Bayesian inference to calculate the posterior probability distribution over
the parameters (sky location, distance, and/or intrinsic properties of the
source) given the observed gravitational-wave signal.

There are different parameter estimation methods for modeled (CBC) and
unmodeled (Burst) events. However, in both cases there is a rapid analysis that
estimates only the localization, and is ready in seconds, and a refined
analysis that explores a larger parameter space and completes up to hours or a
day later.

Modeled Events
--------------

**BAYESTAR** [#BAYESTAR]_ is the rapid CBC localization algorithm. It reads in
the matched-filter time series from the :doc:`search pipeline <searches>` and
calculates the posterior probability distribution over the sky location and
distance of the source by coherently modeling the response of the
gravitational-wave detector network. It explores the parameter space using
Gaussian quadrature, lookup tables, and sampling on an adaptively refined
HEALPix grid. The localization takes tens of seconds and is included in the
preliminary alert.

**LALInference** [#LALInference]_ is the full CBC parameter estimation
algorithm. It explores a greatly expanded parameter space including sky
location, distance, masses, and spins, and performs full forward modeling of
the gravitational-wave signal and the strain calibration of the
gravitational-wave detectors. It explores the parameter space using Markov
chain Monte Carlo and nested sampling. For all events, there is an automated
LALInference analysis that uses the least expensive CBC waveform models and
completes within hours and may be included in a subsequent alert. More
time-consuming analyses with more sophisticated waveform models are started at
the discretion of human analysts, and complete days or weeks later.

Unmodeled Events
----------------

**cWB**, the burst :doc:`search pipeline <searches>`, also performs a rapid
localization based on its coherent reconstruction of the gravitational-wave
signal using a wavelet basis and the response of the gravitational-wave
detector network [#cWBLocalization]_. The cWB localization is included in the
preliminary alert.

Refined localizations for unmodeled bursts are provided by two algorithms that
use the same MCMC and nested sampling methodology as LALInference.
**LALInference Burst (LIB)** [#oLIB]_ models the signal as a single
sinusoidally modulated Gaussian. **BayesWave** [#BayesWave]_ models the signal
as a superposition of wavelets and jointly models the background with both a
stationary noise component and glitches composed of wavelets that are present
in individual detectors.

.. |cqg| replace:: *Class. Quantum Grav.*
.. |prd| replace:: *Phys. Rev. D*

.. [#BAYESTAR]
   Singer, L. P., & Price, L. R. 2016, |prd|, 93, 024013.
   https://doi.org/10.1103/PhysRevD.93.024013

.. [#LALInference]
   Veitch, J., Raymond, V., Farr, B., et al. 2015, |prd|, 91, 042003.
   https://doi.org/10.1103/PhysRevD.91.042003

.. [#cWBLocalization]
   Klimenko, S., Vedovato, G., Drago, M., et al. 2011, |prd|, 83, 102001.
   https://doi.org/10.1103/PhysRevD.83.102001

.. [#oLIB]
   Lynch, R., Vitale, S., Essick, R., Katsavounidis, E., & Robinet, F. 2017, |prd|, 95, 104046.
   https://doi.org/10.1103/PhysRevD.95.104046

.. [#BayesWave]
   Cornish, N. J., & Littenberg, T. B. 2015, |cqg|, 32, 135012.
   https://doi.org/10.1088/0264-9381/32/13/135012
