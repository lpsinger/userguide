LIGO/Virgo/KAGRA Public Alerts User Guide
=========================================

This Git repository contains the source code for the LIGO/Virgo/KAGRA Public
Alerts User Guide. For most recently released HTML edition of the User Guide,
visit http://emfollow.docs.ligo.org/.

We welcome feedback and suggestions. To report an issue related to the User
Guide, please send an e-mail to emfollow-userguide@support.ligo.org.

Building
--------

To render the HTML version of the User Guide on your own computer, make sure
that you have a working Python environment with Python >= 3.5. Then run the
following commands::

    python -m venv env
    source env/bin/activate
    git clone https://git.ligo.org/emfollow/userguide.git
    cd userguide
    pip install -r requirements.txt
    make html

Then open the main page _build/html/index.html in your favorite browser.

Publishing a new version
------------------------

When you are ready to publish a new version, follow these steps:

1.  **Update the the current version's change log entry.** Edit the change log
    in `changes.rst`_ following the steps below.

    **Make one last check that the change log is up to date.** Check that the
    current change log entry lists all of the important changes from the past
    version.

    **Update the release date.** You will find that the current versions's
    section of the change log has a title like ``vNN (unreleased)``, where NN
    will be the version number of the new release. Change the title of that
    section to ``vNN (YYYY-MM-DD)``, where YYYY-MM-DD is today's date.

    **Remove empty change log rubrics.** The current version's section will
    have rubrics for each top-level page of the User Guide, such as ``..
    rubric:: Getting Started Checklist``, ``.. rubric:: Alert Contents``, and
    so on. Some of these rubrics may be empty because there were no changes to
    the corresponding section. Delete any empty rubrics.

    **Save and commit the updated change log.** Commit the change log with a
    message such as ``Update change log for version NN``.

2.  **Create a new version tag.** Create a new version tag to mark the release
    by running the following command (replace NN with the new version number)::

        $ git tag vNN -m "Version NN"

3.  **Create a new dummy change log entry for the next version.** Go back to
    editing `changes.rst`_ and make a new section with the title ``Version MM
    (unreleased)``, where MM is NN + 1. Add empty rubrics for every top-level
    page. Commit the change log with a message such as ``Back to development``.

4.  **Push the new tag and updated change log.** Check your work carefully by
    running ``git log -p`` and looking at your two new commits. Then, push the
    new tag and updated change log to GitLab::

        git push && git push --tags

    You will need the appropriate permission to push the new tag. If required,
    contact one of the maintainers.

    Within a few minutes, the official live version at
    http://emfollow.docs.ligo.org/ will be updated automatically.

5.  **Send an announcement to the OpenLVEM list.** Compose an email starting
    from `a recent example`_ or from the template below:

        Subject: Announcing version *NN* of the LIGO/Virgo/KAGRA Public Alerts
        User Guide, including *BRIEF PHRASE DESCRIBING MAJOR CHANGES*
        
        Dear colleagues,
        
        We made some changes to the LIGO/Virgo/KAGRA Public Alerts User Guide
        (https://emfollow.docs.ligo.org/). The most significant update is *A
        FEW WORDS CALLING ATTENTION TO THE MOST IMPORTANT CHANGES*.
        
        
        As always, we welcome further feedback by email at
        <emfollow-userguide@support.ligo.org>.
        
        Below is a complete list of changes since the last version.
        
        | Sincerely yours,
        | *YOUR NAME HERE*
        | for the LIGO, Virgo, and KAGRA Collaborations
        |

        Version *NN* (*YYYY*-*MM*-*DD*)
        
        *INSERT VERBATIM COPY OF CURRENT CHANGE LOG, INCLUDING TOP-LEVEL PAGE
        RUBRICS*

    Send the message to openlvem@gw-astronomy.org.

.. _`changes.rst`: https://git.ligo.org/emfollow/userguide/-/blob/master/changes.rst
.. _`a recent example`: https://gw-astronomy.org/lists/arc/openlvem/2020-01/msg00010.html
