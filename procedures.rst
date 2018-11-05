Procedures
==========

Here, we described the sequence of the GW alert distributed the Gamma-ray Coordinates Network/Transient Astronomy Network (`GCN/TAN`_) via notices and circulars (`Alert content`_ and `Technical`_). Alerts should contain all of the information that is useful for searching for a counterpart 

.. _`GCN/TAN`: http://gcn.gsfc.nasa.gov/
.. _`Alert content`: https://emfollow.docs.ligo.org/userguide/content.html
.. _`preliminary notice`: https://emfollow.docs.ligo.org/userguide/content.html
.. _`Initial notices and circulars`: https://emfollow.docs.ligo.org/userguide/content.html
.. _`Technical`: https://emfollow.docs.ligo.org/userguide/technical.html
.. _`GraceDB`: https://gracedb.ligo.org/

Within minutes after GW trigger time: No human inspection!
----------------------------------------------------------

1) The first `preliminary notice`_ will be sent fully autonomously (not necessary attached to localization). The trigger will be immediately visible under the LIGO/Virgo GW database `GraceDB`_.
2) Second and others preliminaries: same content but does contain a localization (BAYESTAR for CBC events).

Beware! Some preliminary alerts may be retracted after human inspection for data quality, instrumental conditions, and pipeline behavior.

Within 4 hours after the GW trigger time: vetted by human instrument scientists and analysts
--------------------------------------------------------------------------------------------

* `Initial notices and circulars`_ with an update for the sky localization area and the source classification. 
* Possible **retractation** (data are unsuitable) or **confirmation** of the event for BNS or Burst triggers
  Note that the initial Circular is considered the first publication of a GW candidate, appropriate to cite in publications


After 4 hours : manual updates for sky localization area
--------------------------------------------------------

* Sent whenever localization or significance accuracy improves (e.g. as a  result of improved calibration, de-glitching, or computationally deeper parameter estimation)
* Updates will be sent up until the position is determined more accurately by public announcement of an unambiguous counterpart, at which point they will stop until publication of the event
* Possible retractation for BBH events within a day


Special case : promotion of sub-thresholds candidates
-----------------------------------------------------
 
* We can elect to promote a candidate that does not pass our OPA thresholds if it is compellingly associated with a multimessenger signal (e.g. GRB, core-collapse SN)
* The procedure will start from the `Initial notices and circulars`_ sequence.
