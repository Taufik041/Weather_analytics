from confluent_kafka import Consumer, KafkaException

# Kafka Consumer Configuration
consumer_config = {
    'bootstrap.servers': 'localhost:9092',  # Kafka broker
    'group.id': 'weather-consumer-group',   # Consumer group ID
    'auto.offset.reset': 'earliest'        # Read messages from the beginning
}

consumer = Consumer(consumer_config)

# Subscribe to the topic
consumer.subscribe(['weatherpipline'])

print("Consumer is listening for messages...")

try:
    while True:
        msg = consumer.poll(1.0)  # Poll for messages with a timeout of 1 second

        if msg is None:
            continue  # No message received, keep polling
        if msg.error():
            if msg.error().code() == KafkaException._PARTITION_EOF:
                print(f"End of partition reached {msg.topic()} {msg.partition()}")
            else:
                print(f"Error: {msg.error()}")
                break

        # Successfully received message
        print(f"Received message: {msg.value().decode('utf-8')}")

except KeyboardInterrupt:
    print("Consumer stopped.")

finally:
    # Ensure the consumer closes cleanly
    consumer.close()
