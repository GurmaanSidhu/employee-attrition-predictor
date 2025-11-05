# 🧠 Employee Attrition Predictor

This project predicts whether an employee is likely to leave the company using a **Logistic Regression** model.  
It was developed as part of the **Machine Learning with Data Science Summer Training (CipherSchools)**.

---

## 📊 Project Overview

Employee attrition — when employees leave an organization — is a major challenge for businesses.  
Understanding why people quit helps HR teams reduce turnover and improve workplace satisfaction.  

The main goal of this project is to:
- Analyze employee data (income, age, satisfaction, years at company, overtime)
- Build a predictive model to determine the likelihood of an employee leaving
- Identify important factors influencing attrition

---

## 🧾 Dataset

The dataset contains HR-related information, including:

| Feature | Description |
|----------|--------------|
| **MonthlyIncome** | Employee’s monthly salary |
| **Age** | Employee’s age |
| **JobSatisfaction** | Job satisfaction rating |
| **YearsAtCompany** | Number of years at the company |
| **OverTime** | Whether the employee works overtime (Yes/No) |
| **Attrition** | Target variable (Yes = employee left, No = stayed) |

📂 **Dataset Source:** [Google Sheets Dataset](https://docs.google.com/spreadsheets/d/11wkjia84rKmOys3Fpxij3jgf_Dyq8qfBcBAqGAe4o9A/edit?usp=sharing)

---

## ⚙️ Methodology

1. **Exploratory Data Analysis (EDA):**  
   - Inspected data structure, missing values, and feature distributions.  
   - Visualized relationships using histograms, boxplots, and heatmaps.  

2. **Data Preprocessing:**  
   - Removed missing values and outliers using IQR.  
   - Encoded categorical variables (`OverTime`, `Attrition`) using `LabelEncoder`.  
   - Standardized features for better model performance.  

3. **Model Building:**  
   - Implemented a **Logistic Regression** model for binary classification.  
   - Split the dataset into 80% training and 20% testing data.  

4. **Model Evaluation:**  
   - Evaluated performance using **Accuracy**, **Precision**, **Recall**, and **F1-score**.  
   - Analyzed the **Confusion Matrix** to assess prediction reliability.

---

## 🧮 Technologies Used

- **Python**
- **Pandas**, **NumPy**
- **Seaborn**, **Matplotlib**
- **Scikit-learn**

---

## 🚀 Results and Insights

- The **Logistic Regression model** achieved strong accuracy in predicting employee attrition.  
- Features like **OverTime**, **JobSatisfaction**, and **YearsAtCompany** showed strong influence on attrition.  
- Employees with **low satisfaction** and **frequent overtime** had higher chances of leaving.  

---

## 🌍 Real-World Applications

- **HR Analytics:** Identify at-risk employees and take preventive actions (e.g., promotions, workload balance).  
- **Talent Retention:** Use predictions to improve employee satisfaction and retention strategies.  
- **Business Planning:** Help management reduce turnover costs by addressing key attrition drivers.  
- **Workforce Optimization:** Plan future hiring and training needs based on attrition trends.

---

## 💡 Learnings and Future Work

This project provided hands-on experience with:
- Cleaning and analyzing real-world HR data  
- Implementing a complete ML workflow (EDA → Preprocessing → Modeling → Evaluation)  
- Understanding how Logistic Regression can be applied to classification problems  

**Future improvements:**
- Experiment with other models (Random Forest, XGBoost)  
- Use hyperparameter tuning to optimize performance  
- Handle class imbalance using SMOTE or weighted models  

---

## 📂 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/employee-attrition-predictor.git
   cd employee-attrition-predictor
