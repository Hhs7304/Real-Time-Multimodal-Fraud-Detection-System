from kafka import KafkaConsumer
import json
import joblib
import pandas as pd

# Load trained fraud detection model
model = joblib.load("fraud_model.pkl")

# Kafka consumer setup
consumer = KafkaConsumer(
    'fraud-topic',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Consumer started... Waiting for transactions...\n")

# Listen continuously
for message in consumer:

    transaction = message.value

    print("Received Transaction:", transaction)

    # Convert transaction to DataFrame
    df = pd.DataFrame([transaction])

    # Predict fraud
    prediction = model.predict(df)[0]

    # Fraud probability
    probability = model.predict_proba(df)[0][1]

    # Display result
    if prediction == 1:
        print(f"🚨 FRAUD DETECTED | Risk Score: {probability:.2f}\n")
    else:
        print(f"✅ SAFE TRANSACTION | Risk Score: {probability:.2f}\n")