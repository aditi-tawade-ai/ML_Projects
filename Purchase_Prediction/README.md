# 🛒 Purchase Prediction

## 📌 Project Overview

This project uses **K-Nearest Neighbors (KNN)** to predict whether a customer is likely to **purchase a product** based on their **Age** and **Estimated Salary**.

The model learns from previous customer data and classifies a new customer into one of two categories:

* ✅ Will Purchase
* ❌ Will Not Purchase

This is a **supervised machine learning classification** problem because the dataset contains a predefined target variable.

---

## 🎯 Problem Statement

Given a customer's:

* Age
* Estimated Salary

build a machine learning model that predicts whether the customer is likely to purchase a product.

### Example

```text
Customer Information
       ↓
Age
Estimated Salary
       ↓
KNN Model
       ↓
Purchase Prediction
       ↓
Yes / No
```

---

## 🧠 Machine Learning Algorithm

### K-Nearest Neighbors (KNN)

**KNN** is a supervised machine learning algorithm used for classification and regression.

For a new customer, KNN:

1. Calculates the distance between the new customer and existing customers.
2. Finds the nearest `K` customers.
3. Looks at their classes.
4. Assigns the class with the majority vote.

In this project, KNN is used to classify customers based on their purchasing behavior.

---

## 📊 Dataset

The dataset contains information about customers and whether they purchased the product.

### Features Used

| Feature          | Description                             |
| ---------------- | --------------------------------------- |
| Age              | Age of the customer                     |
| Estimated Salary | Estimated annual salary of the customer |

### Target

| Target    | Description                                          |
| --------- | ---------------------------------------------------- |
| Purchased | Indicates whether the customer purchased the product |

```text
0 → Did not purchase
1 → Purchased
```

---

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Loading
   ↓
Data Exploration
   ↓
Feature Selection
   ↓
Train-Test Split
   ↓
Feature Scaling
   ↓
Choose K
   ↓
Train KNN Model
   ↓
Make Predictions
   ↓
Evaluate Model
   ↓
Save Model
   ↓
Predict New Customer
```

---

## ⚙️ Feature Scaling

Feature scaling is particularly important for KNN because KNN calculates the **distance** between data points.

Age and Estimated Salary have very different numerical ranges.

For example:

```text
Age              → 18–60
Estimated Salary → 15,000–150,000
```

Without scaling, Estimated Salary could dominate the distance calculation.

Therefore, **StandardScaler** is used to scale the features before applying KNN.

---

## 🔢 Choosing the Value of K

The value of `K` determines how many neighboring data points are considered when making a prediction.

Different values of `K` can be tested and evaluated to find a suitable value.

In this project, **K = 7** was selected for the final model based on model evaluation.

---

## 📏 Model Evaluation

The model can be evaluated using:

* Accuracy
* Precision
* Recall
* F1-score

