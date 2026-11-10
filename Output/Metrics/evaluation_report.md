
The model was evaluated on the test set (20% of the data).

| Model | Accuracy | Precision | Recall | F1 Score | ROC AUC | PR AUC |
|-------|----------|-----------|--------|----------|---------|--------|
| Logistic Regression | 0.7773 | 0.8017 | 0.7823 | 0.7918 | 0.8237 | 0.8428 |

**Interpretation:**
- **Accuracy (0.7773):** about 77.7% of the test wines were classified correctly.
- **Precision (0.8017):** when the model predicts a wine as good quality, it is correct about 80.2% of the time.
- **Recall (0.7823):** the model finds about 78.2% of the wines that are truly good quality.
- **F1-score (0.7918):** a balance of precision and recall, close to 0.79.
- **ROC AUC (0.8237):** the model separates good and not-good wines well across different thresholds.
- **PR AUC (0.8428):** the model keeps good precision and recall for the good-quality class.
