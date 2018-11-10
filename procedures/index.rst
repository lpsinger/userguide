Procedures
==========

In this section we describe the different online searches looking for GW
signals. The corresponding triggers from multiple pipelines close enough in
time will be considered at originating from the same physical event and will be
grouped in a unique :doc:`superevent <superevents>`. See the following pages
for technical details.

.. toctree::
   :maxdepth: 1

   searches
   superevents
   parameter_estimation
   inference

The timeline for distribution of alerts is described below.

Alert Timeline
--------------

Here, we described the sequence of the GW alert distributed the Gamma-ray
Coordinates Network (:term:`GCN`) via notices and circulars (:doc:`Alert
content </content>` and :doc:`Technical </tutorial/index>`). Alerts should
contain all of the information that is useful for searching for a counterpart.

**Within minutes after GW trigger time**, the first :doc:`preliminary notice
</content>` will be sent fully autonomously (not necessary attached to
localization). The trigger will be immediately visible under the LIGO/Virgo GW
database :term:`GraceDb`. As soon as the skymap localization area is available,
a second preliminary notice is sent. The procedure is fully automatic and some
preliminary alerts may be retracted after human inspection for data quality,
instrumental conditions, and pipeline behavior.

**Within 4 hours after the GW trigger time**, the :doc:`Initial notices and
circulars </content>` will be distributed with an update for the sky
localization area and the source classification. They are vetted by human
instrument scientists and analysts. In case of a binary coalescence including a
neutron star or a burst trigger, the initial circular can labeled as
**retractated** (data are unsuitable) or **confirmed**. Note that the initial
circular is considered the first LIGO/Virgo publication of a GW candidate,
appropriate to cite in publications.

**Within a day**, black hole mergers will be fully vetted by experts and
retraction or confirmation status will be reported.

:doc:`Update notice and circulars </content>` are sent whenever the sky
localization area or significance accuracy improves (e.g. as a result of
improved calibration, de-glitching, or computationally deeper parameter
estimation). Updates will be sent up until the position is determined more
accurately by public announcement of an unambiguous counterpart. At which point
they will stop until publication of the event.

**Any time**, we can **promote** an extraordinary candidate that does not pass
our public alert thresholds if it is compellingly associated with a
multimessenger signal (e.g. GRB, core-collapse SN). In this case, :doc:`Initial
notices and circulars </content>` will be distributed.
  
.. image:: /_static/Flowchartprocv2.jpg
   :alt: Alert Flowchart
