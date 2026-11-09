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

# Train/Test Split & Feature Scaling
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model Training
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)
y_prob = model.predict_proba(X_test_scaled)[:, 1]

# Metric Evaluation
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

# Curve Calculations
fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)
p_curve, r_curve, _ = precision_recall_curve(y_test, y_prob)
ap_score = average_precision_score(y_test, y_prob)

print("--- Model Evaluation Metrics ---")
print(f"Accuracy:  {acc:.4f}")
print(f"Precision: {prec:.4f}")
print(f"Recall:    {rec:.4f}")
print(f"F1 Score:  {f1:.4f}")
print(f"ROC AUC:   {roc_auc:.4f}")
print(f"PR AUC:    {ap_score:.4f}")
print("Confusion Matrix:\n", cm)

#2x2 Plot Visualizations
plt.figure(figsize=(12, 10))

# Subplot 1: Target Class Distribution
plt.subplot(2, 2, 1)
counts = df["quality_binary"].value_counts().sort_index()
plt.bar(["Low/Med (<6)", "High (>=6)"], counts.values, color=["#e74c3c", "#2ecc71"])
plt.title("Binary Quality Distribution")
plt.xlabel("Quality Class")
plt.ylabel("Count")
for i, v in enumerate(counts.values):
    plt.text(i, v + 10, str(v), ha="center", fontweight="bold")

# Subplot 2: Confusion Matrix Heatmap
plt.subplot(2, 2, 2)
plt.imshow(cm, cmap="Blues", interpolation="nearest")
plt.title("Confusion Matrix")
plt.colorbar()
plt.xticks([0, 1], ["Pred 0", "Pred 1"])
plt.yticks([0, 1], ["True 0", "True 1"])
for i in range(2):
    for j in range(2):
        plt.text(j, i, str(cm[i, j]), ha="center", va="center", color="red", fontweight="bold")

# Subplot 3: ROC Curve
plt.subplot(2, 2, 3)
plt.plot(fpr, tpr, color="#3498db", lw=2, label=f"ROC curve (AUC = {roc_auc:.2f})")
plt.plot([0, 1], [0, 1], color="navy", lw=1.5, linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend(loc="lower right")

# Subplot 4: Precision-Recall Curve
plt.subplot(2, 2, 4)
plt.plot(r_curve, p_curve, color="#9b59b6", lw=2, label=f"PR curve (AP = {ap_score:.2f})")
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("Precision-Recall Curve")
plt.legend(loc="lower left")

plt.tight_layout()
plt.savefig(output_path, dpi=300)
plt.close()
print(f"Plot saved successfully to {output_path}")
