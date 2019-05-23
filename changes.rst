Change Log
==========

Version 8 (unreleased)
----------------------

.. rubric:: General

.. rubric:: Getting Started Checklist

.. rubric:: Observing Capabilities

.. rubric:: Procedures

.. rubric:: Alert Contents

* Update the description of the ``HasNS`` property in the sample GCN Notices.
  Previously, it was defined as the probability that at least one object in the
  binary has a mass that is less than 2.83 solar masses. Now, for consistency
  with the source classification definitions, it is defined as the probability
  that at least one object in the binary has a mass that is less than 3 solar
  masses.

* Describe the two localization formats, the official ``*.fits.gz``
  HEALPix-in-FITS format and the experimental multi-resolution HEALPix
  ``*.multiorder.fits`` format.

  The multi-resolution file suffix has been renamed from ``*.fits`` to
  ``*.multiorder.fits``. The old ``*.fits`` suffix had caused confusion because
  the multi-resolution format is *not* the same as the ``*.fits.gz`` files
  without gzip compression.

  **The multi-resolution format is experimental, and it is currently
  recommended only for advanced users.** Tutorials and sample code will be
  included in the next version of the User Guide.

* Add some shading to the source classification diagram to make it clear that
  the definitions of the source classes are symmetric under exchange of the
  component masses, but that by convention the component masses are defined
  such that :math:`m_1 \geq m_2`.

.. rubric:: Sample Code

Version 7.1 (2019-03-02)
------------------------

* Remove the warning on the front page about significant changes to this
  document occurring before the start of O3.

Version 7 (2019-03-02)
----------------------

.. rubric:: Observing Capabilities

* Record the official start of O3.

.. rubric:: Procedures

* Add Gravitational Wave/High Energy Neutrino search to the list of
  multi-messenger search pipelines.

.. rubric:: Sample Code

* Add instructions for installing required packages using the Anaconda Python
  distribution.

Version 6 (2019-03-08)
----------------------

.. rubric:: Alert Contents

* Switch to the GW170817 Hanford-Livingston-Virgo localization for the example
  sky map.

Version 5 (2019-03-01)
----------------------

.. rubric:: Alert Contents

* Add a human-readable description to the ``Pkt_Ser_Num`` parameter.

* Add ``<EventIVORN cite="supersedes">`` elements to the sample Initial and
  Update notices in order to cite all prior VOEvents. GraceDB already includes
  this metadata, but it was missing from the examples.

* Add MassGap classification for compact binary mergers.

Version 4 (2019-02-15)
----------------------

.. rubric:: General

* Changed the contact email to <emfollow-userguide@support.ligo.org> because
  some mail clients had trouble with the slash in the old contact email
  address, <contact+emfollow/userguide@support.ligo.org>. (The old address will
  also still work.)

.. rubric:: Getting Started Checklist

* Update links for OpenLVEM enrollment instructions.

.. rubric:: Observing Capabilities

* Update planned dates for Engineering Run 14 (ER14; starts 2019-03-04) and
  Observing Run 3 (O3; starts 2019-04-01).

* Add Live Status section, listing some public web pages that provide real-time
  detector status.

.. rubric:: Sample Code

* Update the example GCN notice handler so that it does not fail if the notice
  is missing a sky map, because as we have specified them, ``LVC_RETRACTION``
  notices never contain sky maps and ``LVC_PRELIMINARY`` notices may or may not
  contain sky maps.

* When building the documentation, test all of the sample code automatically.

Version 3 (2019-02-13)
----------------------

.. rubric:: Alert Contents

* Remove the ``skymap_png`` parameter from the VOEVents. The sky map plots take
  longer to generate than the FITS files themselves, so they would have
  needlessly delayed the preliminary alerts.

* Change the IVORN prefix from ``ivo://gwnet/gcn_sender`` to
  ``ivo://gwnet/LVC``, because GCN traditionally uses the text after the ``/``
  to indicate the name of the mission, which most closely corresponds to "LVC,"
  short for "LIGO/Virgo Collaboration." Note that this IVORN is used for
  historical purposes and continuity with the GCN notice format used in O1 and
  O2, and is likely to change in the future with the commissioning of
  additional gravitational-wave facilities.

* Retraction notices now get a separate GCN notice packet type,
  ``LVC_RETRACTION=164``. The ``Retraction`` parameter has been removed from
  the ``<What>`` section.

Version 2 (2018-12-13)
----------------------

.. rubric:: Alert Contents

* Removed the ``Vetted`` parameter from GCN Notices. It was intended to
  indicate whether the event had passed human vetting. However, it was
  redundant because by definition Preliminary events have not been vetted
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
