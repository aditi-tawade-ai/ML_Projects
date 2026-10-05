# 🛍️ Customer Segmentation

## 📌 Project Overview

This project uses **K-Means Clustering** to segment customers into different groups based on their **Annual Income** and **Spending Score**.

The purpose of customer segmentation is to identify customers with similar purchasing behavior so that businesses can understand their customers better and create targeted strategies.

This is an **unsupervised machine learning** project because there is no predefined target variable. The algorithm automatically discovers groups within the customer data.

---

## 🎯 Problem Statement

Given customer information such as **Annual Income** and **Spending Score**, divide customers into meaningful groups using the **K-Means Clustering algorithm**.

The resulting customer segments can help a business identify groups such as:

* 💰 High-income, high-spending customers
* 💰 High-income, low-spending customers
* 🛍️ Low-income, high-spending customers
* 🛍️ Low-income, low-spending customers
* 👥 Average-income, average-spending customers

The actual clusters are determined by the model based on the patterns in the dataset.

---

## 🧠 Machine Learning Algorithm

### K-Means Clustering

**K-Means** is an unsupervised machine learning algorithm that divides data points into a specified number of clusters.

The algorithm works by:

1. Selecting the number of clusters `K`.
2. Initializing cluster centroids.
3. Assigning each customer to the nearest centroid.
4. Calculating new centroid positions.
5. Repeating the process until the clusters stabilize.

---

## 📊 Dataset

The dataset contains customer information related to their income and spending behavior.

### Features Used

| Feature        | Description                                         |
| -------------- | --------------------------------------------------- |
| Annual Income  | Customer's annual income                            |
| Spending Score | Score representing the customer's spending behavior |

These features are used to identify similarities between customers.

---

## 🔄 Project Workflow

```text
Customer Dataset
       ↓
Data Loading
       ↓
Data Exploration
       ↓
Feature Selection
       ↓
Feature Scaling
       ↓
Finding Optimal K
       ↓
K-Means Clustering
       ↓
Customer Segmentation
       ↓
Cluster Visualization
       ↓
Model Saving
       ↓
Prediction
```

---

## 📈 Finding the Optimal Number of Clusters

The **Elbow Method** is used to determine an appropriate value of `K`.

Different values of `K` are tested and the **Within-Cluster Sum of Squares (WCSS)** is calculated.

The value where the WCSS starts decreasing more slowly is considered the **elbow point** and can be selected as the number of clusters.

---

## ⚙️ Feature Scaling

Before applying K-Means, the features are scaled using **StandardScaler**.

Scaling is important because Annual Income and Spending Score may have different numerical ranges.

Without scaling, a feature with a larger numerical range could have a greater influence on the clustering process.

---

## 👥 Customer Segments

After applying K-Means, customers are assigned to different clusters.

The clusters can then be analyzed based on their average income and spending score.

For example:

```text
High Income + High Spending
        ↓
Potential Premium Customers


High Income + Low Spending
        ↓
Potentially Under-engaged Customers


Low Income + High Spending
        ↓
Potential High-value Spending Group


Low Income + Low Spending
        ↓
Low-value / Budget Customers
```

The exact interpretation depends on the cluster centers produced by the model.

---

## 💾 Saved Model Files

| File         | Purpose                                      |
| ------------ | -------------------------------------------- |
| `kmeans.pkl` | Trained K-Means clustering model             |
| `scaler.pkl` | Fitted StandardScaler used for preprocessing |

The saved files allow the trained model to be reused without training it again.

---

## 🖥️ Application

The project contains an `app.py` file that can be used to interact with the trained clustering model.

The application can take customer information such as:

```text
Annual Income
Spending Score
```

and determine which customer segment the person belongs to.

```text
Customer Information
        ↓
Feature Scaling
        ↓
K-Means Model
        ↓
Cluster Prediction
        ↓
Customer Segment
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
Customer_Segmentation/
│
├── app.py
├── dataset.csv
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
cd ML_Projects/Customer_Segmentation
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

Suppose a customer has:

```text
Annual Income = 80,000
Spending Score = 85
```

The values are passed through the scaler and then to the trained K-Means model.

```text
Annual Income = 80,000
Spending Score = 85
        ↓
StandardScaler
        ↓
K-Means Model
        ↓
Predicted Cluster
```

The predicted cluster can then be analyzed to understand the customer's spending behavior.

---

## 💡 Key Learning

Through this project, I practiced:

* Unsupervised Machine Learning
* K-Means Clustering
* Customer Segmentation
* Feature Selection
* Feature Scaling
* Elbow Method
* WCSS
* Cluster Analysis
* Data Visualization
* Model Serialization using Pickle
* Using a trained ML model for predictions
* Deploying an ML model using Streamlit

---

## 🚀 Future Improvements

* Add more customer features such as age and purchase frequency.
* Create interactive cluster visualizations.
* Add automatic descriptions for each customer segment.
* Compare K-Means with DBSCAN and Hierarchical Clustering.
* Improve the Streamlit interface.
* Deploy the application online.

