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

GCN Notice Contents
-------------------

Like all VOEvent XML packets, LIGO/Virgo GCN Notices contain of several
top-level sections (Who, WhereWhen, What). The table below is a diagrammatic
representation of the contents of a LIGO/Virgo GCN Notice.

+-------------------+-------------------------------------------+-------------------------------------------------------+
|                   | CBC                                       | Burst                                                 |
+===================+===========================================+=======================================================+
| **IVORN**         | :samp:`ivo://nasa.gsfc.gcn/LVC#S{YYMMDDabc}-{{1,2,3}}-{{Preliminary,Initial,Update,Retraction}}`  |
+-------------------+-------------------------------------------+-------------------------------------------------------+
| **Who**           | :samp:`LIGO Scientific Collaboration and Virgo Collaboration`                                     |
+-------------------+-------------------------------------------+-------------------------------------------------------+
| **WhereWhen**     | Arrival time (UTC, ISO-8601), e.g. :samp:`2010-08-27T19:21:13.982800`                             |
+-------------------+-------------------------------------------+-------------------------------------------------------+
| **What**          | GraceDb ID: :samp:`S{YYMMDDabc}`                                                                  |
+-------------------+-------------------------------------------+-------------------------------------------------------+
| - Search          | :samp:`CBC`                               | :samp:`Burst`                                         |
+-------------------+-------------------------------------------+-------------------------------------------------------+
| - Pipeline        | :samp:`{{Gstlal,MBTA,PyCBC,SPIIR}}`       | :samp:`{{cWB,oLIB}}`                                  |
+-------------------+-------------------------------------------+-------------------------------------------------------+
| - FAR             | Estimated false alarm rate in Hz                                                                  |
+-------------------+-------------------------------------------+-------------------------------------------------------+
| - Network         | Flag for each detector (:samp:`LHO_participated`, etc.)                                           |
+-------------------+-------------------------------------------+-------------------------------------------------------+
| - Sky map         | URL of HEALPix FITS localization file                                                             |
+-------------------+-------------------------------------------+-------------------------------------------------------+
| - ProbHasNS,      | Probability (0–1) that the less massive   |                                                       |
|   ProbHasRemnant  | companion has mass :math:`<3 M_\odot`,    |                                                       |
|                   | and that the system ejected a significant |                                                       |
|                   | amount of NS material, respectively       |                                                       |
+-------------------+-------------------------------------------+-------------------------------------------------------+

Preliminary Alert
-----------------

Within minutes after a gravitational wave trigger an automated, **preliminary
alert** will be issued, in the form of a *notice* only. It will contain the
`event name`_, trigger time and a link to the `source localization`_ "skymap"
(if available). Being the result of a fully autonomous pipeline, this
preliminary notice might be subsequently *retracted* after human vetting.

Initial Alert
-------------

Within 4 hours of the preliminary alert, after vetting by human instrument
scientists and data analysts, an **initial alert** will be issued in the form
of both a *circular* and a *notice*. Such initial alert could contain the
possible *retraction* of the candidate, in case of e.g. data quality issues.
The initial alert GCN circular is considered as the first publication of a
candidate, and it can be cited as such.

The initial alert circular and notice contain the following information:

* `event name`_ and GraceDb identifier(s)
* event significance_
* `source classification`_
* `source localization`_
* (...)

The alert may also contain a `data quality assessment`_.

The purpose of the alerts is to allow for an effective electro-magnetic
follow-up of the candidates: `quantitative intrinsic infomation on the sources
that is not vital to this purpose`_ is thus not provided in the alerts.

Alert update
------------

Whenever refined GW data analysis leads to improved estimates of the event
localization, significance or classification, an alert update can be issued.
The alert update is issued both as a circular and a notice, with the updated
information. The update may also contain a retraction of the candidate.


Content description
-------------------

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
space ("3D localization", currently only available if the source is a CBC). The
probability distribution is encoded as a FITS file (...provide link to skymap
documentation...).

.. _`data quality assessment`:

**Data quality assessment**

Circulars may contain concise descriptions of any instrument or data quality
issues that may affect the significance estimates or the GW parameter
inferences. Unresolved data quality issues could mean that localization
estimates may shift after they have been mitigated, but does not mean that they
will. This is to be considered as advisory information.

.. _`quantitative intrinsic infomation on the sources that is not vital to this purpose`:

What will *not* be included in the alerts
-----------------------------------------

The alerts are not going to release quantitative estimates of intrinsic
properties such as masses and spins, nor contain information on the GW strain
or reconstructed waveforms.

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
