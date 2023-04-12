Superevents
===========

Superevents are an abstraction to unify gravitational-wave candidates from
multiple search pipelines. Each superevent is intended to represent a single
astrophysical source.

A superevent consists of one or more event candidates, possibly from
:doc:`different pipelines </analysis/searches>`, that are neighbors in time. At
any given time, one event belonging to the superevent is identified as the
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
