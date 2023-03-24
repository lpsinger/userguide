Kafka Notices via GCN
=====================

In this section, we'll show you how to register for a GCN account and then set
up credentials to receive JSON-serialized notices over Kafka. We will then
write a script to receive and parse these notices. Finally, we'll download and
parse an example notice.

Account Creation and Credential Generation
------------------------------------------

1. Sign up for an account at https://gcn.nasa.gov/quickstart.
2. Create new credentials by following the guide from the previous step. Select
   ``gcn.nasa.gov/kafka-public-consumer`` from the Scope drown-down menu (this
   should already be selected by default).
3. Do not click on any of the check boxes in the Customize Alerts section.
4. Record the ``client_id`` and ``client_secret`` values in the generated code
   on the next section.

   .. note::
      You can retrieve your ``client_id`` and ``client_secret`` at a later time by
      signing in at https://gcn.nasa.gov and navigating to the credentials page.
      This page can be found in the drop-down menu underneath your sign-in name in
      the top menu-bar.

Receiving and Parsing Notices
-----------------------------

Once you are authenticated to receive JSON-serialized LIGO/Virgo/KAGRA notices
from GCN, we can write a function to parse them.

.. important::
   Note that mock or 'test' observations have superevent IDs that begin with
   'M', while real observations have superevent IDs that begin with 'S'. Mock
   events also list the search that found them as 'MDC', however this field is
   not present in retraction alerts so it is best to check the first character
   of the superevent ID to distinguish between the two.

.. testcode::

    from base64 import b64decode
    from io import BytesIO
    import json
    from pprint import pprint

    from astropy.table import Table
    import astropy_healpix as ah
    from gcn_kafka import Consumer
    import numpy as np

    def parse_notice(record):
        record = json.loads(record)

        # Only respond to mock events. Real events have GraceDB IDs like
        # S1234567, mock events have GraceDB IDs like M1234567.
        # NOTE NOTE NOTE replace the conditional below with this commented out
        # conditional to only parse real events.
        # if record['superevent_id'][0] != 'S':
        #    return
        if record['superevent_id'][0] != 'M':
            return

        if record['alert_type'] == 'RETRACTION':
            print(record['superevent_id'], 'was retracted')
            return

        # Respond only to 'CBC' events. Change 'CBC' to 'Burst' to respond to
        # only unmodeled burst events.
        if record['event']['group'] != 'CBC':
            return

        # Parse sky map
        skymap_str = record.get('event', {}).pop('skymap')
        if skymap_str:
            # Decode, parse skymap, and print most probable sky location
            skymap_bytes = b64decode(skymap_str)
            skymap = Table.read(BytesIO(skymap_bytes))

            level, ipix = ah.uniq_to_level_ipix(
                skymap[np.argmax(skymap['PROBDENSITY'])]['UNIQ']
            )
            ra, dec = ah.healpix_to_lonlat(ipix, ah.level_to_nside(level),
                                           order='nested')
            print(f'Most probable sky location (RA, Dec) = ({ra.deg}, {dec.deg})')

            # Print some information from FITS header
            print(f'Distance = {skymap.meta["DISTMEAN"]} +/- {skymap.meta["DISTSTD"]}')

        # Print remaining fields
        print('Record:')
        pprint(record)

The final step is to set up a Kafka consumer that calls our function whenever a
notice is received.

::

    consumer = Consumer(client_id='fill me in', client_secret='fill me in')
    consumer.subscribe(['igwn.gwalert'])

    while True:
        for message in consumer.consume():
            parse_notice(message.value())

When you run this script you should receive a sample LIGO/Virgo/KAGRA notice
every hour. The output will be the same as the output in the
:ref:`offline-testing-gcn` section below.

.. _offline-testing-gcn:

Offline Testing
---------------

Sample files are available to download at any time for testing responses to
notices without needing to wait for the one-per-hour example. 

.. code-block:: shell-session

    $ curl -O https://emfollow.docs.ligo.org/userguide/_static/MS181101ab-preliminary.json

This file can be parsed as follows:

.. testsetup::

    import os
    import unittest.mock
    import urllib.parse
    from urllib.request import urlopen, Request

    old_dir = os.getcwd()
    os.chdir('_static')

    def patched_urlopen(url, *args, **kwargs):
        new_url = url
        if isinstance(new_url, Request):
            new_url = new_url.full_url
        parsed_url = urllib.parse.urlparse(new_url)
        dirname, basename = os.path.split(parsed_url.path)
        if parsed_url.netloc != 'emfollow.docs.ligo.org' \
                or dirname != '/userguide/_static':
            return urlopen(url, *args, **kwargs)
        return urlopen('file:{}'.format(basename), 'rb')

    patcher = unittest.mock.patch('urllib.request.urlopen', patched_urlopen)
    patcher.start()


.. testcode::

    # Read the file and then parse it
    with open('MS181101ab-preliminary.json', 'r') as f:
        record = f.read()

    parse_notice(record)

Running this should produce the following output:

.. testoutput::

   Most probable sky location (RA, Dec) = (194.30419921874997, -17.856895095545468)
   Distance = 39.76999609489013 +/- 8.308435058808886
   Record:
   {'alert_type': 'PRELIMINARY',
    'event': {'central_frequency': None,
              'classification': {'BBH': 0.03,
                                 'BNS': 0.95,
                                 'NSBH': 0.01,
                                 'Terrestrial': 0.01},
              'duration': None,
              'far': 9.11069936486e-14,
              'group': 'CBC',
              'instruments': ['H1', 'L1', 'V1'],
              'pipeline': 'gstlal',
              'properties': {'HasMassGap': 0.01,
                             'HasNS': 0.95,
                             'HasRemnant': 0.91},
              'search': 'MDC',
              'significant': True,
              'time': '2018-11-01T22:22:46.654Z'},
    'external_coinc': None,
    'superevent_id': 'MS181101ab',
    'time_created': '2018-11-01T22:34:49Z',
    'urls': {'gracedb': 'https://example.org/superevents/MS181101ab/view/'}}

.. testcleanup::

    os.chdir(old_dir)

Examples
--------

Below are some sample JSON alerts that can be used for testing purposes.

* :download:`MS181101ab-earlywarning.json </_static/MS181101ab-earlywarning.json>`
* :download:`MS181101ab-preliminary.json </_static/MS181101ab-preliminary.json>`
* :download:`MS181101ab-initial.json </_static/MS181101ab-initial.json>`
* :download:`MS181101ab-update.json </_static/MS181101ab-update.json>`
* :download:`MS181101ab-retraction.json </_static/MS181101ab-retraction.json>`
* :download:`MS181101ab-ext-update.json </_static/MS181101ab-ext-update.json>`

.. _confluent-kafka: https://pypi.org/project/confluent-kafka/
.. _Docker: https://docs.docker.com/get-docker/
.. _Alert: https://git.ligo.org/emfollow/userguide/-/raw/main/_static/igwn.alerts.v1_0.Alert.avsc
.. _AlertType: https://git.ligo.org/emfollow/userguide/-/raw/main/_static/igwn.alerts.v1_0.AlertType.avsc
.. _GCN: https://gcn.nasa.gov
.. _EventInfo: https://git.ligo.org/emfollow/userguide/-/raw/main/_static/igwn.alerts.v1_0.EventInfo.avsc
.. _ExternalCoincInfo: https://git.ligo.org/emfollow/userguide/-/raw/main/_static/igwn.alerts.v1_0.ExternalCoincInfo.avsc
