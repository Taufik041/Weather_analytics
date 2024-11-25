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
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
