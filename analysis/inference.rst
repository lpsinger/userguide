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
background fluctuation or a glitch) origin.

Our :doc:`search pipelines </analysis/searches>` use independent methods to
assign those source probabilities to their own triggers. These methods all
start from the common assumptions that terrestrial and astrophysical events
occur as independent Poisson processes, and that NSs and BHs only exist below
and above :math:`3 M_{\odot}` respectively (see the :ref:`figure in the alert
contents section <classification-diagram>` for the boundaries of the source
classification categories in the :math:`(m_1,m_2)` plane). The search pipelines
then account for the rates of background and astrophysical events in ways that
differ in detail, but are all based on the population of events observed during
the O1, O2 and O3 runs.

For details of the GstLAL method, see [#Pastro]_ (especially Equation 20).
For MBTA, see [#SrcClassMBTA]_. For PyCBC Live, see [#SrcClassPyCBCLive]_.
For SPIIR, see [#CountingAndConfusion]_ and [#SrcClassPyCBCLive]_.

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

The performance of these quantities across online :term:`CBC` pipelines is shown below.

.. tabs::

   .. tab:: HasNS
      .. figure:: ../_static/hasNS.*
         :alt: :term:`ROC` curve for HasNS
         :align: center

         The :term:`ROC` curve showing the performance of **HasNS**.

   .. tab:: HasRemnant
      .. figure:: ../_static/hasRemnant.*
         :alt: :term:`ROC` curve for HasRemnant
         :align: center
         
         The :term:`ROC` curve showing the performance of **HasRemnant**.

   .. tab:: HasMassGap
      .. figure:: ../_static/hasMassGap.*
         :alt: :term:`ROC` curve for HasMassGap
         :align: center
         
         The :term:`ROC` curve showing the performance of **HasMassGap**.

The :term:`ROC` curves shown above were constructed using pipeline recovered injections from the O3 Mock Data Challenge (MDC). 
For details see [#MDC]_.

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

.. [#SrcClassMBTA]
   Andres, N., Assiduo, M., Aubin, F., et al., 2022, |CQG|, 39, 055002.
   :doi:`10.1088/1361-6382/ac482a`

.. [#SrcClassPyCBCLive]
   Villa-Ortega, V., Dent, T., Curiel Barroso, A., 2022.
   :arxiv:`2203.10080`

.. [#CountingAndConfusion]
   Farr, W. M., Gair, J. R., Mandel, I., et al, 2015, |PRD|, 91, 023005.
   :doi:`10.1103/PhysRevD.91.023005`

.. [#ModelSelection]
   Ghosh, S., Liu, X., Creighton, J., et. al., 2021, |PRD|, 104, 083003.
   :doi:`10.1103/PhysRevD.104.083003`

.. [#DiskMass]
   Foucart, F., Hinderer, T. & Nissanke, S. 2018, |PRD|, 98, 081501.
   :doi:`10.1103/PhysRevD.98.081501`

.. [#MLEMBright]
   Chatterjee, D., Ghosh, S., Brady, P. R., et al. 2020, |ApJ|, 896, 54.
   :doi:`10.3847/1538-4357/ab8dbe`

.. [#MDC]
   Sharma Chaudhary, S., Toivonen, A., et al. 2023,
   :arxiv:`2308.04545` 
