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


image = Image.open('header.jpg')

st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto") 

st.title("Lung Cancer Survival Prediction System")

st.caption("The following is a prototype survival prediction model that accepts genomic data and outputs a survivability in the form of a number between 0 and 1. A number greater than 0.5 indicates a survivability greater than 50%, while a number below 0.5 indicates a survivability less than 50%. Please upload your data in a .txt file format.", unsafe_allow_html=False) 

uploaded_file=st.file_uploader("Upload DNA Sequence Here", type=['txt'], accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)


if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    
    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

    # To read file as string:
    string_data = stringio.read()
    
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file, delimiter=",")
    st.write(dataframe)
    
    uploadbutton=st.button('Upload',disabled= False)
    
    if uploadbutton:
       st.write('Uploading(add progress bar here)') 
       
if st.button('Predict!'):
    df_json = json.loads(string_data)
    prediction = requests.post('http://backend:8080/prediction/', json=df_json, headers={"Content-Type":"application/json"})
    st.write(prediction) ##begin prediction and output results here
    st.write(prediction.text)
        


st.header('FAQ', anchor=None)

st.caption('WIP')

st.header('Acknowledgements', anchor=None)

st.caption('WIP')  

