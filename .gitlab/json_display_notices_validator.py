#!/usr/bin/env python3
"""
Validate the example Kafka notices using an avro schema validator, and confirm
that deserialized notices are equivalent.
"""

from base64 import b64decode
from glob import glob
import json
import sys

failed = False

for filename in glob('_static/MS181101ab-*_displayexample.json'):
    original_filename = filename.replace('_displayexample', '')
    # Open display example
    with open(filename, 'r') as fo:
        display_alert_dict = json.load(fo)

    # Open non-display example
    with open(original_filename, 'r') as fo:
        original_alert_dict = json.load(fo)

    if original_alert_dict.get('event', {}):
        if not display_alert_dict.get('event', {}):
            print(f'{filename} does not appear to be a display version of {original_filename}', file=sys.stderr)
            failed = True
            continue

        # Truncate skymap to same length as the display example
        original_alert_dict['event']['skymap'] = original_alert_dict['event']['skymap'][:len(display_alert_dict['event']['skymap'][:-3])] + '...'

    if display_alert_dict != original_alert_dict:
        print(f'{filename} does not appear to be a display version of {original_filename}', file=sys.stderr)
        failed = True

if failed:
    sys.exit(1)
