Change Log
==========

Version 17 (unreleased)
-----------------------

.. rubric:: General

.. rubric:: Getting Started Checklist

.. rubric:: Observing Capabilities

.. rubric:: Data Analysis

*  Add the reference to the source properties methods paper.
   Provide details on the cases where the above method is used.

.. rubric:: Alert Contents

.. rubric:: Sample Code

.. rubric:: Additional Resources

Version 16 (2020-05-28)
-----------------------

.. rubric:: General

*  Add the new :doc:`early_warning` section to introduce early warning alerts
   as a public post-O3 technology demonstration. Early warning alerts are
   detections of binary neutron star merger candidates up to tens of seconds
   before merger. **Starting on 2020-06-09 and lasting for one week, simulated
   early-warning alerts from replayed O3 LIGO/Virgo data will be publicly
   distributed at a rate of approximately once per day.**

.. rubric:: Observing Capabilities

*  Note suspension of Observing Run 3 (O3) on March 27, 2020, due to the
   COVID-19 pandemic. When it becomes safe to resume normal activities, there
   may be a short period of additional O3 observations before an extended
   shutdown to prepare for the next observing run (O4). Updates will be posted
   in this document as they become available.

.. rubric:: Alert Contents

*  Add an example EarlyWarning GCN notice.

Version 15 (2020-01-15)
-----------------------

.. rubric:: Observing Capabilities

*  Add sensitivity, detection rate, and localization accuracy statistics for O3
   and O4 from the most recent arXiv submission of the LIGO/Virgo/KAGRA
   observing scenarios paper, :arxiv:`1304.0670`. Add ranges for BBH and NSBH
   sources. Update O3 timeline and range schedule figures. Expect another
   update in the next few weeks incorporating O3a.

Version 14 (2020-01-06)
-----------------------

.. rubric:: Data Analysis

*  Change FAR threshold due to the additional trials from the GRB coincidence
   search.

.. rubric:: Alert Contents

*  Add VOEvent documentation and examples for gravitational-wave events that
   are coincident with GRBs.

Version 13 (2019-12-16)
-----------------------

.. rubric:: Data Analysis

*  Add a note that the oLIB search is not currently in operation.

.. rubric:: Alert Contents

*  Add a warning that :term:`VOEvent` over anonymous :term:`VTP` is the only
   GCN format and distribution method that is fully supported by LIGO/Virgo. In
   particular, LIGO/Virgo performs only limited quality control control checks
   for the textual "full format" and the binary format.

*  In the VOEvent alert schema, add a ``name`` attribute to each ``<Group>``
   tag so that parameter groups are recognized by the
   :func:`~voeventparse.convenience.get_grouped_params` function from the
   :doc:`voevent-parse:index` package. For backwards compatibility, both the
   ``name`` attribute and the ``type`` attribute will be set to the same value.

   The groups are now denoted as follows:

   *  ``<Group name="GW_SKYMAP" type="GW_SKYMAP">`` for localization parameters
   *  ``<Group name="Classification" type="Classification">`` for compact
      binary source classification parameters
   *  ``<Group name="Properties" type="Properties">`` for compact binary source
      properties parameters

.. rubric:: Additional Resources

*  Add the `Chirp <https://www.laserlabs.org/chirp.php>`_ mobile app for iOS
   and Android by Laser Labs.

Version 12 (2019-10-24)
-----------------------

.. rubric:: Observing Capabilities

*  Update ranges and rates based on up-to-date O3 analysis. Add BBH and NSBH
   ranges. Update range and observing schedule figures.

*  Generalize the definition of the range so that it is unambiguous at high
   redshift. It is now defined as in :arxiv:`1709.08079`.

*  Add the end date of Observing Run 3 (O3) on 2020-04-30.

.. rubric:: Data Analysis

*  Document the false alarm rate threshold for public alerts.

.. rubric:: Alert Contents

*  Remove the documentation for the Fluence parameter from burst alerts because
   it is not currently present in the VOEvents.

*  Update the list of pipeline names that can appear in GCN Notices.

.. rubric:: Additional Resources

*  Created a new section for additional and contributed tools. The
   :doc:`ligo.skymap </resources/ligo.skymap>` and :doc:`Aladin
   </resources/aladin>` pages have been moved into this section.

*  Add instructions for cross-matching sky localizations with galaxy catalogs
   in Aladin Desktop.

*  Add the unofficial iOS Gravitational Wave Events app.

Version 11 (2019-09-15)
-----------------------

.. rubric:: Data Analysis

*  Update the documentation about superevents describing the criteria by which
   the preferred event is selected. For CBC events, events with three detectors
   are preferred over two detectors, and events with two detectors are
   preferred over events with one detector.

.. rubric:: Alert Contents

*  Add references to the HEALPix paper (Górski et al. 2005,
   :doi:`10.1086/427976`).

*  Add version number suffixes to sky map FITS filenames in GCN notices to
   distinguish between different sky maps with the same filename. For example,
   the first file with the name ``bayestar.fits.gz`` will be referred to as
   ``bayestar.fits.gz,0``, then the next will be ``bayestar.fits.gz,1``, and so
   on. The filename with no version suffix always points to the most recent
   version.

.. rubric:: Sample Code

*  Add attribution for a HEALPix illustration that was reproduced from
   https://healpix.jpl.nasa.gov.

*  Fix the example image for ``hp.mollview()``, which was distorted due to a
   file conversion issue.

*  Add section on sky map visualization and credible regions in Aladin.

Version 10 (2019-07-31)
-----------------------

.. rubric:: Data Analysis

*  Add a more detailed description of the RAVEN pipeline. Previously just
   mentioned types of searches but now has information on external
   experiments, coincident searches, and coincident false alarm rates.

* Fixed PyCBC Live reference.

.. rubric:: Alert Contents

* Changed the data type of the ``UNIQ`` column of the multi-order sky map
  format from an unsigned integer to a signed integer as specified by the
  `MOC-in-FITS standard`_.

  This will improve interoperability with the `mrdfits`_ function from the `IDL
  Astronomy User's Library`_ and the `fv FITS Viewer`_ from `FTOOLS`_, both of
  which were reported to have problems with the old unsigned integer column. It
  will also make it simpler to work with Numpy indexing operations, since Numpy
  uses a signed integer type for indexing.

  This change will go into effect in the LIGO/Virgo low-latency alert system on
  2019-08-06.

  Users of `ligo.skymap`_ should update to version 0.1.8 or newer because older
  versions will be unable to read old files with unsigned ``UNIQ`` columns. The
  new version of ``ligo.skymap`` can read files with either signed or unsigned
  ``UNIQ`` columns.

.. _`MOC-in-FITS standard`: http://www.ivoa.net/documents/MOC/
.. _`mrdfits`: https://idlastro.gsfc.nasa.gov/ftp/pro/fits/mrdfits.pro
.. _`IDL Astronomy User's Library`: https://idlastro.gsfc.nasa.gov/homepage.html
.. _`fv FITS Viewer`: https://heasarc.gsfc.nasa.gov/ftools/fv/
.. _`FTOOLS`: https://heasarc.gsfc.nasa.gov/ftools/
.. _`ligo.skymap`: https://lscsoft.docs.ligo.org/ligo.skymap/

Version 9 (2019-06-13)
----------------------

.. rubric:: General

* There is now a shorter URL for the Public Alerts User Guide, which can now be
  found at either https://emfollow.docs.ligo.org or
  https://emfollow.docs.ligo.org/userguide.

.. rubric:: Data Analysis

* Renamed this section from "Procedures" to "Data Analysis" and reordered its
  subsections to better reflect the chronological order of the steps of the
  analysis.

.. rubric:: Sample Code

* Add tutorial on working with multi-resolution sky maps.

* Add sample code to test whether a sky position is in the 90% credible region.

* Add sample code to find the area of the 90% credible region.

Version 8 (2019-05-22)
----------------------

.. rubric:: Alert Contents

* Describe the two localization formats, the official ``*.fits.gz``
  HEALPix-in-FITS format and the experimental multi-resolution HEALPix
  ``*.multiorder.fits`` format.

  Effective 2019-05-28, the multi-resolution file suffix will be renamed from
  ``*.fits`` to ``*.multiorder.fits``. The old ``*.fits`` suffix had caused
  confusion because the multi-resolution format is *not* the same as the
  ``*.fits.gz`` files without gzip compression.

  **The multi-resolution format is currently recommended only for advanced
  users.** Tutorials and sample code will soon be included in an upcoming
  version of the User Guide.

* Update the description of the ``HasNS`` property in the sample GCN Notices.
  Previously, it was defined as the probability that at least one object in the
  binary has a mass that is less than 2.83 solar masses. Now, for consistency
  with the source classification definitions, it is defined as the probability
  that at least one object in the binary has a mass that is less than 3 solar
  masses.

* Add some shading to the source classification diagram to make it clear that
  the definitions of the source classes are symmetric under exchange of the
  component masses, but that by convention the component masses are defined
  such that :math:`m_1 \geq m_2`.

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
