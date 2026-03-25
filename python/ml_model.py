import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy as np

# Mock dataset for delivery delay prediction
# Features: order_size, distance, weather_risk, supplier_reliability
# Label: delay (0 or 1)
data = {
    'order_size': np.random.randint(1, 100, 1000),
    'distance': np.random.uniform(10, 1000, 1000),
    'weather_risk': np.random.uniform(0, 1, 1000),
    'supplier_reliability': np.random.uniform(0, 1, 1000),
    'delay': np.random.choice([0, 1], 1000, p=[0.7, 0.3])  # 70% no delay
}
df = pd.DataFrame(data)

# Split data
X = df[['order_size', 'distance', 'weather_risk', 'supplier_reliability']]
y = df['delay']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Logistic Regression Model
lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)
lr_pred = lr_model.predict(X_test)
lr_accuracy = accuracy_score(y_test, lr_pred)

# Random Forest Model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_pred)

print(f"Logistic Regression Accuracy: {lr_accuracy:.2f}")
print(f"Random Forest Accuracy: {rf_accuracy:.2f}")

# For dissertation: Table 4.3 and Figure 4.3
# Assuming this supports prediction accuracy metrics
print("Prediction Accuracy Computed.")
