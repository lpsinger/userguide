#!/usr/bin/env python3
"""
Validate the example Kafka notices using an avro schema validator, and confirm
that deserialized notices are equivalent.
"""

from base64 import b64decode
from glob import glob
import json
import sys

import fastavro

parsed_schema = fastavro.schema.load_schema('_static/igwn.alerts.v1_0.Alert.avsc')

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
        fastavro.validation.validate(avro_alert_dict, parsed_schema, strict=True)
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
