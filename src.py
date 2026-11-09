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
