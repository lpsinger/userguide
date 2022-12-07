Kafka Notices via SCiMMA
========================

In this section, we'll show you how to register for a SCiMMA account and then
set up credentials to receive Avro-serialized notices over Kafka. We will then
write a script to receive and parse these notices. Finally, we'll download and
parse an example notice.

Account Creation and Credential Generation
------------------------------------------

1. Sign up for an account at https://hop.scimma.org. Note that if you are not
   affiliated with any options in the identity provider list, you can use a
   `GitHub <https://github.com/>`_ or Google account.

2. Create credentials at https://my.hop.scimma.org/. Take care to save your
   credential password when you do so.

   .. important::
      You will not be able to access the password for your newly created
      credentials again after this step. If you lose it you will need to create
      new credentials.

3. Subscribe to the ``igwn.gwalert`` topic. You will find the list of topics
   available for subscribing by clicking the "Manage" button next to the
   credential you created at https://my.hop.scimma.org/

   .. note::
      It can take up to approximately an hour for a newly added subscription to
      register and become usable.

4. Finally, add your credentials to your environment with

   .. code-block:: shell-session

      hop auth add

   This will prompt you for your HOPSKOTCH_ credentials username and password.

Receiving and Parsing Notices
-----------------------------

Once you're authenticated to receive LIGO/Virgo/KAGRA notices, we can write
a function to parse them.

.. important::
   Note that mock or 'test' observations have superevent IDs that begin with
   'M', while real observations have superevent IDs that begin with 'S'. Mock
   events also list the search that found them as 'MDC', however this field is
   not present in retraction alerts so it is best to check the first character
   of the superevent ID to distinguish between the two.

.. testcode::

    from io import BytesIO
    from pprint import pprint

    from astropy.table import Table
    import astropy_healpix as ah
    from hop import stream
    import numpy as np

    def parse_notice(record):
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
        skymap_bytes = record.get('event', {}).pop('skymap')
        if skymap_bytes:
            # Parse skymap directly and print most probable sky location
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

    with stream.open('kafka://kafka.scimma.org/igwn.gwalert', 'r') as s:
        for message in s:
            parse_notice(message.content[0])

When you run this script you should receive a sample LIGO/Virgo/KAGRA notice
every hour. The output will be the same as the output in the
offline-testing-avro_ section below.

.. _offline-testing-avro:

Offline Testing
---------------

Sample files are available to download at any time for testing responses to
notices without needing to wait for the one-per-hour example. 

.. code-block:: shell-session

    $ curl -O https://emfollow.docs.ligo.org/userguide/_static/MS181101ab-preliminary.avro

Now you can parse the Avro packet using the code we wrote above.

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

    import fastavro

    # Read the file in bytes mode and then parse it
    with open('MS181101ab-preliminary.avro', 'rb') as fo:
        reader = fastavro.reader(fo)
        # LIGO/Virgo/KAGRA notices will only ever contain one record
        record = next(reader)

    parse_notice(record)

Running this should produce the following output:

.. testoutput::

   Most probable sky location (RA, Dec) = (194.30419921874997, -17.856895095545468)
   Distance = 39.76999609489013 +/- 8.308435058808886
   Record:
   {'alert_type': 'PRELIMINARY',
    'event': {'classification': {'BBH': 0.03,
                                 'BNS': 0.95,
                                 'NSBH': 0.01,
                                 'Terrestrial': 0.01},
              'far': 9.11069936486e-14,
              'group': 'CBC',
              'instruments': ['H1', 'L1', 'V1'],
              'pipeline': 'gstlal',
              'properties': {'HasMassGap': 0.01,
                             'HasNS': 0.95,
                             'HasRemnant': 0.91},
              'search': 'MDC',
              'time': '2018-11-01T22:22:46.654Z'},
    'external_coinc': None,
    'superevent_id': 'MS181101ab',
    'time_created': '2018-11-01T22:34:49Z',
    'urls': {'gracedb': 'https://example.org/superevents/MS181101ab/view/'}}

.. testcleanup::

    os.chdir(old_dir)

Examples
--------

Below are some sample Avro alerts that can be used for testing purposes.

* :download:`MS181101ab-earlywarning.avro </_static/MS181101ab-earlywarning.avro>`
* :download:`MS181101ab-preliminary.avro </_static/MS181101ab-preliminary.avro>`
* :download:`MS181101ab-initial.avro </_static/MS181101ab-initial.avro>`
* :download:`MS181101ab-update.avro </_static/MS181101ab-update.avro>`
* :download:`MS181101ab-retraction.avro </_static/MS181101ab-retraction.avro>`

.. _confluent-kafka: https://pypi.org/project/confluent-kafka/
.. _Docker: https://docs.docker.com/get-docker/
.. _fastavro: https://pypi.org/project/fastavro/
.. _Alert: https://git.ligo.org/emfollow/userguide/-/raw/main/_static/igwn.alerts.v1_0.Alert.avsc
.. _AlertType: https://git.ligo.org/emfollow/userguide/-/raw/main/_static/igwn.alerts.v1_0.AlertType.avsc
.. _HOPSKOTCH: https://scimma.org/hopskotch.html
.. _EventInfo: https://git.ligo.org/emfollow/userguide/-/raw/main/_static/igwn.alerts.v1_0.EventInfo.avsc
.. _ExternalCoincInfo: https://git.ligo.org/emfollow/userguide/-/raw/main/_static/igwn.alerts.v1_0.ExternalCoincInfo.avsc
