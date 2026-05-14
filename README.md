# OIBSIP-Sales-Prediction
# 📊 Sales Prediction using Python

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge\&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black?style=for-the-badge\&logo=pandas)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge\&logo=scikitlearn)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

A Machine Learning project that predicts product sales based on advertising budget spent on TV, Radio, and Newspaper platforms.

---

# 📚 Table of Contents

1. [Project Overview](#-project-overview)
2. [Dataset](#-dataset)
3. [Technologies Used](#-technologies-used)
4. [Machine Learning Pipeline](#-machine-learning-pipeline)
5. [Model Used](#-model-used)
6. [Results](#-results)
7. [How to Run](#-how-to-run)
8. [Conclusion](#-conclusion)

---

# 📌 Project Overview

Sales prediction means predicting how much of a product people will buy based on different factors such as advertising cost, target audience, and advertising platform.

In this project, we use Machine Learning to predict sales based on the amount spent on:

* TV advertising
* Radio advertising
* Newspaper advertising

---

# 📂 Dataset

Dataset used:

* `Advertising.csv`

Features:

```text
TV
Radio
Newspaper
```

Target:

```text
Sales
```

---

# 🛠 Technologies Used

* Python
* Pandas
* Scikit-learn
* Linear Regression

---

# ⚙ Machine Learning Pipeline

```text
Load Dataset
   ↓
Clean Data
   ↓
Select Features and Target
   ↓
Split Dataset
   ↓
Train Model
   ↓
Predict Sales
   ↓
Evaluate Model
```

---

# 🤖 Model Used

## Linear Regression

Linear Regression is used because this is a regression problem where the output is a continuous numerical value.

---

# 📈 Results

The model predicts sales based on advertising budget and evaluates performance using:

* Mean Absolute Error
* R² Score

Example:

```text
Input:
TV = 150
Radio = 25
Newspaper = 30

Output:
Predicted Sales = approximate sales value
```

---

# ▶ How to Run

## Install dependencies

```bash
pip install pandas scikit-learn
```

## Run the project

```bash
python sales_prediction.py
```

---

# 📌 Conclusion

This project demonstrates how Machine Learning can be used to predict future sales based on advertising investment. It helps businesses understand the relationship between advertising spending and product sales.
