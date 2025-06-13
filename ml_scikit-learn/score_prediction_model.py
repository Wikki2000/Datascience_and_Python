#!/usr/bin/python3
"""Train Linear Regression Model to Predict Student Scores."""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


data_csv_file = "linear_hours_scores.csv"

df = pd.read_csv(data_csv_file)

# ================== Step 2: Visualize Data ================== #
plt.scatter(
    df["Hours"], df["Scores"], label="Data Points", marker="*", color="blue")
plt.xlabel("Hours")
plt.ylabel("Scores")
plt.title("Scores vs. Hours")
plt.savefig("score_vs_hours.png", dpi=300, bbox_inches='tight')

# ================== Step 3: Train/Test Split ================== #
features = ["Hours"]  # Features (must be 2D for sklearn)
target = "Scores"

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ================== Step 4: Baseline Model (Mean) ================== #
y_mean = y_train.mean()
y_pred_baseline = [y_mean] * len(y_test)

baseline_mae = mean_absolute_error(y_test, y_pred_baseline)
print(f"Baseline MAE: {baseline_mae:.2f}")

# ================== Step 5: Linear Regression ================== #
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(y_pred)

model_mae = mean_absolute_error(y_test, y_pred)
print(f"Model MAE: {model_mae:.2f}")

# ================== Step 6: Compare Results ================== #
print("Baseline Prediction:", y_mean)
print("Linear Model Coefficient (slope):", model.coef_[0])
print("Linear Model Intercept:", model.intercept_)

if model_mae < baseline_mae:
    print("✅ Model improves on the baseline!")
else:
    print("⚠️ Model does not improve on the baseline.")
