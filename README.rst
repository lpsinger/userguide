LIGO/Virgo Public Alerts User Guide
===================================

This Git repository contains the source code for the LIGO/Virgo Public Alerts
User Guide. For the latest HTML edition of the User Guide, visit
http://emfollow.docs.ligo.org/userguide/.

We welcome feedback and suggestions. To report an issue related to the User
Guide, please send an e-mail to contact+emfollow/userguide@support.ligo.org.

Building
--------

To render the HTML version of the User Guide on your own computer, make sure
that you have a working Python environment with Python >= 3.5. Then run the
following commands::

    git clone https://git.ligo.org/emfollow/userguide.git
    cd userguide
    python -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    make html

Then open the main page _build/html/index.html in your favorite browser.
