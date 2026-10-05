# 🚗 MPG Predictor

## 📌 Project Overview

This project uses **Machine Learning** to predict the **Miles Per Gallon (MPG)** of a car based on its different characteristics.

MPG represents the fuel efficiency of a vehicle. A higher MPG generally means the vehicle can travel more miles using the same amount of fuel.

The project uses a **regression model** because the goal is to predict a continuous numerical value.

---

## 🎯 Problem Statement

Given information about a vehicle such as its:

* Cylinders
* Displacement
* Horsepower
* Weight
* Acceleration
* Model Year

build a machine learning model that can predict the vehicle's **MPG (fuel efficiency)**.

### Example

```text
Vehicle Information
       ↓
Cylinders
Displacement
Horsepower
Weight
Acceleration
Model Year
       ↓
Machine Learning Model
       ↓
Predicted MPG
```

---

## 🧠 Machine Learning Approach

This is a **supervised learning regression problem**.

The model learns the relationship between different vehicle characteristics and their corresponding MPG values.

The target variable is:

```text
MPG
```

The remaining relevant numerical vehicle characteristics are used as input features.

---

## 📊 Dataset

The project uses vehicle specifications and their corresponding fuel efficiency values.

### Features

| Feature      | Description                                       |
| ------------ | ------------------------------------------------- |
| Cylinders    | Number of cylinders in the engine                 |
| Displacement | Engine displacement                               |
| Horsepower   | Engine horsepower                                 |
| Weight       | Weight of the vehicle                             |
| Acceleration | Vehicle acceleration                              |
| Model Year   | Year associated with the vehicle model            |
| Origin       | Origin of the vehicle, if included in the dataset |

### Target

| Target | Description                        |
| ------ | ---------------------------------- |
| MPG    | Miles Per Gallon / fuel efficiency |

---

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Loading
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Selection
   ↓
Train-Test Split
   ↓
Feature Scaling
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model Saving
   ↓
MPG Prediction
```

---

## ⚙️ Data Preprocessing

Before training the model, the dataset is prepared by:

* Checking the dataset for missing values.
* Selecting relevant features.
* Separating input features `X` and target `y`.
* Splitting the data into training and testing sets.
* Scaling the features when required by the selected model.

Feature scaling helps put numerical features on a comparable scale.

---

## 📈 Model Evaluation

The regression model can be evaluated using metrics such as:

### Mean Absolute Error (MAE)

Measures the average absolute difference between the actual MPG and predicted MPG.

### Mean Squared Error (MSE)

Measures the average squared difference between actual and predicted MPG.

### R² Score

Shows how well the model explains the variation in MPG.

A higher R² score generally indicates better predictive performance.

---

## 💾 Saved Model

The trained machine learning model is saved as a Pickle file.

```text
model.pkl
```

The saved model can be loaded later to make predictions without retraining the model.

---

## 🖥️ Application

The project contains an `app.py` file that can be used to create an interface for predicting MPG.

The user can provide vehicle information such as:

```text
Cylinders
Displacement
Horsepower
Weight
Acceleration
Model Year
```

The trained model then predicts the expected MPG.

```text
Vehicle Details
       ↓
Preprocessing
       ↓
Trained ML Model
       ↓
Predicted MPG
```

---

## 🛠️ Technologies Used

* Python 🐍
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Pickle
* Streamlit

---

## 📂 Project Structure

```text
MPG_Predictor/
│
├── app.py
├── dataset.csv
├── model.pkl
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
cd ML_Projects/MPG_Predictor
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

Or install them manually:

```bash
pip install pandas numpy matplotlib scikit-learn streamlit
```

### 4. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🔍 Example

Suppose a vehicle has:

```text
Cylinders     = 4
Displacement  = 120
Horsepower    = 90
Weight        = 2400
Acceleration  = 16
Model Year    = 80
```

These values are passed to the trained model:

```text
Vehicle Features
       ↓
Preprocessing
       ↓
ML Model
       ↓
Predicted MPG
```

The model returns the estimated fuel efficiency of the vehicle.

---

## 💡 Key Learning

Through this project, I practiced:

* Supervised Machine Learning
* Regression
* Feature Selection
* Data Preprocessing
* Train-Test Split
* Feature Scaling
* Regression Evaluation Metrics
* Model Serialization using Pickle
* Making predictions using a trained model
* Deploying an ML model using Streamlit

---

## 🚀 Future Improvements

* Compare multiple regression algorithms.
* Perform hyperparameter tuning.
* Improve feature engineering.
* Add more vehicle specifications.
* Add interactive data visualizations.
* Improve the Streamlit user interface.
* Deploy the application online.

