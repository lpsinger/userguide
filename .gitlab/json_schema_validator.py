#!/usr/bin/env python3
"""
Parse JSON schema.

Errors are output in the GNU error format
<https://www.gnu.org/prep/standards/html_node/Errors.html>.

Adapted from Leo Singer's CI scripts from TACH/GCN project.
"""
from importlib import resources
import json
import jsonschema
import sys

import igwn_gwalert_schema

failed = False
try:
    with resources.open_text(igwn_gwalert_schema, 'igwn.alerts.v1_0.Alert.schema.json') as f:
        schema = json.load(f)
except json.decoder.JSONDecodeError as e:
    print(f'{filename}:{e.lineno}:{e.colno}: error: {e.msg}', file=sys.stderr)
    failed = True

try:
    jsonschema.Draft202012Validator.check_schema(schema)
except jsonschema.exceptions.SchemaError as e:
    print(f'igwn.alerts.v1_0.Alert.schema.json error: {e.message}', file=sys.stderr)
    failed = True

for fname in sys.argv[1:]:
    print(fname)
    with open(fname, 'r') as f:
        try:
            jsonschema.validate(json.load(f), schema)
        except jsonschema.exceptions.ValidationError as e:
            print(f'{fname}: validation error: {e.message}', file=sys.stderr)
            failed = True


if failed:
    sys.exit(1)
