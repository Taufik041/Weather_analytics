# Real-Time Weather Analytics Pipeline 🌦️

## **Overview**
This project is a real-time weather analytics pipeline built using **Kafka** and **Python**. It fetches live weather data from the OpenWeatherMap API, produces it to a Kafka topic, and consumes it for downstream processing. Additionally, the project stores weather data in a **PostgreSQL** database for persistent storage and further analysis.

---

## **Features**
- Fetches real-time weather data using the OpenWeatherMap API.
- Publishes weather data to Kafka topics using a producer script.
- Consumes the weather data from Kafka topics using a consumer script.
- Saves weather data to a PostgreSQL database for storage and analysis.
- Modular design for easy extension and scalability.

---

## **Technologies Used**
- **Kafka**: Real-time messaging system for producing and consuming data.
- **Python**:
  - `confluent-kafka`: For Kafka producer and consumer.
  - `requests`: To fetch data from the OpenWeatherMap API.
  - `json`: To serialize and deserialize messages.
  - `sqlalchemy`: For database interaction with PostgreSQL.
  - `psycopg2`: PostgreSQL database adapter for Python.
- **OpenWeatherMap API**: To fetch real-time weather data.
- **PostgreSQL**: For storing weather data.

---

## **Architecture**
1. **Producer**:
   - Fetches weather data for a specified city from the OpenWeatherMap API.
   - Sends the data to a Kafka topic (`weatherAnalytics`).
   - Weather data includes: `city`, `temperature`, `humidity`, `description`, `timestamp`.

2. **Consumer**:
   - Listens to the Kafka topic.
   - Processes and displays the weather data in real time.
   - Saves the weather data to a PostgreSQL database for storage.

3. **Database**:
   - PostgreSQL database to store weather data.
   - Weather data includes: `city`, `temperature`, `humidity`, `description`, `timestamp`.

---

## **Setup and Usage**

### **1. Prerequisites**
- Python (3.8+)
- Kafka installed and running locally.
- PostgreSQL installed and running.
- OpenWeatherMap API key.
- Access to a GitHub repository for version control.

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

### **4. Set Up PostgreSQL**
- Create a PostgreSQL database to store weather data.
- Add your PostgreSQL credentials (e.g., `postgres_url`) in a `secrets.yaml` file. This file should be added to `.gitignore` to avoid exposing sensitive information.

### **5. Start Kafka Services**
- Start zookeeper:
```bash
./bin/windows/zookeeper-server-start.bat ./config/zookeeper.properties
```
- Start Kafka:
```bash
./bin/windows/kafka-server-start.bat ./config/server.properties
```

### **6. Create Kafka Topic**
```bash
bin/kafka-topics.sh --create --topic weatherpipline --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

### **7. Run the Kafka Producer**
```PowerShell
python kafka-weather-pipeline/producer/producer.py
```

### **8. Run the Kafka Consumer**
```PowerShell
python kafka-weather-pipeline/consumer/consumer.py
```

### **9. Run the Kafka Consumer with Database Integration**
Ensure that the `secrets.yaml` file is configured correctly for your PostgreSQL database connection. Then, run the consumer which will listen to Kafka and save weather data to the database:
```PowerShell
python kafka-weather-pipeline/consumer/consumer_with_db.py
```

### **Sample Output**

**Producer**
```css
Fetching weather data...
Message delivered: {"city": "London", "temperature": 12.3, "humidity": 78, "description": "clear sky", "timestamp": 1701112345}
```

**Consumer**
```css
Consumer is listening for messages...
Received message: {"city": "London", "temperature": 12.3, "humidity": 78, "description": "clear sky", "timestamp": 1701112345}
```

**Consumer with Database**
```css
Consumer is listening for messages...
Received message: {"city": "London", "temperature": 12.3, "humidity": 78, "description": "clear sky", "timestamp": 1701112345}
Weather data saved to database.
```

---

## **Next Steps and Future Improvements**
- Add more cities and weather metrics.
- Set up a periodic task scheduler to fetch weather data at regular intervals.
- Expand the consumer to process data in various ways (e.g., anomaly detection, reporting).
- Integrate with a front-end dashboard to visualize real-time weather data.

---

Let me know if you'd like to add more details or change any part!