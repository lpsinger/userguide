Alert Content
=============

.. Should mention:
.. 
..  * Description of the notices: https://wiki.ligo.org/Bursts/EMFollow/O3GCNnotices
..  * Description of the circulars
.. * also some info here https://dcc.ligo.org/LIGO-G1800404/public

Public LIGO/Virgo alerts are distributing using NASA's Gamma-ray Coordinates
Network (:term:`GCN`). There are two types of alerts:

* **Circulars** are human-readable astronomical bulletins.

* **Notices** are machine-readable packets, available as VOEvent XML and
  several legacy plain text and binary formats.

Alert Schema
------------

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
