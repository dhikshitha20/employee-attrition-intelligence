import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pickle

st.set_page_config(page_title="Employee Attrition Intelligence Platform", layout="wide")

st.markdown("""
    <style>
    div[data-testid="stMetric"] {
        border: 1px solid #3a3a4a;
        border-radius: 10px;
        padding: 15px;
        background-color: #1a1a2e;
    }
    div[data-testid="stPlotlyChart"] {
        border: 1px solid #3a3a4a;
        border-radius: 10px;
        padding: 10px;
        background-color: #1a1a2e;
        overflow: hidden;
    }
    </style>
""", unsafe_allow_html=True)

df = pd.read_csv('../data/WA_Fn-UseC_-HR-Employee-Attrition.csv')
df['Attrition_num'] = df['Attrition'].map({'Yes': 1, 'No': 0})

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Employee Attrition Intelligence Platform")
st.markdown("Analyzing workforce patterns to identify attrition risk factors")
st.divider()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Employees", len(df))
col2.metric("Attrition Rate", f"{df['Attrition_num'].mean()*100:.1f}%")
col3.metric("Avg Monthly Income", f"${df['MonthlyIncome'].mean():,.0f}")
col4.metric("Avg Age", f"{df['Age'].mean():.0f} yrs")
st.divider()

st.sidebar.header("Filters")
dept = st.sidebar.selectbox("Department", ['All'] + list(df['Department'].unique()))
overtime = st.sidebar.selectbox("Overtime", ['All', 'Yes', 'No'])

filtered_df = df.copy()
if dept != 'All':
    filtered_df = filtered_df[filtered_df['Department'] == dept]
if overtime != 'All':
    filtered_df = filtered_df[filtered_df['OverTime'] == overtime]

st.subheader(f"Showing {len(filtered_df)} employees")

col5, col6 = st.columns(2)

with col5:
    dept_rate = filtered_df.groupby('Department')['Attrition_num'].mean().reset_index()
    dept_rate.columns = ['Department', 'Attrition Rate']
    dept_rate['Attrition Rate'] = (dept_rate['Attrition Rate'] * 100).round(1)
    fig1 = px.bar(dept_rate, x='Department', y='Attrition Rate',
                  title='Attrition Rate by Department (%)',
                  color='Attrition Rate', color_continuous_scale='Reds')
    st.plotly_chart(fig1, use_container_width=True)

with col6:
    fig2 = px.histogram(filtered_df, x='Age', color='Attrition',
                        title='Age Distribution by Attrition',
                        barmode='overlay', opacity=0.7,
                        color_discrete_map={'Yes': 'tomato', 'No': 'steelblue'})
    st.plotly_chart(fig2, use_container_width=True)

col7, col8 = st.columns(2)

with col7:
    fig3 = px.box(filtered_df, x='Attrition', y='MonthlyIncome',
                  title='Monthly Income vs Attrition',
                  color='Attrition',
                  color_discrete_map={'Yes': 'tomato', 'No': 'steelblue'})
    st.plotly_chart(fig3, use_container_width=True)

with col8:
    ot = filtered_df.groupby(['OverTime', 'Attrition']).size().reset_index(name='Count')
    fig4 = px.bar(ot, x='OverTime', y='Count', color='Attrition',
                  title='Overtime vs Attrition',
                  barmode='group',
                  color_discrete_map={'Yes': 'tomato', 'No': 'steelblue'})
    st.plotly_chart(fig4, use_container_width=True)

st.divider()
st.subheader("Raw Employee Data")
st.dataframe(filtered_df, use_container_width=True)