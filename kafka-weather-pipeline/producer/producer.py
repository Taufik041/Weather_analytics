from confluent_kafka import Producer

producer = Producer({'bootstrap.servers': 'localhost:9092'})

def ack(err, msg):
    if err is not None:
        print(f"Failed to deliver message: {err}")
    else:
        print(f"Message delivered: {msg.value()}")

while True:
    producer.produce('weatherpipline', key="key", value="test message", callback=ack)
    producer.flush()
    break