import io
import json

from confluent_kafka import Producer
from fastavro import writer
from fastavro import parse_schema

# create kafka producer

producer_settings = {
    'bootstrap.servers': 'localhost:9092',
    'message.max.bytes': 5242880,  # 5 MB
}

producer = Producer(producer_settings)

# load and parse schema
with open('alert.avsc', 'r') as f:
    schema = json.load(f)
s = parse_schema(schema)

# load and parse alerts
events = []
event_names = ['early', 'external', 'initial', 'prelim', 'retraction', 'update']
for event_name in event_names:
    with open(f'{event_name}_alert.json', 'r') as f:
        event = json.load(f)
        events.append(event)

# write alerts
for name, event in zip(event_names, events):
    f = io.BytesIO()
    writer(f, schema, [event])
    producer.produce(topic='igwn-alerts', value=f.getvalue())


producer.flush()
