# Wine Quality Predictor

Predicts the quality score (0-10) of Portuguese "Vinho Verde" wine from its physicochemical properties (pandas, matplotlib, scikit-learn).

![AI101 Mini-Project](https://img.shields.io/badge/AI101-Mini--Project-blue) ![Group](https://img.shields.io/badge/Group-4-lightblue) ![Python](https://img.shields.io/badge/Python-3.10%2B-green)

---

## 1. Team and Roles

**Team number - 4:** 

| Member | Entry No. | GitHub Handle | Role |
|--------|-----------|---------------|------|
| Sajid Hasan | 2026MCB1561 | https://github.com/2026MCB1561-coder | Execution Lead |
| Harshit Kumar Agrawal | 2026AIB1042 | https://github.com/2026AIB1042-alt| Documentation Lead|
| Shwet Purushottam Chandankar | 2026EEB1414| https://github.com/Shwetchandankar001 | Video lead |
| Yashnoor Singh | 2026EEB1427 | https://github.com/2026EEB1427 | PPT lead |

All four members contributed code from their own GitHub accounts (see the commit history).

---

## 2. Project Description

**Problem:** Wine quality is normally judged by human experts, which is slow and subjective. We build a machine learning model that predicts a wine's quality score from lab measurements (acidity, sugar, alcohol, etc.). This could help producers check quality consistently and find which properties matter most.

**Task type:** BINARY CLASSIFICATION (predict whether a wine is "Good" or "Bad")

**Approach (pipeline):**

```
Load data  ->  Clean and explore (EDA)  ->  Train/test split  ->  Train model(s)  ->  Evaluate  ->  Save plots
```

1. Load the wine dataset from `data/`.
2. Check for missing values and duplicates, and explore the data with plots.
3. Split the data into 80% training and 20% test sets.
4. Train a Logistic Regression model (binary classifier: Good vs. Bad quality) on the scaled features.
5. Evaluate on the test set using accuracy, ROC-AUC, and a classification report (precision, recall and F1-score).
6. Save the result plots into `outputs/`.

---

## 3. Dataset

- **Name:** Wine Quality dataset (Vinho Verde, Portugal)
- **Source:** UCI Machine Learning Repository, https://archive.ics.uci.edu/dataset/186/wine+quality
- **Citation:** P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis. *Modeling wine preferences by data mining from physicochemical properties.* Decision Support Systems, 47(4):547-553, 2009. Licensed CC BY 4.0.
- **File used:** `WineQT.csv` (stored in `data/`)
- **Size:** 1143 rows, 13 columns (11 input features, the target `quality`, and an `Id` column that the code drops)
- **Missing values:** None found (checked with `df.isnull().sum()`).

| Column | Type | Description |
|--------|------|-------------|
| fixed acidity | Input | Non-volatile acids in the wine |
| volatile acidity | Input | Acetic acid content |
| citric acid | Input | Citric acid content |
| residual sugar | Input | Sugar left after fermentation |
| chlorides | Input | Salt content |
| free sulfur dioxide | Input | Free SO2 |
| total sulfur dioxide | Input | Total SO2 |
| density | Input | Density of the wine |
| pH | Input | Acidity level |
| sulphates | Input | Sulphate content |
| alcohol | Input | Alcohol percentage |
| **quality** | **Target** | Score from 0 to 10, given by wine experts |

---

## 4. Project Structure

```
AI101-Project-Group-4/
├── Output/
|   ├── Evaluation_metrics.md                               
│   ├── binary_quality_distribution.png
│   ├── confusion_matrix.png
│   ├── precision_recall_curve.png
│   └── roc_curve.png
├── data/
│   └── WineQT.csv                           # dataset used by the code
├── docs/                                    # supporting files
├── Wine Quality Binary Classification ...   # 5-slide presentation (.pptx)
├── README.md
├── requirements.txt                         # libraries and pinned versions
└── src.py                                   # main script: run this file
```

---

## 5. Setup

**Python version:** Python 3.10 or higher (tested on Python 3.15.0rc2 on MacOS).

**Step 1: Clone the repository**

```bash
git clone https://github.com/2026mcb1561-coder/AI101-Project-Group-4.git
cd AI101-Project-Group-4
```

**Step 2: Create a virtual environment**

```bash
 a) python -m venv venv  ( In case your terminal does not identify python use py instead of 'python'.)
  b) Grant Permission in Your Current Session (Recommended)
      Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

**Step 3: Activate the virtual environment**

- Windows:
  ```bash
    .\venv\Scripts\Activate.ps1
  ```
- macOS / Linux:
  ```bash
  source venv/bin/activate
  ```

**Step 4: Install the libraries**

```bash
pip install -r requirements.txt
```

Libraries used (exact versions pinned in `requirements.txt`): numpy, pandas, matplotlib, scikit-learn 

---

## 6. How to Run

Run these commands in order from the project's main folder:

1. Make sure the virtual environment is activated (Setup, Step 3).
2. Run the main script:
   ```bash
   python src.py (( In case your terminal does not identify python use py instead of 'python'.)
   ```
3. The script loads `data/WineQT.csv`, trains the model, prints the evaluation scores, and saves plots in `outputs/`.
4. Expected runtime: under 20 second.



The data file is included in the repository, so no download step is needed. All paths in the code are relative.

---

## 7. Expected Output and Results

When the code runs correctly you should see something like this:

<img width="3600" height="3000" alt="output" src="https://github.com/user-attachments/assets/fdedbcc1-53c2-4747-ae1b-0febb3a0aa5d" />




**Key results (on the test set):**

| Model | Accuracy | Precision | Recall | F1 Score | ROC AUC | PR AUC |
|-------|----------|-----------|--------|----------|---------|--------|
| Logistic Regression | 0.7773 | 0.8017 | 0.7823 | 0.7918 | 0.8237 | 0.8428 |

**Files created in `outputs/`:**

- `confusion_matrix.png`: counts of correct and wrong predictions for each class on the test set
- `precision_recall_curve.png`: precision against recall for the High quality class, with the PR AUC (average precision) score
- `roc_curve.png`: true positive rate against false positive rate, with the ROC AUC score
- `binary_quality_distribution.png`: number of wines in each class, Low/Medium (quality < 6) and High (quality >= 6)

The Logistic Regression model reached an accuracy of 0.7773 and a ROC AUC of 0.8237 on the test set. 

---

## 8. Links

- **Slides (5):** https://gamma.app/docs/Wine-Quality-Binary-Classification-Project-2kkf6tcxd4vd1qr
- **Video (max 5:00):** [FILL: paste the unlisted YouTube/Drive link, or the file path if uploaded to this repo]

---

## 9. AI-use Disclosure

- **Claude:** used to learn and understand the project requirements, GitHub, virtual environments and the README structure. It helped draft the README and the planning documents (problem statement, model plan, evaluation plan, demonstration plan), and suggested code for relative file paths and for saving the individual plots and metrics files. We edited all documents with our own details and results.
- **Gemini:** generated the first draft of the Logistic Regression code, which we modified (file paths, metrics and plots) and ran ourselves.
- **ROC curve, precision-recall curve:** these were not covered in our course, so we used AI to learn what they mean and to write the code for them.
- **Multiple plots in one figure (subplots):** displaying several graphs together in a single image was not covered in our course, so we used AI to learn how it works and to write that plotting code.
- We read and ran the AI-assisted code ourselves, and every result in this README comes from our own run. No AI was used to generate the dataset or the results.
