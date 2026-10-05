# 💵 Banknotes Authentication

## 📌 Project Overview

This project uses **Decision Tree Classification** to determine whether a banknote is **genuine or forged** based on features extracted from images of banknotes.

The model learns patterns from the numerical features in the dataset and predicts the authenticity of a new banknote.

This is a **supervised machine learning classification** problem because the dataset contains a target variable indicating whether the banknote is genuine or forged.

---

## 🎯 Problem Statement

Given different numerical measurements extracted from images of banknotes, build a machine learning model that can classify a banknote as:

* ✅ Genuine
* ❌ Forged

The goal is to train a classification model that can accurately identify whether a banknote is authentic.

---

## 🧠 Machine Learning Algorithm

### Decision Tree Classifier 🌳

A **Decision Tree** is a supervised machine learning algorithm that makes predictions by creating a series of decision rules.

The tree starts with a **root node** and splits the data based on the feature that provides the best separation between the classes.

In this project, **Gini Impurity** is used to determine the quality of the splits.

### Why Decision Tree?

Decision Trees are useful because:

* They are easy to understand.
* They can handle numerical features.
* They do not require feature scaling.
* Their decision-making process can be visualized.
* They work well for classification problems.

---

## 📊 Dataset

The dataset contains numerical features extracted from images of banknotes.

### Features Used

| Feature  | Description                                    |
| -------- | ---------------------------------------------- |
| Variance | Variance of the image wavelet-transformed data |
| Skewness | Skewness of the image wavelet-transformed data |
| Curtosis | Curtosis of the image wavelet-transformed data |
| Entropy  | Entropy of the image data                      |

### Target

The target variable represents whether the banknote is genuine or forged.

```text
0 → Genuine
1 → Forged
```

> The exact class interpretation should be verified from the dataset/model output because target-label meanings depend on how the dataset is encoded.

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
Decision Tree Model
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

## ⚙️ Model Training

The dataset is divided into:

* **Training data** → Used to train the model.
* **Testing data** → Used to evaluate the model on unseen data.

The Decision Tree learns relationships between the four input features and the target class.

---

## 📏 Model Evaluation

The model can be evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

### Confusion Matrix

The confusion matrix helps understand how many banknotes were correctly and incorrectly classified.

```text
                 Predicted
              Genuine  Forged
Actual
Genuine          TP       FN
Forged           FP       TN
```

This helps identify whether the model is making false predictions.

---

## 💾 Saved Model

The trained Decision Tree model is saved using **Pickle**.

```text
decision_tree.pkl
```

The saved model can later be loaded and used to predict the authenticity of new banknotes without retraining the model.

---

## 🖥️ Application

The project contains an `app.py` file that can be used to create an interface for making predictions using the trained model.

The application takes the banknote's feature values as input and predicts its class.

```text
Input Features
      ↓
Decision Tree Model
      ↓
Prediction
      ↓
Genuine / Forged
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

```text
Banknotes_Authentication/
│
├── app.py
├── dataset.csv
├── decision_tree.pkl
└── README.md
```

> File names may vary slightly depending on the final files in the repository.

---

## ▶️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/aditi-tawade-ai/ML_Projects.git
```

### 2. Navigate to the Project

```bash
cd ML_Projects/Banknotes_Authentication
```

### 3. Install Required Libraries

```bash
pip install pandas numpy scikit-learn matplotlib seaborn streamlit
```

### 4. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🔍 Example

Suppose a new banknote has the following feature values:

```text
Variance  = 3.62
Skewness  = 8.67
Curtosis  = -2.81
Entropy   = -0.45
```

These values are passed to the trained Decision Tree:

```text
Banknote Features
       ↓
Decision Tree
       ↓
Decision Rules
       ↓
Prediction
       ↓
Genuine / Forged
```

---

## 💡 Key Learning

Through this project, I practiced:

* Supervised Machine Learning
* Classification
* Decision Tree algorithm
* Gini Impurity
* Train-Test Split
* Confusion Matrix
* Classification Report
* Model evaluation
* Model serialization using Pickle
* Using a trained ML model for predictions
* Deploying an ML model using Streamlit

---

## 🚀 Future Improvements

* Compare Decision Tree with Random Forest, KNN and SVM.
* Tune the Decision Tree hyperparameters.
* Visualize the complete decision tree.
* Add interactive prediction features.
* Improve the Streamlit user interface.
* Deploy the application online.

