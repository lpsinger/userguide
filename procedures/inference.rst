Inference
=========

For :term:`CBC` events, we calculate a number of quantities that are inferred
from the signal. In preliminary alerts, these quantities are based on the
candidate significance and the matched-filter estimates of the source
parameters. Once parameter estimation has been completed, updated values will
be provided based on samples drawn from the posterior probability distribution.

Classification
--------------

The classification consists of four numbers, summing to unity, that give the
probability that the source is a :term:`BNS`, :term:`NSBH`, :term:`BBH` merger,
or terrestrial (i.e. a background fluctuation or a glitch).

This assumes that terrestrial and astrophysical events occur as independent
Poisson processes. A source-dependent weighting of matched-filter templates is
used to compute the mean values of expected counts associated with each of
these four categories. The mean values are updated weekly based on observed
matched-filter count rates. They are then used to predict the category for new
triggers uploaded by :doc:`search pipelines </procedures/searches>`.

Properties
----------

The source properties consist of a set of numbers, each between zero and unity,
that give the probabilities that the source satisfies certain conditions. These
conditions are:

**HasNS**: At least one of the compact objects in the binary (that is, the less
massive or *secondary* compact object) has a mass that is consistent with a
neutron star. Specifically, we define this as the probability that the
secondary mass satisfies :math:`m_2 \leq 3 M_{\odot}`.

**HasRemnant**: The probability that the source ejected a nonzero mass outside
the final remnant compact object. This is calculated using the disk mass
fitting formula from [#DiskMass]_ (Equation 4).

For preliminary estimates based on the matched-filter pipeline results, the
source properties are calculated using a supervised learning technique;
mass-dependent rates are the same as those used for the classification. For
parameter estimation, updated properties are calculated from posterior samples.

.. |prd| replace:: *Phys. Rev. D*

.. [#DiskMass]
   Foucart, F., Hinderer, T. & Nissanke, S. 2018, |prd|, 98, 081501.
   https://doi.org/10.1103/PhysRevD.98.081501
