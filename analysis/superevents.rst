Superevents
===========

Superevents are an abstraction to unify gravitational-wave candidates from
multiple search pipelines. Each superevent is intended to represent a single
astrophysical event.

A superevent consists of one or more event candidates, possibly from
:doc:`different pipelines </analysis/searches>`, that are neighbors in time.
At any given time, one event belonging to the superevent is identified as the
*preferred event*. The superevent inherits properties from the preferred event
such as time, significance, sky localization, and classification.

The preferred event may change after a preliminary alert has been sent, but the
name of the superevent will stay the same. The naming scheme is described in
the `alert contents <../content.html#name>`_ section.

Selection of the Preferred Event
--------------------------------

When multiple online searches report events at the same time, the preferred
event is decided by applying the following rules, in order:

1. An event from modeled :term:`CBC` searches are preferred over an event from
   unmodeled Burst searches (see :doc:`Searches </analysis/searches>` for
   details on search pipelines).
2. In the case of multiple CBC events, three-interferometer events are
   preferred over two-interferometer events, and two-interferometer events are
   preferred over single-interferometer events.
3. In the case of multiple CBC events with the same number of participating
   interferometers, the event with the highest :term:`SNR` is preferred. In the
   case of multiple Burst events, the event with the lowest :term:`FAR` is
   preferred.

See also the :ref:`preferred event selection flow chart
<gwcelery.tasks.superevents:Selection of the preferred event>` in our software
documentation.

.. note::
   * A Preliminary GCN is automatically issued for a superevent if the
     preferred event's :term:`FAR` is less than the threshold value stated in
     the :ref:`alert-threshold` section.
   * In case of an event created by a pipeline due to an *offline* analysis, no
     preliminary GCN will be sent.
   * The :term:`SNR` is used to select the preferred event among `CBC`
     candidates because higher :term:`SNR` implies better sky location and
     parameter estimates from low-latency searches.
