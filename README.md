````markdown
# AI-Driven Supply Chain Risk Classification Framework

## Project Overview

The **AI-Driven Supply Chain Risk Classification Framework** is a machine learning-based system developed to identify, classify, and prioritize risks within supply chain operations. The project focuses on analyzing logistics, supplier performance, inventory conditions, transportation metrics, operational indicators, and external disruption data to predict different categories of supply chain risks.

The framework supports intelligent decision-making by generating:
- Risk classifications
- Risk severity levels
- Operational insights
- Visualization dashboards

This project is developed as part of an internship at **Esparse Matrix Solutions Private Limited**.

---

# Problem Statement

Supply chains are vulnerable to various operational and external risks such as:
- Supplier delays
- Traffic congestion
- Inventory shortages
- Cargo damage
- Weather disruptions
- Transportation inefficiencies

Traditional monitoring systems struggle to proactively identify and classify these risks. This project aims to solve this challenge using Artificial Intelligence and Machine Learning techniques.

---

# Project Objectives

The major objectives of this project are:

- To identify major supply chain risk categories
- To preprocess and analyze logistics and operational datasets
- To build machine learning models for automated risk classification
- To calculate and categorize risk severity levels
- To visualize operational risks through an interactive dashboard
- To support decision-making using predictive analytics

---

# Risk Categories

The system classifies risks into the following categories:

- Supplier Risk
- Logistics Risk
- Quality Risk
- Demand Risk
- Operational Risk
- External Disruption Risk
- Low Risk

---

# Dataset Description

The dataset contains logistics and supply chain operational parameters such as:

| Feature | Description |
|---|---|
| ETA Variation | Difference between estimated and actual delivery times |
| Traffic Congestion Level | Traffic severity affecting logistics routes |
| Warehouse Inventory Level | Inventory availability at warehouses |
| Shipping Costs | Transportation and shipping expenses |
| Supplier Reliability Score | Supplier performance and reliability indicator |
| Lead Time | Average delivery time from suppliers |
| IoT Temperature | Sensor-based cargo temperature monitoring |
| Cargo Condition Status | Cargo quality condition indicator |
| Weather Condition Severity | Weather disruption severity |
| Route Risk Level | Risk associated with transportation routes |
| Driver Behavior Score | Driver safety and behavior score |
| Fatigue Monitoring Score | Driver fatigue detection score |

---

# Technology Stack

## Programming Language
- Python

## Libraries & Frameworks
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- XGBoost
- SHAP
- Streamlit

## Development Environment
- Visual Studio Code
- Jupyter Notebook

---

# Project Workflow

```text
Data Collection
        ↓
Data Preprocessing
        ↓
Feature Engineering
        ↓
Risk Label Generation
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Risk Prediction
        ↓
Dashboard Visualization
````

---

# Project Structure

```text
AI_SupplyChain_Risk_Classification/
│
├── data/
│   ├── raw_data/
│   └── processed_data/
│
├── models/
│
├── notebooks/
│   └── eda.ipynb
│
├── reports/
│
├── src/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── risk_labeling.py
│   ├── model_training.py
│   ├── evaluate_model.py
│   ├── predict_risk.py
│   └── dashboard.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Machine Learning Models

The following machine learning algorithms are used for risk classification:

* Decision Tree Classifier
* Random Forest Classifier
* XGBoost Classifier

---

# Evaluation Metrics

The models are evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

---

# Explainable AI

The project uses Explainable AI techniques to improve model interpretability.

Tools Used:

* SHAP (SHapley Additive Explanations)
* Feature Importance Analysis

These techniques help identify the key operational factors contributing to supply chain risks.

---

# Dashboard Features

The dashboard provides:

* Risk Category Prediction
* Risk Severity Visualization
* Operational Analytics
* Supply Chain Insights
* Risk Alerts
* Interactive Charts

---

# Installation Guide

## Step 1: Clone Repository

```bash
git clone <repository-link>
```

## Step 2: Create Virtual Environment

```bash
python -m venv venv
```

## Step 3: Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

## Step 4: Install Required Libraries

```bash
pip install -r requirements.txt
```

---

# Running the Project

## Run Main Application

```bash
python main.py
```

## Run Dashboard

```bash
streamlit run src/dashboard.py
```

---

# Future Enhancements

* Real-time IoT integration
* NLP-based disruption detection
* Cloud deployment
* Real-time alert systems
* Advanced deep learning models
* API integration with ERP systems

---

# Expected Outcomes

The system is expected to:

* Improve supply chain visibility
* Reduce operational risks
* Support proactive decision-making
* Improve logistics efficiency
* Predict high-risk operational conditions

---

# Team Members

* Vidhi Patel
* [Second Member Name]

---

# Organization

Developed during internship at:

**Esparse Matrix Solutions Private Limited**

---

# License

This project is developed for academic and internship purposes.

```
```
