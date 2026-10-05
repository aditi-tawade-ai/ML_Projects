# 🍷 Wine Type Prediction

## 📌 Project Overview

This project uses **Logistic Regression** to predict the **type of wine** based on its chemical properties.

The dataset contains different chemical measurements of wine samples. The machine learning model learns the relationship between these measurements and the wine type, then predicts the class of a new wine sample.

This is a **supervised machine learning classification** problem because the dataset contains a predefined target variable.

---

## 🎯 Problem Statement

Given the chemical properties of a wine sample, build a machine learning model that can classify the wine into its correct type.

The model uses multiple chemical characteristics of wine as input and predicts one of the available wine classes.

### Example

```text id="9d8k2q"
Wine Chemical Properties
        ↓
Data Preprocessing
        ↓
Logistic Regression
        ↓
Wine Type Prediction
```

---

## 🧠 Machine Learning Algorithm

### Logistic Regression

**Logistic Regression** is a supervised machine learning algorithm commonly used for classification problems.

Although its name contains "Regression", it is mainly used to predict **classes/categories**.

In this project, Logistic Regression is used for **multi-class classification** because the dataset contains multiple wine classes.

The model calculates probabilities for the different classes and assigns the sample to the class with the highest probability.

---

## 📊 Dataset

The dataset contains chemical properties of different wine samples.

### Features Used

The model uses chemical characteristics such as:

| Feature              | Description                     |
| -------------------- | ------------------------------- |
| Alcohol              | Alcohol content                 |
| Malic Acid           | Amount of malic acid            |
| Ash                  | Ash content                     |
| Alcalinity of Ash    | Alcalinity of ash               |
| Magnesium            | Magnesium content               |
| Total Phenols        | Total phenolic compounds        |
| Flavanoids           | Flavanoid content               |
| Nonflavanoid Phenols | Nonflavanoid phenolic compounds |
| Proanthocyanins      | Proanthocyanin content          |
| Color Intensity      | Intensity of wine color         |
| Hue                  | Hue of the wine                 |
| OD280/OD315          | Diluted wine measurement        |
| Proline              | Proline content                 |

### Target

The target represents the **wine class/type**.

The dataset contains **three wine classes**.

---

## 🔄 Project Workflow

```text id="4h5g7w"
Wine Dataset
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
Logistic Regression
      ↓
Model Training
      ↓
Prediction
      ↓
Model Evaluation
      ↓
Model Saving
```

---

## ⚙️ Feature Scaling

Feature scaling is performed using **StandardScaler**.

This is important because the chemical features have different numerical ranges.

StandardScaler transforms the features so that they are on a comparable scale.

```text id="j7h2f0"
Original Features
       ↓
StandardScaler
       ↓
Scaled Features
       ↓
Logistic Regression
```

---

## 🍷 Multi-Class Classification

Unlike binary classification, where there are only two possible classes, this project contains **three wine classes**.

The model predicts which of the three classes a new wine sample belongs to.

```text id="1f8d6j"
Wine Sample
     ↓
Logistic Regression
     ↓
┌─────────────┐
│ Class 1     │
│ Class 2     │
│ Class 3     │
└─────────────┘
     ↓
Predicted Wine Type
```

---

## 📏 Model Evaluation

The model is evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix
* Classification Report

### Confusion Matrix

The confusion matrix shows how correctly the model classified samples from each wine class.

```text id="q3c8tw"
                 Predicted
              C1    C2    C3
Actual C1     ✓
       C2           ✓
       C3                 ✓
```

A strong diagonal indicates that most samples were correctly classified.

---

## 💾 Saved Model Files

| File         | Purpose                                      |
| ------------ | -------------------------------------------- |
| `model.pkl`  | Trained Logistic Regression model            |
| `scaler.pkl` | Fitted StandardScaler used for preprocessing |

Both the model and scaler are saved so that they can be reused for predictions without retraining.

---

## 🖥️ Application

The project contains an `app.py` file that can be used to make predictions using the trained model.

The application takes the chemical properties of a wine sample as input.

```text id="j3d9aa"
Wine Features
      ↓
StandardScaler
      ↓
Logistic Regression
      ↓
Predicted Class
      ↓
Wine Type
```

---

## 🛠️ Technologies Used

* Python 🐍
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Pickle
* Streamlit

---

## 📂 Project Structure

```text id="w8y1je"
Wine_Type_Prediction/
│
├── app.py
├── dataset.csv
├── model.pkl
├── scaler.pkl
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

### 1. Clone the Repository

```bash id="7q2hkr"
git clone https://github.com/aditi-tawade-ai/ML_Projects.git
```

### 2. Navigate to the Project

```bash id="3w7k5a"
cd ML_Projects/Wine_Type_Prediction
```

### 3. Install Required Libraries

```bash id="m4b8qz"
pip install -r requirements.txt
```

Or install them manually:

```bash id="s5q2jk"
pip install pandas numpy scikit-learn matplotlib seaborn streamlit
```

### 4. Run the Application

```bash id="k9r3mw"
streamlit run app.py
```

The application will open in your browser.

---

## 🔍 Example

A new wine sample provides values for its chemical properties:

```text id="x7c1pa"
Alcohol
Malic Acid
Ash
Magnesium
Flavanoids
Color Intensity
Hue
Proline
...
```

The values are passed through the preprocessing pipeline:

```text id="e5w9sx"
Wine Features
      ↓
StandardScaler
      ↓
Logistic Regression
      ↓
Class Probabilities
      ↓
Highest Probability Class
      ↓
Predicted Wine Type
```

---

## 💡 Key Learning

Through this project, I practiced:

* Supervised Machine Learning
* Classification
* Logistic Regression
* Multi-Class Classification
* Feature Scaling
* Train-Test Split
* Confusion Matrix
* Classification Report
* Model Evaluation
* Model Serialization using Pickle
* Making predictions using a trained model
* Deploying an ML model using Streamlit

---

## 🚀 Future Improvements

* Compare Logistic Regression with SVM, KNN and Decision Tree.
* Perform hyperparameter tuning.
* Experiment with different classification algorithms.
* Add interactive visualizations for wine features.
* Display prediction probabilities in the application.
* Improve the Streamlit interface.
* Deploy the application online.
