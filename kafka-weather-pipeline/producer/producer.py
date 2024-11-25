import requests
from confluent_kafka import Producer
import time
import json

# Kafka Producer Configuration
producer_config = {
    'bootstrap.servers': 'localhost:9092'  # Kafka broker
}

producer = Producer(producer_config)

# OpenWeatherMap API Configuration
API_KEY = "641db5a7827eaef1218207e0e6715304"  # Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
CITY_NAME = "London"  # Replace with your desired city

def fetch_weather_data():
    """Fetch weather data from the OpenWeatherMap API."""
    params = {
        'q': CITY_NAME,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'],
            'timestamp': int(time.time())
        }
        return weather_data
    else:
        print(f"Failed to fetch weather data: {response.status_code}")
        return None

def delivery_report(err, msg):
    """Delivery report for Kafka producer."""
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered: {msg.value().decode('utf-8')}")

# Main loop
while True:
    weather_data = fetch_weather_data()
    if weather_data:
        # Convert data to JSON
        weather_json = json.dumps(weather_data)
        # Send data to Kafka topic
        producer.produce(
            'weatherpipline', 
            key=str(weather_data['timestamp']), 
            value=weather_json, 
            callback=delivery_report
        )
        producer.flush()
    time.sleep(100)  # Fetch and send data every 100 seconds
