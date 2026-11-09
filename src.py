import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
# =================================================
df = pd.read_csv("data/WineQT.csv")
if "Id" in df.columns:
    df = df.drop(columns=["Id"])
print("Dataset shape:", df.shape)
print("Columns:", list(df.columns))
if "quality" not in df.columns:
    print("Error: quality column missing")
df["quality_binary"] = (df["quality"] >= 6).astype(int)
print("Binary target distribution:")
print(df["quality_binary"].value_counts())

feature_cols = [col for col in df.columns if col not in ["quality", "quality_binary"]]
X = df[feature_cols]
y = df["quality_binary"]
print("Feature matrix shape:", X.shape)
print("Target vector shape:", y.shape)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train_scaled, y_train)
