FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install pandas numpy scikit-learn xgboost fastapi uvicorn joblib kafka-python

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]