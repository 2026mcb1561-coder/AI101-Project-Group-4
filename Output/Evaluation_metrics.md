
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
  # Key Observations and Insights:
  1) Class Distribution and Skew:
     The dataset exhibits moderate class imbalance, with the majority of samples falling into average quality ratings (5 and 6), while extreme values (ratings of 3,       4, 7, and 8) are sparse. As a result, the highest recall (TP/TP+FN) is for average rated wines.
  2) Classification Error Patterns:
     Misclassifications predominantly occur between adjacent quality tiers (e.g., predicting a quality score of 5 as 6). Large margin errors (e.g., predicting a 3 as      a 7) are practically non-existent.
  3) Feature Importance
       Feature          Regression Coefficient(Standardized)              Impact on Wine Quality
     I. Alcohol                 +0.3082                                  Very High Positive Impact
     II. Sulphates              +0.1553                                   High Positive Impact
     III. Citric Acid           +0.0043                                    Minor Positive Impact
     IV.  Residual Sugar        +0.0230                                     Moderate Positive Impact
     V. Free SO₂                +0.0461                                     Moderate Positive Impact
     VI. Fixed acidity          +0.0250                                     Moderate Positive Impact
     VII. pH                    -0.0638                                     Moderate Negative Impact
     VIII. Chlorides            -0.0882                                     Moderate Negative Impact
     IX.  Total   SO₂           -0.1084                                     High Negative Impact
     X.   Density               -0.0335                                     Moderate Negative Impact
     XI. Volatile acidity       -0.1944                                      High Negative Impact
         Standardized Model Intercept: +5.6360        
