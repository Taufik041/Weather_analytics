# Real-Time Weather Analytics Pipeline 🌦️

## **Overview**
This project is a real-time weather analytics pipeline built using **Kafka** and **Python**. It fetches live weather data from the OpenWeatherMap API, produces it to a Kafka topic, and consumes it for downstream processing.

---

## **Features**
- Fetches real-time weather data using the OpenWeatherMap API.
- Publishes weather data to Kafka topics using a producer script.
- Consumes the weather data from Kafka topics using a consumer script.
- Modular design for easy extension and scalability.

---

## **Technologies Used**
- **Kafka**: Real-time messaging system for producing and consuming data.
- **Python**:
  - `confluent-kafka`: For Kafka producer and consumer.
  - `requests`: To fetch data from the OpenWeatherMap API.
  - `json`: To serialize and deserialize messages.
- **OpenWeatherMap API**: To fetch real-time weather data.

---

## **Architecture**
1. **Producer**:
   - Fetches weather data for a specified city from the OpenWeatherMap API.
   - Sends the data to a Kafka topic (`weatherAnalytics`).

2. **Consumer**:
   - Listens to the Kafka topic.
   - Processes and displays the weather data in real time.

---

## **Setup and Usage**

### **1. Prerequisites**
- Python (3.8+)
- Kafka installed and running locally.
- OpenWeatherMap API key.

### **2. Clone the Repository**
```bash
git clone https://github.com/Taufik041/Weather_analytics.git
cd Weather_analytics
```

### **3. Install Dependencies**
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

### **4. Start Kafka Services**
- Start zookeeper:
```bash
./bin/windows/zookeeper-server-start.bat ./config/zookeeper.properties
```
- Start Kafka:
```bash
./bin/windows/kafka-server-start.bat ./config/server.properties
```


### **5. Create Kafka Topic**
```bash
bin/kafka-topics.sh --create --topic weatherpipline --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

### **6. Run the Kafka Producer**
```PowerShell
python kafka-weather-pipeline/producer/producer.py
```

### **7. Run the Kafka Consumer**
```PowerShell
python kafka-weather-pipeline/consumer/consumer.py
```

### **Sample Output**

-**Producer**
```css
Fetching weather data...
Message delivered: {"city": "London", "temperature": 12.3, "humidity": 78, "description": "clear sky", "timestamp": 1701112345}
```

-**Consumer**
```css
Consumer is listening for messages...
Received message: {"city": "London", "temperature": 12.3, "humidity": 78, "description": "clear sky", "timestamp": 1701112345}
```