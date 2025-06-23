import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import cloudpickle

# Load dataset
dataset = pd.read_csv('cancer.csv')

# Drop non-feature columns
features = dataset.drop(['index', 'Patient Id', 'Level'], axis=1)
target = dataset['Level']

# Encode target (Low:0, Medium:1, High:2)
label_encoder = LabelEncoder()
target_encoded = label_encoder.fit_transform(target)

# Standardize features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Train/test split
X_train, X_test, Y_train, Y_test = train_test_split(
    features_scaled, target_encoded, test_size=0.2, random_state=3
)

# Train Multinomial Logistic Regression model
model = LogisticRegression(
    multi_class='multinomial',
    solver='lbfgs', 
    max_iter=1000,
    C=1.0  
)
model.fit(X_train, Y_train)

# Predict and evaluate
train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

print(f"Train Accuracy: {accuracy_score(Y_train, train_pred)*100:.2f}%")
print(f"Test Accuracy: {accuracy_score(Y_test, test_pred)*100:.2f}%")

# Save model and scaler
with open('trained_lung_cancer_model.sav', 'wb') as f:
    cloudpickle.dump(model, f)

with open('standard_scaler_cancer.sav', 'wb') as f:
    cloudpickle.dump(scaler, f)
