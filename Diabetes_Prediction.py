# train_and_predict.py

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
import cloudpickle

# Load dataset
dataset = pd.read_csv('diabetes.csv')
features = dataset.drop(columns='Outcome', axis=1)
target = dataset['Outcome']

# Standardize features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Split data
X_train, X_test, Y_train, Y_test = train_test_split(
    features_scaled, target, test_size=0.2, random_state=3
)

# Train Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)

# Evaluate
train_preds = model.predict(X_train)
test_preds = model.predict(X_test)

train_acc = accuracy_score(Y_train, train_preds) * 100
test_acc = accuracy_score(Y_test, test_preds) * 100

print(f"Train Accuracy: {train_acc:.2f}%")
print(f"Test Accuracy: {test_acc:.2f}%")

# Save model & scaler
with open('trained_diabetes_model.sav', 'wb') as f:
    cloudpickle.dump(model, f)

with open('standard_scaler_diabetes.sav', 'wb') as f:
    cloudpickle.dump(scaler, f)
