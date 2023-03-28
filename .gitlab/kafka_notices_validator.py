#!/usr/bin/env python3
"""
Validate the example Kafka notices using an avro schema validator, and confirm
that deserialized notices are equivalent.
"""

from base64 import b64decode
from glob import glob
from importlib import resources
import json
import sys

import fastavro
import igwn_gwalert_schema


# The order does not matter other than the Alert schema must be loaded last
# because it references the other schema. All of the schema are saved in
# named_schemas, but we only need to save a reference to the the Alert
# schema to write the packet.
# NOTE Specifying expand=True when calling parse_schema is okay when only
# one schema contains references to other schema, in our case only the
# alerts schema contains references to other schema. More complicated
# relationships between schema though can lead to behavior that does not
# conform to the avro spec, and a different method will need to be used to
# load the schema. See https://github.com/fastavro/fastavro/issues/624 for
# more info.
named_schemas = {}
for s in ['igwn.alerts.v1_0.ExternalCoincInfo.avsc',
          'igwn.alerts.v1_0.EventInfo.avsc',
          'igwn.alerts.v1_0.AlertType.avsc',
          'igwn.alerts.v1_0.Alert.avsc']:
    with resources.open_text(igwn_gwalert_schema, s) as f:
        schema = fastavro.schema.parse_schema(json.load(f), named_schemas,
                                              expand=True)

failed = False

for filename in glob('_static/*.avro'):
    json_filename = filename.replace('.avro', '.json')
    # Load avro
    with open(filename, 'rb') as fo:
        reader = fastavro.reader(fo)
        avro_alert_dict, *rest = iter(reader)
    if rest:
        print(f'{filename} contains more than 1 record', file=sys.stderr)
        failed = True
        continue

    # Validate avro record against schema
    try:
        fastavro.validation.validate(avro_alert_dict, schema, strict=True)
    except fastavro._validate_common.ValidationError as e:
        print(f'{filename} failed validation with error {e.errors}', file=sys.stderr)
        failed = True
        continue
    # Load json
    with open(json_filename, 'r') as fo:
        json_alert_dict = json.load(fo)

    if avro_alert_dict.get('event', {}):
        # Decode base64 encoded skymap in json notice
        json_alert_dict['event']['skymap'] = b64decode(json_alert_dict['event']['skymap'])

    if avro_alert_dict.get('external_coinc', {}):
        # Decode base64 encoded skymap in json notice
        json_alert_dict['external_coinc']['combined_skymap'] = b64decode(json_alert_dict['external_coinc']['combined_skymap'])

    if avro_alert_dict != json_alert_dict:
        print(f'Deserialized {filename} does not equal deserialized {json_filename}', file=sys.stderr)
        failed = True

if failed:
    sys.exit(1)
