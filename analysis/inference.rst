Inference
=========

For :term:`CBC` events, we calculate a number of quantities that are inferred
from the signal. In preliminary alerts, these quantities are based on the
candidate significance and the matched-filter estimates of the source
parameters. Once parameter estimation has been completed, updated values will
be provided based on samples drawn from the posterior probability distribution.

Classification
--------------

The classification consists of four numbers, summing to unity, that
give the probability that the source is either a :term:`BNS`,
:term:`NSBH`, :term:`BBH` merger, or is of :term:`Terrestrial` (i.e. a
background fluctuation or a glitch) origin. See the :ref:`figure in
the alert contents section <classification-diagram>` for the
boundaries of the source classification categories in
the :math:`(m_1,m_2)` plane. The boundary between NSs and BHs
is set to :math:`3 M_{\odot}`.

This assumes that terrestrial and astrophysical events occur as independent
Poisson processes. A source-dependent weighting of matched-filter templates is
used to compute the mean values of expected counts associated with each of
these four categories. The mean values are updated weekly based on observed
matched-filter count rates. They are then used to predict the category for new
triggers uploaded by :doc:`search pipelines </analysis/searches>`.

For details, see [#Pastro]_, especially Section II E. and Equation 18 therein.

Properties
----------

The source properties consist of a set of numbers, each between zero and unity,
that give the probabilities that the source satisfies certain conditions. These
conditions are:

**HasNS**: At least one of the compact objects in the binary (that is, the less
massive or *secondary* compact object) has a mass that is consistent with a
neutron star. Specifically, we define this as the probability that the
secondary mass satisfies :math:`m_2 \leq M_{\mathrm{max}}`, where
:math:`M_{\mathrm{max}}` is the maximum mass allowed by the neutron star equation of
state (:term:`EOS`). Several NS EOSs are considered and the value is marginalized by
weighting using the Bayes factors reported in [#ModelSelection]_.

**HasRemnant**: The source formed a nonzero mass outside the final remnant
compact object. Specifically, the probability is calculated using the disk mass
fitting formula from [#DiskMass]_ (Equation 4). Several neutron star EOSs
are considered to compute the remnant mass. The value is marginalized by weighting
based on Bayes factors in reference mentioned above.

**HasMassGap**: At least one of the compact objects in the binary has a mass in
the hypothetical “mass gap” between neutron stars and black holes, defined here
as :math:`3 M_{\odot} \leq m \leq 5 M_{\odot}`.

The mass values mentioned in this section are :term:`source-frame mass`. The value reported in
the :ref:`preliminary <preliminary>` alert is calculated using a supervised machine learning
classifier on a feature space consisting of the masses, spins, and :term:`SNR` of the best-matching
template, described in [#MLEMBright]_. This is to account for the uncertainty in the reported template
parameters compared to the true parameters. The value reported in the :ref:`update <update>` alerts
uses the :doc:`online parameter estimation <parameter_estimation>` to compute the value.


.. include:: /journals.rst

.. [#Pastro]
   Kapadia, S. J., Caudill, S., Creighton, J. D. E., et al., 2020, |CQG|, 37, 045007.
   :doi:`10.1088/1361-6382/ab5f2d`

.. [#ModelSelection]
   Ghosh, S., Liu, X., Creighton, J., et. al., 2021, |PRD|, 104, 083003.
   :doi:`10.1103/PhysRevD.104.083003`
.. [#DiskMass]
   Foucart, F., Hinderer, T. & Nissanke, S. 2018, |PRD|, 98, 081501.
   :doi:`10.1103/PhysRevD.98.081501`

.. [#MLEMBright]
   Chatterjee, D., Ghosh, S., Brady, P. R., et al. 2020, |ApJ|, 896, 54.
   :doi:`10.3847/1538-4357/ab8dbe`
