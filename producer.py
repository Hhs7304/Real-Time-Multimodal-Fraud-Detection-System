from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:

    transaction = {
        "Time": random.uniform(0, 50000),
        "Amount": random.uniform(1, 10000)
    }

    # Generate V1 to V28
    for i in range(1, 29):
        transaction[f"V{i}"] = random.uniform(-5, 5)

    producer.send("fraud-topic", transaction)

    print("Transaction Sent")

    time.sleep(5)