#!/usr/bin/env python3
"""
Parse Avro schema.

Errors are output in the GNU error format
<https://www.gnu.org/prep/standards/html_node/Errors.html>.

Adapted from Leo Singer's CI scripts from TACH/GCN project.
"""
from importlib import resources
import json
import sys

from fastavro.schema import parse_schema, SchemaParseException, UnknownType
import igwn_gwalert_schema

failed = False
named_schemas = {}

for filename in ['igwn.alerts.v1_0.ExternalCoincInfo.avsc',
          'igwn.alerts.v1_0.EventInfo.avsc',
          'igwn.alerts.v1_0.AlertType.avsc',
          'igwn.alerts.v1_0.Alert.avsc']:
    try:
        with resources.open_text(igwn_gwalert_schema, filename) as f:
            schema = parse_schema(json.load(f), named_schemas, expand=True)
    except json.decoder.JSONDecodeError as e:
        print(f'{filename}:{e.lineno}:{e.colno}: error: {e.msg}', file=sys.stderr)
        failed = True
    except SchemaParseException as e:
        print(f'{filename}: error: {e.args[0]}', file=sys.stderr)
        failed = True
    except UnknownType as e:
        print(f'{filename}: error: unknown type: {e.args[0]}', file=sys.stderr)
        failed = True

if failed:
    sys.exit(1)
