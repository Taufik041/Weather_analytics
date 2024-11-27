import json
from confluent_kafka import Consumer, KafkaException, KafkaError
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import yaml
from datetime import datetime


# Load secrets from secrets.yaml
def load_secrets(file_path="kafka-weather-pipeline/secrets.yaml"):
    """Load secrets from YAML file."""
    with open(file_path, "r") as f:
        return yaml.safe_load(f)


# SQLAlchemy Setup
def setup_database(database_url):
    """Set up the database engine and sessionmaker."""
    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)
    return engine, Session


# Define WeatherData model
Base = declarative_base()

class WeatherData(Base):
    """Weather data model to map to the weather_data table."""
    __tablename__ = 'weather_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String)
    temperature = Column(Float)
    humidity = Column(Float)
    description = Column(String)
    timestamp = Column(Integer)  # To be converted to datetime when saving


# Create the table if not exists
def create_tables(engine):
    """Create tables in the database."""
    Base.metadata.create_all(engine)


# Kafka Consumer Configuration
def create_kafka_consumer(consumer_config):
    """Create and return a Kafka consumer."""
    return Consumer(consumer_config)


# Save weather data to PostgreSQL
def save_to_database(session, weather_data):
    """Save parsed weather data to the database."""
    timestamp = datetime.fromtimestamp(weather_data['timestamp'])
    new_data = WeatherData(
        city=weather_data['city'],
        temperature=weather_data['temperature'],
        humidity=weather_data['humidity'],
        description=weather_data['description'],
        timestamp=timestamp  # Storing datetime object instead of raw integer
    )
    session.add(new_data)
    session.commit()


def main():
    """Main Kafka consumer loop."""
    # Load secrets and database setup
    secrets = load_secrets()
    engine, Session = setup_database(secrets['postgres_url'])
    
    # Create tables in the database (if not already created)
    create_tables(engine)
    
    # Kafka Consumer setup
    consumer_config = {
        'bootstrap.servers': secrets['kafka_broker'],
        'group.id': 'weather_consumer_group',
        'auto.offset.reset': 'earliest'
    }
    consumer = create_kafka_consumer(consumer_config)
    
    # Subscribe to the Kafka topic
    consumer.subscribe([secrets['kafka_topic']])
    
    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            
            if msg is None:
                continue  # No new message, keep polling
            
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue  # End of partition, no action needed
                else:
                    raise KafkaException(msg.error())  # Unexpected error
            
            # Parse the message and save it to the database
            weather_data = json.loads(msg.value().decode('utf-8'))
            
            # Insert the weather data into the database
            with Session() as session:
                save_to_database(session, weather_data)
            
    except KeyboardInterrupt:
        print("Kafka consumer interrupted.")
    
    finally:
        consumer.close()


if __name__ == "__main__":
    main()
