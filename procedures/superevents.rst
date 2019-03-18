Superevents
===========

Superevents are a new abstraction to unify gravitational-wave candidates from
multiple search pipelines. Each superevent is intended to represent a single
astrophysical event.

A superevent consists of one or more event candidates, possibly from
:doc:`different pipelines </procedures/searches>`, that are neighbors in time.
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

1. Events that are detected in multiple interferometers are preferred over an
   events from a single interferometer.
2. Events from modeled :term:`CBC` searches are preferred over events from
   unmodeled Burst searches (see :doc:`Searches </procedures/searches>` for
   details on search pipelines).
3. In the case of multiple CBC events, the event with the highest signal to
   noise ratio (SNR) is preferred. In the case of multiple Burst events, the
   event with the lowest false alarm rate (FAR) is preferred.

.. note::
   A Preliminary GCN is automatically issued for superevents when the false
   alarm rate is lower than a threshold value.

.. note::
   In case of an *offline* trigger upload from a pipeline, no
   preliminary GCN will be sent.
