# Real-Time-Multimodal-Fraud-Detection-System


# Real-Time Multimodal Fraud Detection System

## Overview

A real-time AI-powered fraud detection platform that processes streaming transaction events using Apache Kafka and performs instant fraud prediction using an XGBoost machine learning model.

The system demonstrates distributed event-driven architecture, real-time inference pipelines, Docker-based infrastructure, and machine learning integration.

---

# Architecture

```text
Producer
   ↓
Apache Kafka
   ↓
Kafka Consumer
   ↓
XGBoost Fraud Detection Model
   ↓
Fraud Prediction Output
```

---

# Features

* Real-time transaction streaming using Apache Kafka
* Event-driven producer-consumer architecture
* Fraud prediction using XGBoost
* Dockerized infrastructure
* Scalable distributed pipeline foundation
* Continuous real-time inference workflow
* Streaming transaction simulation

---

# Tech Stack

| Category         | Technologies                  |
| ---------------- | ----------------------------- |
| Programming      | Python                        |
| Machine Learning | XGBoost, Scikit-learn, Pandas |
| Streaming        | Apache Kafka                  |
| Backend          | FastAPI                       |
| DevOps           | Docker, Docker Compose        |
| Data Processing  | NumPy                         |

---

# Project Structure

```text
fraud-detection-system/
│
├── app.py
├── producer.py
├── consumer.py
├── train_model.py
├── fraud_model.pkl
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
│
└── README.md
```

---

# Workflow Explanation

## 1. Producer

The producer continuously generates transaction events and sends them into Kafka.

Example transaction:

```json
{
  "Time": 12345,
  "Amount": 5422,
  "V1": 0.23,
  "V2": -1.45
}
```

---

## 2. Kafka Broker

Kafka acts as the real-time message broker.

It stores transaction events inside a topic:

```text
fraud-topic
```

---

## 3. Consumer

The Kafka consumer continuously listens for new transaction events.

When a transaction arrives:

```text
Receive transaction
↓
Convert to DataFrame
↓
Send to ML model
↓
Generate fraud prediction
```

---

## 4. Fraud Detection Model

The system uses an XGBoost classification model trained on transaction fraud data.

Prediction Output:

```text
SAFE TRANSACTION
```

or

```text
FRAUD DETECTED
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <your-repo-link>
cd fraud-detection-system
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Docker Setup

## Build Docker Image

```bash
docker build -t fraud-api .
```

---

## Run Docker Container

```bash
docker run -p 8000:8000 fraud-api
```

---

# Kafka Setup

## Start Kafka Infrastructure

```bash
docker compose up -d
```

---

## Verify Containers

```bash
docker ps
```

---

# Running the System

## Step 1 — Run Consumer

```bash
python consumer.py
```

---

## Step 2 — Run Producer

```bash
python producer.py
```

---

# Example Output

## Producer Output

```text
Transaction Sent
```

---

## Consumer Output

```text
Received Transaction
SAFE TRANSACTION | Risk Score: 0.02
```

or

```text
FRAUD DETECTED | Risk Score: 0.91
```

---

# Machine Learning Pipeline

## Model Training

The fraud detection model is trained using:

* XGBoost Classifier
* Credit Card Fraud Dataset
* Scikit-learn preprocessing pipeline

---

## Real-Time Inference

Streaming transactions are processed instantly:

```text
Kafka Event
↓
Consumer
↓
ML Prediction
↓
Fraud Classification
```

---

# Future Improvements

* Redis feature store integration
* SHAP explainability
* CNN-based document fraud detection
* MLflow model registry
* Kubernetes deployment
* Monitoring dashboards
* Multi-service orchestration

---

# Resume Highlights

* Built a real-time AI-powered fraud detection system using Kafka and XGBoost.
* Developed an event-driven streaming pipeline with producer-consumer architecture.
* Integrated machine learning inference into real-time transaction workflows.
* Containerized services using Docker for scalable deployment.

---

# Skills Demonstrated

* Distributed Systems
* Event-Driven Architecture
* Machine Learning Engineering
* Real-Time Streaming
* Docker & Containerization
* Kafka Messaging Systems
* Backend Development
* AI Inference Pipelines

---

