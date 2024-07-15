import pandas as pd;
import joblib ;
import streamlit as st;

model = joblib.load('mj')

st.title(" House Price Prediction")



area = st.number_input("Enter the Area")
# bedroom = st.number_input("Enter the bedroom")

def prediction(area):
    P= model.predict([[area]])
    return P
if(st.button('predict')):
    result = prediction(area)
    st.success("The predicted price is {}".format(result))
