#!/usr/bin/env python3
"""
Parse Avro schema.

Errors are output in the GNU error format
<https://www.gnu.org/prep/standards/html_node/Errors.html>.

Adapted from Leo Singer's CI scripts from TACH/GCN project.
"""
from json.decoder import JSONDecodeError
import sys

from fastavro.schema import load_schema, SchemaParseException, UnknownType

failed = False

for filename in sys.argv[1:]:
    try:
        load_schema(filename)
    except JSONDecodeError as e:
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
