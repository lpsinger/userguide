import io

from confluent_kafka import Consumer
from fastavro import reader

# create kafka consumer
consumer_settings = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'test',
	"auto.offset.reset": "EARLIEST",
}

consumer = Consumer(consumer_settings)
consumer.subscribe(['igwn-alerts'])

# read messages from topic
for msg in consumer.consume(num_messages=10, timeout=1):
    if msg and not msg.error():
        f = io.BytesIO(msg.value())
        f.seek(0)
        for record in reader(f):
            print(record)


consumer.unsubscribe()
consumer.close()
