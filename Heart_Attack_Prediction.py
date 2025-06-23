import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
import cloudpickle

# Load Cleveland dataset from UCI
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"
column_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
                'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']
data = pd.read_csv(url, names=column_names, na_values='?')

# Data preprocessing
# Convert target to binary (0 = no disease, 1 = disease)
data['target'] = (data['target'] > 0).astype(int)

# Handle missing values (thal and ca have missing values in Cleveland data)
data = data.dropna()

# Separate features and target
features = data.drop(columns='target')
target = data['target']

# Print group statistics
print("Mean values by target class:")
print(data.groupby('target')[['thalach', 'ca']].mean())

# Standardize features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Split data
X_train, X_test, Y_train, Y_test = train_test_split(
    features_scaled, target, 
    test_size=0.2, 
    random_state=3, 
    stratify=target
)

# Train Logistic Regression
model = LogisticRegression(
    C=100,
    max_iter=5000, 
    solver='lbfgs',
    class_weight='balanced'  # Handles class imbalance
)
model.fit(X_train, Y_train)

# Evaluate
train_preds = model.predict(X_train)
test_preds = model.predict(X_test)

train_acc = accuracy_score(Y_train, train_preds) * 100
test_acc = accuracy_score(Y_test, test_preds) * 100

print("\nModel Performance:")
print(f"✅ Train Accuracy: {train_acc:.2f}%")
print(f"✅ Test Accuracy: {test_acc:.2f}%")
print("\nClassification Report:")
print(classification_report(Y_test, test_preds))

# Save model and scaler
with open('trained_heart_model.sav', 'wb') as f:
    cloudpickle.dump(model, f)

with open('standard_scaler_heart.sav', 'wb') as f:
    cloudpickle.dump(scaler, f)
