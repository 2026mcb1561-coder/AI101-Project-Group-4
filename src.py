import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, roc_curve, auc, precision_recall_curve, average_precision_score
)

data_path = "data/WineQT.csv"
output_path = "outputs/binary_wine_quality.png"

# Load & Clean Data
df = pd.read_csv(data_path)
if "Id" in df.columns:
    df = df.drop(columns=["Id"])

print("Dataset shape:", df.shape)
print("Columns:", list(df.columns))

if "quality" not in df.columns:
    print("Error: quality column missing")

# Target Binarization
df["quality_binary"] = (df["quality"] >= 6).astype(int)
print("Binary target distribution:")
print(df["quality_binary"].value_counts())

feature_cols = [col for col in df.columns if col not in ["quality", "quality_binary"]]
X = df[feature_cols]
y = df["quality_binary"]

print("Feature matrix shape:", X.shape)
print("Target vector shape:", y.shape)
