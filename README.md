# Employee Attrition Intelligence Platform

## Live Demo

🔗 https://employee-attrition-intelligence.onrender.com

## Project Overview

Employee attrition is a major challenge for organizations as it affects productivity, workforce stability, and operational costs. This project uses data analytics and machine learning to identify factors influencing employee turnover and predict employees who are at risk of leaving the organization.

Using the IBM HR Analytics Employee Attrition dataset, the project performs exploratory data analysis, predictive modeling, and interactive visualization to generate actionable workforce insights.

---

## Objectives

* Analyze employee demographics, compensation, and workplace factors affecting attrition.
* Identify trends and patterns associated with employee turnover.
* Build a machine learning model to predict attrition risk.
* Develop an interactive dashboard for workforce analytics.

---

## Dataset Information

**Dataset:** IBM HR Analytics Employee Attrition Dataset

* Total Records: 1,470 Employees
* Features: 35 Employee Attributes
* Target Variable: Attrition (Yes/No)
* Missing Values: None

---

## Technology Stack

| Category             | Technologies  |
| -------------------- | ------------- |
| Programming Language | Python        |
| Data Analysis        | Pandas, NumPy |
| Visualization        | Plotly        |
| Machine Learning     | Scikit-learn  |
| Dashboard            | Streamlit     |
| Deployment           | Render        |
| Version Control      | Git, GitHub   |

---

## Key Features

* Employee attrition analysis and trend identification
* Department-wise attrition monitoring
* Income and overtime impact analysis
* Age distribution and workforce insights
* Interactive filtering using Streamlit
* Machine learning-based attrition prediction
* Public deployment using Render

---

## Machine Learning Model

**Algorithm:** Random Forest Classifier

**Performance:**

* Accuracy: ~87%
* Binary Classification (Attrition: Yes/No)

The model helps identify employees who may be at risk of attrition, enabling proactive workforce management.

---

## Key Insights

* Employees working overtime exhibit higher attrition rates.
* Lower monthly income is associated with increased turnover.
* Certain departments experience higher attrition than others.
* Early and mid-career employees show elevated attrition risk.
* Job satisfaction and work-life balance significantly influence retention.

---

## Project Structure

```text
employee-attrition-intelligence/
│
├── data/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
│
├── src/
│   ├── app.py
│   └── model.pkl
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

```bash
git clone https://github.com/dhikshitha20/employee-attrition-intelligence.git

cd employee-attrition-intelligence

pip install -r requirements.txt

streamlit run src/app.py
```

---

## Future Enhancements

* XGBoost and LightGBM implementation
* Explainable AI (SHAP)
* Real-time HR analytics
* Employee retention recommendation system
* Advanced workforce forecasting

---

## Links

* GitHub Repository: https://github.com/dhikshitha20/employee-attrition-intelligence
* Live Demo: https://employee-attrition-intelligence.onrender.com

---

## Conclusion

The Employee Attrition Intelligence Platform combines data analytics, machine learning, and business intelligence to provide workforce insights and attrition risk prediction. The solution enables data-driven HR decision-making and supports employee retention strategies.
