Superevents
===========

Superevents are an abstraction to unify gravitational-wave candidates from
multiple search pipelines. Each superevent is intended to represent a single
astrophysical source.

A superevent consists of one or more event candidates, possibly from
:doc:`different pipelines </analysis/searches>`, that are clustered based on
coalescence time for modeled searches, and trigger time for unmodeled searches. 

.. note:: While the initial clustering window for superevents is 1 second, 
   this window can expand as event candidates are added. 
   Concretely, if the time of the first event is :math:`t`, 
   the window for the superevent is :math:`(t - 1, t + 1)`. 
   If the next event candidate arrives at :math:`t + 0.1`, 
   the window becomes :math:`(t - 1, t + 1.1)`. In this way, 
   the superevent windows can become larger than 1 second.

At any given time, one event belonging to the superevent is identified as the
*preferred event*. The superevent inherits properties from the preferred event
such as time, significance, sky localization, and classification.

The superevent accumulates event candidates from the :doc:`search pipelines
</analysis/searches>` and updates its preferred event as more significant event
candidates are reported (see :ref:`preferred-event`). The name of the
superevent does not change. The naming scheme is described in the `alert
contents <../content.html#name>`_ section. Once a preferred event candidate
passes the public alert threshold (see :ref:`alert-threshold`), it is frozen
and a preliminary alert is queued using the data products of this preferred
event. New event candidates are still allowed to be added to the superevent as
the necessary annotations are completed. Once the preliminary alert is received
by the GCN broker, the preferred event is revised after a `timeout
<https://gwcelery.readthedocs.io/en/latest/gwcelery.conf.html#gwcelery.conf.supe
revent_clean_up_timeout>`_ and a second preliminary notice is issued. Note that
the latter is issued even if the preferred event candidate remains unchanged.

.. _preferred-event:

Selection of the Preferred Event
--------------------------------

When multiple online searches report events at the same time, the preferred
event is decided by applying the following rules, in order:

1. A *publishable* event, meeting the public alert threshold, is given
   preference over one that does not meet the threshold.
2. An event from :term:`CBC` searches is preferred over an event from
   unmodeled Burst searches (see :doc:`Searches </analysis/searches>` for
   details on search pipelines).
3. In the case of multiple CBC events, three-interferometer events are
   preferred over two-interferometer events, and two-interferometer events are
   preferred over single-interferometer events.
4. In the case of multiple CBC events with the same number of participating
   interferometers, the event with the highest :term:`SNR` is preferred.
   The :term:`SNR` is used to select the preferred event among `CBC`
   candidates because higher :term:`SNR` implies better sky location and
   parameter estimates from low-latency searches. In the case of multiple
   Burst events, the event with the lowest :term:`FAR` is preferred.

See also the :ref:`preferred event selection flow chart
<gwcelery.tasks.superevents:Selection of the preferred event>` in our software
documentation.

.. _per-pipeline-info:

Per Pipeline Event Information
------------------------------

.. image:: ../_static/per-pipeline-screenshot.png
   :width: 600px
   :alt: Per-pipeline information for S230927l
   :align: center

For many GW candidates, multiple pipelines will produce at least one event.
The `Per Pipeline Event Information` table on :term:`GraceDB` for superevents
associated with a :ref:`significant alert <alert-threshold>` displays properties
of the highest :term:`SNR` event from each search pipeline. Specifically, we
provide the estimated GW arrival time and significance (:term:`FAR`). In general,
we expect significant :term:`CBC` candidates to be identified in more than one
pipeline, though there may be exceptions for events seen in only a single
detector.
