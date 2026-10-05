# 👥 Age & Income Clustering

## 📌 Project Overview

This project uses **K-Means Clustering**, an unsupervised machine learning algorithm, to group people based on their **Age** and **Annual Income**.

The main goal is to identify different groups of people with similar age and income characteristics.

Since this is an **unsupervised learning** problem, there is no predefined target/output column. The algorithm automatically finds patterns and forms clusters in the data.

---

## 🎯 Problem Statement

Given information about people's **Age** and **Annual Income**, divide them into meaningful groups using the **K-Means Clustering algorithm**.

The model can help identify groups such as:

* Young people with lower income
* Young people with higher income
* Older people with lower income
* Older people with higher income

The actual groups are determined by the algorithm based on the data.

---

## 🧠 Machine Learning Algorithm

### K-Means Clustering

K-Means is an **unsupervised learning algorithm** that divides data into a predefined number of clusters.

The basic process is:

1. Select the number of clusters `K`.
2. Randomly initialize cluster centroids.
3. Assign each data point to its nearest centroid.
4. Calculate new centroid positions.
5. Repeat the process until the centroids stabilize.

In this project, **K-Means** is used to group people based on:

* `Age`
* `Annual Income`

---

## 📊 Dataset

The dataset contains information about individuals and their income.

### Features Used

| Feature       | Description                     |
| ------------- | ------------------------------- |
| Age           | Age of the individual           |
| Annual Income | Annual income of the individual |

Only these relevant numerical features are used for clustering.

---

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Loading
   ↓
Data Preprocessing
   ↓
Feature Selection
   ↓
Feature Scaling
   ↓
Finding Optimal Number of Clusters
   ↓
K-Means Clustering
   ↓
Cluster Assignment
   ↓
Model Saving
   ↓
Prediction
```

---

## 📈 Choosing the Number of Clusters

The **Elbow Method** is used to determine a suitable value of `K`.

The algorithm is trained with different values of `K`, and the **Within-Cluster Sum of Squares (WCSS)** is calculated.

The value of `K` where the decrease in WCSS starts becoming less significant is considered the **elbow point**.

---

## ⚙️ Data Preprocessing

Before applying K-Means, the numerical features are scaled using **StandardScaler**.

This is important because Age and Annual Income have different ranges.

Without scaling, the feature with larger numerical values could have a greater influence on the clustering process.

---

## 💾 Saved Model Files

| File         | Purpose                                      |
| ------------ | -------------------------------------------- |
| `kmeans.pkl` | Trained K-Means clustering model             |
| `scaler.pkl` | Fitted StandardScaler used for preprocessing |

These files allow the trained model to be reused without training it again.

---

## 🖥️ Application

The project also contains an `app.py` file that can be used to run the trained clustering model and make predictions for new input data.

The application takes:

* Age
* Annual Income

and predicts the **cluster** to which the person belongs.

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
Age_Income_Clustering/
│
├── app.py
├── Employee_income_1.csv
├── kmeans.pkl
├── scaler.pkl
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
cd ML_Projects/Age_Income_Clustering
```

### 3. Install Required Libraries

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

Suppose a new person has:

```text
Age = 25
Annual Income = 50000
```

The trained K-Means model will determine which cluster this person belongs to based on the patterns learned from the dataset.

For example:

```text
Input
Age = 25
Annual Income = 50000

        ↓

Scaling

        ↓

K-Means Model

        ↓

Predicted Cluster
```

The cluster number itself does **not** have a fixed meaning.
For example, **Cluster 0 is not necessarily "low income"**. The characteristics of each cluster must be examined after training.

---

## 💡 Key Learning

Through this project, I practiced:

* Unsupervised Machine Learning
* K-Means Clustering
* Feature selection
* Feature scaling
* Elbow Method
* Cluster analysis
* Model serialization using Pickle
* Using a trained ML model for predictions
* Deploying an ML model using Streamlit

---

## 🚀 Future Improvements

* Add more features for better segmentation.
* Visualize the clusters interactively.
* Add cluster descriptions based on average age and income.
* Improve the Streamlit interface.
* Compare K-Means with other clustering algorithms such as DBSCAN and Hierarchical Clustering.

