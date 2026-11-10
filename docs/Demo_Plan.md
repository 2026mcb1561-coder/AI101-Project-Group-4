# Model Plan

## Project
Wine Quality Prediction Using Logistic Regression

## Objective
Build a Logistic Regression model that classifies a wine as good quality (quality >= 6) or not good (quality < 6) using its physicochemical properties.

## Model Selection

Logistic Regression is used because:

- It is a standard model for binary classification.
- It is fast to train and easy to explain.
- Its coefficients show which features influence the prediction most.

## Planned Steps

1. Load the dataset (WineQT.csv).
2. Drop the Id column, as it is only a row number.
3. Create the binary target: Good (1) if quality >= 6, otherwise Not good (0).
4. Split the data into 80% training and 20% testing sets (stratified, random_state=42).
5. Scale the features using StandardScaler (fitted on the training set only).
6. Train the Logistic Regression model (max_iter=1000, random_state=42).
7. Predict classes and probabilities on the test set.
8. Evaluate the model using accuracy, precision, recall, F1-score, ROC-AUC and PR-AUC.
9. Find the top 3 important features using the absolute coefficients.
10. Save the plots in the Output folder.

## Libraries Used

- numpy
- pandas
- matplotlib
- scikit-learn

## Expected Output

- Evaluation metrics printed in the terminal
- Confusion matrix
- ROC curve and Precision-Recall curve
- Binary quality distribution plot
- Top 3 important features

## Reproducibility

- Fixed random seed (random_state=42)
- Relative file paths
- Pinned library versions in requirements.txt
