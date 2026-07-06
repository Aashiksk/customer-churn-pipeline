# Customer Churn Prediction using PySpark & Streamlit

## Project Overview

This project predicts whether a telecom customer is likely to churn using Machine Learning built with **Apache Spark (PySpark)**. The model is deployed through an interactive **Streamlit** web application where users can enter customer details and instantly receive churn predictions.

The project demonstrates a complete Machine Learning pipeline including:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training
- Model Evaluation
- Model Saving
- Streamlit Deployment

---

# Features

- End-to-end Machine Learning Pipeline
- Built completely using PySpark MLlib
- Random Forest Classifier
- Data preprocessing using Spark Pipeline
- Interactive Streamlit application
- Predicts customer churn probability
- Saved reusable ML pipeline

---

# Tech Stack

### Programming Language
- Python

### Big Data
- Apache Spark
- PySpark

### Machine Learning
- Spark MLlib
- Random Forest Classifier

### Data Processing
- Pandas

### Visualization
- Matplotlib
- Seaborn

### Deployment
- Streamlit

### Development Tools
- VS Code
- Git
- GitHub

---

# Project Structure

```
Customer-Churn-Pipeline/
│
├── app/
│   └── app.py
│
├── data/
│
├── notebooks/
│
├── processed/
│
├── saved_model/
│
├── screenshots/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Machine Learning Workflow

1. Load Dataset
2. Clean Missing Values
3. Feature Engineering
4. Exploratory Data Analysis
5. Convert Data to Spark DataFrame
6. Encode Categorical Features
7. Assemble Features
8. Train Random Forest Model
9. Evaluate Model
10. Save Pipeline Model
11. Deploy with Streamlit

---

# Model Performance

| Metric | Score |
|--------|-------|
| Accuracy | **79.66%** |
| Precision | **77.38%** |
| Recall | **79.66%** |
| F1 Score | **78.72%** |

---

# How to Run

## Clone Repository

```bash
git clone https://github.com/Aashiksk/customer-churn-pipeline
```

## Create Virtual Environment

```bash
python -m venv venv
```

### Activate

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Streamlit App

```bash
streamlit run app/app.py
```

---

# Screenshots

## Streamlit Application

(Add screenshot here)

---

## Churn Distribution

(Add screenshot here)

---

## Model Evaluation

(Add screenshot here)

---

# Dataset

Dataset:
Telco Customer Churn Dataset

Source:
https://www.kaggle.com/blastchar/telco-customer-churn

---

# Future Improvements

- Hyperparameter Tuning
- XGBoost Implementation
- Docker Deployment
- AWS Deployment
- Real-time Prediction API
- CI/CD Pipeline

---

# Author

**SHEIK ABDUL AASHIK**

GitHub:
https://github.com/Aashiksk

LinkedIn:
www.linkedin.com/in/aashiksk0192