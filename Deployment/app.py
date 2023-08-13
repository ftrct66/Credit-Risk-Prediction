import streamlit as st
import pandas as pd
import numpy  as np
import joblib
import sklearn

st.header('Credit Risk Prediction')


@st.cache_data
def fetch_data():
    df = pd.read_csv("BankChurners.csv")
    return df

df = fetch_data()

Customer_Age = st.number_input('Customer_Age', value=0)
Gender = st.selectbox('Gender', df['Gender'].unique())
Dependent_count = st.number_input('Dependent_count', value=0)
Income_Category = st.selectbox('Income_Category', df['Income_Category'].unique())
Card_Category = st.selectbox('Card_Category', df['Card_Category'].unique())
Months_on_book = st.number_input('Months_on_book', value=0)
Credit_Limit = st.number_input('Credit_Limit', value=0)
Avg_Open_To_Buy = st.number_input('Avg_Open_To_Buy', value=0)
Total_Trans_Amt = st.number_input('Total_Trans_Amt', value=0)
Total_Trans_Ct = st.number_input('Total_Trans_Ct', value=0)
Avg_Utilization_Ratio = st.number_input('Avg_Utilization_Ratio', value=0)

data = {
    'Customer_Age': Customer_Age,
    'Gender': Gender,
    'Dependent_count': Dependent_count,
    'Income_Category': Income_Category,
    'Card_Category': Card_Category,
    'Months_on_book': Months_on_book,
    'Credit_Limit': Credit_Limit,
    'Avg_Open_To_Buy': Avg_Open_To_Buy,
    'Total_Trans_Amt': Total_Trans_Amt,
    'Total_Trans_Ct': Total_Trans_Ct,
    'Avg_Utilization_Ratio': Avg_Utilization_Ratio,
}
input = pd.DataFrame(data, index=[0])

st.subheader('Nasabah`s Data')
st.write(input)

load_model = joblib.load("best_model.pkl")

if st.button('Priority'):
    prediction = load_model.predict(input)

    if prediction == 0:
        prediction = 'Low Risk'
    else:
        prediction = 'High Risk'

    st.write('based on nasabah`s data, the prediction of priority is: ')
    st.write(prediction)