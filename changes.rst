Change Log
==========

Version 3 (unreleased)
----------------------

.. rubric:: General

.. rubric:: Getting Started Checklist

.. rubric:: Observing Capabilities

.. rubric:: Procedures

.. rubric:: Alert Contents

.. rubric:: Sample Code

Version 2 (2018-12-13)
----------------------

.. rubric:: Alert Contents

* Removed the ``Vetted`` parameter from GCN Notices. It was intended to
  indicate whether the event had passed human vetting. However, it was
  redundant beacuse by definition Preliminary events have not been vetted
  and all Initial and Update alerts have been vetted.

* The type of the ``Retraction`` parameter in the GCN Notices was changed from
  a string (``false`` or ``true``) to an integer (``0`` or ``1``) for
  consistency with other flag-like parameters.

* Remove the ``units`` attribute from parameters that are not numbers.

.. rubric:: Sample Code

* GCN has now begun publicly broadcasting sample LIGO/Virgo GCN Notices.
  Updated the sample code accordingly with instructions for receiving live
  sample notices.

Version 1 (2018-11-27)
----------------------

.. rubric:: Getting Started Checklist

* Updated instructions for joining the OpenLVEM Community.

.. rubric:: Observing Capabilities

* Changed the expected number of BNS events in O3 from 1-50, as stated in the
  latest version of the Living Review, to 1-10 events, as stated in the more
  recent rates presentation.

.. rubric:: Alert Contents

* In the example VOEvents, moved the Classification and Inference quantities
  from the ``<Why>`` section to the ``<What>`` section so that they validate
  against the VOEvent 2.0 schema.
