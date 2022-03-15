# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from fastapi import FastAPI
import requests
import json
import streamlit as st
import pandas as pd
from io import StringIO
from PIL import Image
import logging


image = Image.open('header.jpg')

st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto") 

st.title("Lung Cancer Survival Prediction System")

st.caption("The following is a prototype survival prediction model that accepts genomic data and outputs a survivability in the form of a number between 0 and 1. A number greater than 0.5 indicates a survivability greater than 50%, while a number below 0.5 indicates a survivability less than 50%. Please upload your data in a .txt file format.", unsafe_allow_html=False) 

uploaded_file=st.file_uploader("Upload DNA Sequence Here", type=['txt'], accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)


if uploaded_file is not None:
    
    # To convert to a string based IO:
    #stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

    # To read file as string:
    #string_data = stringio.read()
    
    # conver txt file to pandas dataframe
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
    
    uploadbutton=st.button('Upload',disabled= False) 
       
if st.button('Predict!'):
    data = dataframe.to_dict(orient='records')
    payload = data[0]
    prediction = requests.post("http://backend:8080/prediction/", json=payload, headers={"Content-Type": "application/json"})
    st.write(prediction.status_code)
    st.write(prediction)


st.header('FAQ', anchor=None)

st.caption('WIP')

st.header('Acknowledgements', anchor=None)

st.caption('WIP')  

