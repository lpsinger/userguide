#!/usr/bin/env python
"""Convert spelling report to codeclimate format.

See https://docs.gitlab.com/ee/user/project/merge_requests/code_quality.html#implementing-a-custom-tool.
"""

from glob import iglob
from hashlib import md5
import json
import sys

errors = []
for filename in iglob('**/*.spelling', recursive=True):
    for line in open(filename):
        path, line, description = line.split(':', 2)
        line = int(line)
        error = {
            'description': f'spelling: {description}',
            'severity': 'info',
            'location': {
                'path': path,
                'lines': {
                    'begin': int(line)
                }
            }
        }
        error['fingerprint'] = md5(json.dumps(error).encode()).hexdigest()
        errors.append(error)

with open('spelling.codeclimate.json', 'w') as f:
    json.dump(errors, f)

if errors:
    sys.exit(1)
