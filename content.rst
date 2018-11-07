Alert Contents
==============

Public LIGO/Virgo alerts are distributing using NASA's Gamma-ray Coordinates
Network (:term:`GCN`). There are two types of alerts:

**GCN Circulars** are short human-readable astronomical bulletins. They are written
in a certain well-established `format and style`_. You can `subscribe to GCN
Circulars`_ to receive and post them by email, or you can view them in the
public `GCN Circulars archive`_.

**GCN Notices** are machine-readable packets. They are available as :term:`VOEvent`
XML and `several other formats`_. We strongly recommend receiving LIGO/Virgo
alerts in the VOEvent XML format.

.. _`format and style`: https://gcn.gsfc.nasa.gov/gcn3_circulars.html
.. _`subscribe to GCN Circulars`: https://gcn.gsfc.nasa.gov/gcn_circ_signup.html
.. _`GCN Circulars archive`: https://gcn.gsfc.nasa.gov/gcn3_archive.html
.. _`examples from GW170817`: https://gcn.gsfc.nasa.gov/other/G298048.gcn3
.. _`several other formats`: https://gcn.gsfc.nasa.gov/gcn_describe.html#tc7

GCN Notice Types
----------------

For each event, there are up to four kinds of GCN Notices:

A **Preliminary GCN Notice** is issued automatically within minutes after a
gravitational-wave candidate is detected. The candidate must have passed some
automated data quality checks, but it may later be :ref:`retracted
<retraction>` after human vetting. There is no accompanying GCN Circular at
this stage.

An **Initial GCN Notice** is issued within 4 hours of the preliminary alert,
after vetting by human instrument scientists and data analysts. If the signal
does not pass human vetting (i.e., it is a glitch), then instead of an initial
alert there will be a retraction_. The initial alert is also accompanied by a
GCN Circular which should be considered as the first formal publication of the
candidate and can be cited as such.

An **Update GCN Notice** is issued whenever further analysis leads to improved
estimates of the source localization, significance, or classification. There
may be multiple updates for a given event, and updates may be issued hours,
days, or even weeks after the event.

.. _retraction:

Lastly, a **Retraction GCN Notice** is issued if the candidate is rejected as a
result of vetting by human instrument scientists and data analysts. A
retraction indicates that the candidate has been withdrawn because it is
probably not astrophysical.

All types of GCN Notices *except for Retraction notices* contain the following
information:

* `event name`_ and GraceDb identifier(s)
* event significance_
* `source classification`_
* `source localization`_

All types of GCN Notices *except for Preliminary notices* are accompanied by
human-readable GCN Circulars, which restates all of the above information as
well as a `data quality assessment`_.

Content Description
-------------------

The table below is a diagrammatic representation of the contents of a
LIGO/Virgo GCN Notice.

+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| **Root**                                                                                                                                  |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| IVORN             | :samp:`ivo://nasa.gsfc.gcn/LVC#[{{T,M}}]S{YYMMDDabc}-{{1,2,3}}-{{Preliminary,Initial,Update,Preliminary-Retraction}}` |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Role              | :samp:`{{observation,test}}`                                                                                          |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| **Who**                                                                                                                                   |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Date              | Time sent (UTC, ISO-8601), e.g. :samp:`2018-11-01T22:34:49`                                                           |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Author            | :samp:`LIGO Scientific Collaboration and Virgo Collaboration`                                                         |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| **WhereWhen**     | Time of signal (UTC, ISO-8601), e.g. :samp:`2018-11-01T22:22:46.654437`                                               |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| **What**                                                                                                                                  |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| GraceID           | GraceDb ID: :samp:`[{{T,M}}]S{YYMMDDabc}`                                                                             |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Packet Type       | GCN Notice type: :samp:`{{Preliminary,Initial,Update}}`                                                               |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Notice Type       | Numerical equivalent of GCN Notice type: :samp:`{{150,151,152}}`                                                      |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| FAR               | Estimated false alarm rate in Hz                                                                                      |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Sky Map           | URL of HEALPix FITS localization file                                                                                 |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Group             | :samp:`CBC`                                               | :samp:`Burst`                                             |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Pipeline          | :samp:`{{Gstlal,MBTA,PyCBC,SPIIR}}`                       | :samp:`{{cWB,oLIB}}`                                      |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| CentralFreq       | N/A                                                       | Central frequency in Hz                                   |
+-------------------+                                                           +-----------------------------------------------------------+
| Duration          |                                                           | Duration of burst in Hz                                   |
+-------------------+                                                           +-----------------------------------------------------------+
| Fluence           |                                                           | Gravitational-wave fluence in erg cm\ :math:`^{-2}`       |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| **Why**           | Inference about the source                                                                                            |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| BNS, NSBH, BBH,   | Probability that the source is a :term:`BNS`,             | N/A                                                       |
| Noise             | :term:`NSBH`, :term:`NSBH` merger, or just noise,         |                                                           |
|                   | respectively (mutually exclusive)                         |                                                           |
+-------------------+-----------------------------------------------------------+                                                           +
| HasNS, HasRemnant | Probability, under the assumption that the source is not  |                                                           |
|                   | noise, that at least one of the compact objects was a     |                                                           |
|                   | neutron star, and that the system ejected a nonzero amount|                                                           |
|                   | of neutron star matter, respectively.                     |                                                           |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+

.. _`event name`:

**Event name**

Events will be labeled based on the trigger time (...).


.. _significance:

**Significance**

The significance of the event will be given in the form of a associated False
Alarm Rate (FAR), that is the expected rate of events with the same
significance due to noise only. If the estimated FAR is less than one in a
hundred years, the event will be simply described as "highly significant".
Otherwise, the FAR number will be stated in the circular.

.. _`source classification`:

**Source classification**

If the event is identified as a Compact Binary Coalescence (CBC), a source
classification is provided. The classification is a qualitative statement
whether the signal is consistent with a Binary of two Neutron Stars (BNS), of a
Black Hole and a Neutron Star (NSBH or BHNS) or of two Black Holes (BBH).
Additional information may be provided, if available:

* the probability that the least massive member of the binary has a mass
  consistent with a Neutron Star (NS);
* the probability that some mass is left outside the remnant (we label this
  probability "Disk-Mass-Probability", since the presence of mass makes the
  possibility of electro-magnetic emission more likely);
* the first two probabilities are clubbed together under the broader name of
  "EM-Bright" probability.
* the probability ("P_astro") that the event is of astrophysical origin based
  on both the noise background properties and the observed CBC rate.

.. _`source localization`:

**Source localization**

The source localization estimate is a posterior probability of the source
projected position in the sky ("2D localization") or of the source position in
space ("3D localization", only available if the source is a CBC). The
probability distribution is encoded using the :term:`HEALPix` projection and
saved in a :term:`FITS` file whose URL is included in the GCN Notice. See
:doc:`sample code for working with LIGO/Virgo source localization maps
</tutorial/skymaps>`.

.. _`data quality assessment`:

**Data quality assessment**

Circulars may contain concise descriptions of any instrument or data quality
issues that may affect the significance estimates or the GW parameter
inferences. Unresolved data quality issues could mean that localization
estimates may shift after they have been mitigated, but does not mean that they
will. This is to be considered as advisory information.

.. _`quantitative intrinsic infomation on the sources that is not vital to this purpose`:

What will *not* be included in alerts
-------------------------------------

The alerts will not contain quantitative estimates of intrinsic properties such
as masses and spins, nor contain information on the GW strain or reconstructed
waveforms. After final analysis, those data products are released through the
`Gravitational Wave Open Science Center <https://www.gw-openscience.org/>`_.

Example Alerts
--------------

Below are some sample VOEvents to illustrate the formatting of the GCN Notices.

.. tabs::

   .. tab:: Preliminary

      .. literalinclude:: _static/MS181101abc-1-Preliminary.xml
         :language: xml

   .. tab:: Initial

      .. literalinclude:: _static/MS181101abc-2-Initial.xml
         :language: xml

   .. tab:: Update

      .. literalinclude:: _static/MS181101abc-3-Update.xml
         :language: xml

   .. tab:: Retraction

      .. literalinclude:: _static/MS181101abc-4-Retraction.xml
         :language: xml
