import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv("creditcard.csv")

# Features
X = df.drop("Class", axis=1)

# Target
y = df["Class"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = XGBClassifier()

# Train
model.fit(X_train, y_train)

# Predict
preds = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, preds))

# Save model
joblib.dump(model, "fraud_model.pkl")