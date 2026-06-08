# Employee Attrition Intelligence Platform

## Project Overview

Employee attrition is a critical challenge for organizations as it impacts productivity, operational costs, and workforce stability. This project leverages data analytics and machine learning techniques to identify the factors influencing employee turnover and predict employees who are at risk of leaving the organization.

Using the IBM HR Analytics Employee Attrition dataset, the project performs exploratory data analysis, feature engineering, predictive modeling, and business intelligence reporting to generate actionable workforce insights.

---

## Objectives

* Analyze employee demographics, job roles, compensation, and work-related factors affecting attrition.
* Identify key patterns and trends associated with employee turnover.
* Develop a machine learning model to predict attrition risk.
* Provide an interactive dashboard for workforce analysis and decision-making.

---

## Dataset Information

**Dataset:** IBM HR Analytics Employee Attrition Dataset

* Total Records: 1,470 Employees
* Features: 35 Employee Attributes
* Target Variable: Attrition (Yes/No)
* Data Quality: No Missing Values

The dataset contains information related to employee demographics, job satisfaction, compensation, performance, work-life balance, and employment history.

---

## Methodology

### 1. Data Preprocessing

* Data cleaning and validation
* Encoding categorical variables
* Feature selection and transformation

### 2. Exploratory Data Analysis (EDA)

* Attrition distribution analysis
* Department-wise attrition trends
* Income and overtime impact assessment
* Age-group and experience-based analysis
* Correlation and feature importance evaluation

### 3. Machine Learning

* Train-test data split
* Random Forest Classification
* Model evaluation using accuracy, precision, recall, and confusion matrix

### 4. Business Intelligence Dashboard

* Interactive visualizations using Streamlit
* Dynamic filtering and KPI monitoring
* Attrition risk analysis and reporting

---

## Key Insights

* Employees working overtime exhibit significantly higher attrition rates.
* Lower monthly income is strongly associated with employee turnover.
* Certain departments experience higher attrition compared to others.
* Early and mid-career employees demonstrate increased attrition risk.
* Job satisfaction and work-life balance are influential factors in employee retention.

---

## Technology Stack

| Category             | Technologies                |
| -------------------- | --------------------------- |
| Programming Language | Python                      |
| Data Analysis        | Pandas, NumPy               |
| Visualization        | Matplotlib, Seaborn, Plotly |
| Machine Learning     | Scikit-learn                |
| Web Application      | Streamlit                   |
| Version Control      | Git, GitHub                 |

---

## Project Structure

```text
employee-attrition-intelligence-platform/
│
├── data/
│   └── IBM_HR_Analytics.csv
│
├── notebooks/
│   ├── exploratory_data_analysis.ipynb
│   └── model_development.ipynb
│
├── src/
│   ├── app.py
│   ├── preprocessing.py
│   ├── train_model.py
│   └── model.pkl
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Model Performance

| Metric    | Score                    |
| --------- | ------------------------ |
| Accuracy  | 87%                      |
| Algorithm | Random Forest Classifier |

The model demonstrates strong predictive capability in identifying employees who may be at risk of attrition, supporting proactive workforce management strategies.

---

## Future Enhancements

* Integration of advanced ensemble models such as XGBoost and LightGBM.
* Deployment on cloud platforms for enterprise accessibility.
* Real-time employee attrition monitoring.
* Explainable AI techniques for prediction transparency.
* Automated HR recommendation system for retention strategies.

---

## Conclusion

The Employee Attrition Intelligence Platform combines data analytics, machine learning, and business intelligence to provide meaningful workforce insights. By identifying key attrition drivers and predicting turnover risk, organizations can make informed decisions to improve employee retention and optimize human resource strategies.
