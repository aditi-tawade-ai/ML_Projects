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
* Confusion Matrix

### Precision

Precision tells us how many customers predicted as purchasers actually purchased.

### Recall

Recall tells us how many of the actual purchasers were correctly identified.

### F1-Score

F1-score provides a balance between precision and recall.

---

## 💾 Saved Model Files

| File         | Purpose                                      |
| ------------ | -------------------------------------------- |
| `knn.pkl`    | Trained KNN classification model             |
| `scaler.pkl` | Fitted StandardScaler used for preprocessing |

The scaler is saved because new input data must go through the **same scaling process** used during model training.

---

## 🖥️ Application

The project contains an `app.py` file that can be used to make predictions for a new customer.

The application takes:

```text
Age
Estimated Salary
```

and predicts whether the customer is likely to purchase the product.

```text
Customer Details
       ↓
StandardScaler
       ↓
KNN Model
       ↓
Prediction
       ↓
Purchased / Not Purchased
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
Purchase_Prediction/
│
├── app.py
├── dataset.csv
├── knn.pkl
├── scaler.pkl
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/aditi-tawade-ai/ML_Projects.git
```

### 2. Navigate to the Project

```bash
cd ML_Projects/Purchase_Prediction
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

Or install them manually:

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

Suppose a new customer has:

```text
Age = 35
Estimated Salary = 60,000
```

The input is first scaled using the saved scaler:

```text
Age + Salary
      ↓
StandardScaler
      ↓
KNN Model
      ↓
Nearest Customers
      ↓
Majority Vote
      ↓
Purchase Prediction
```

The model then predicts whether the customer is likely to purchase the product.

---

## 💡 Key Learning

Through this project, I practiced:

* Supervised Machine Learning
* Classification
* K-Nearest Neighbors (KNN)
* Choosing the value of K
* Feature Scaling
* Train-Test Split
* Distance-based classification
* Confusion Matrix
* Precision, Recall and F1-score
* Model Serialization using Pickle
* Using a trained ML model for predictions
* Deploying an ML model using Streamlit

---

## 🚀 Future Improvements

* Perform hyperparameter tuning to find the optimal `K`.
* Compare KNN with SVM, Decision Tree and Random Forest.
* Improve model performance using feature engineering.
* Add probability/confidence information to predictions.
* Improve the Streamlit interface.
* Deploy the application online.
