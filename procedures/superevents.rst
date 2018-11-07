Superevents
===========

*Superevents* are a new abstraction of gravitational-wave candidates introduced
in the third LIGO/Virgo observing (O3). Each superevent is intended to represent
a single astrophysical event. A superevent consists of one or more event
candidates, possibly from different pipelines, that are neighbors in `gpstime`.
One event belonging to the superevent is identified as the preferred event.

In the event of multiple triggers from the different low-latency search pipelines,
the *preferred event* is selected based on the following:

* A multi-interferometer trigger is always preferred over a single-interferometer
  trigger irrespective of the type of search.
* When comparing multi-interferometer triggers, modeled searches from CBC
  search pipelines are preferred over unmodeled Burst searches.
  (see :doc:`Searches </procedures/searches>` for details on search types).
* When comparing multi-interferometer triggers from the same search category, the
  tie is broken based on the false alarm rate (FAR) statistic for Burst and
  the signal to noise ratio (SNR) for CBC.

The preferred event is subjected to change as search pipelines upload triggers.
In case of an *offline* trigger upload from a pipeline, no preliminary GCN will
be sent.
