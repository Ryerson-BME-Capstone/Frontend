# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd
from io import StringIO


st.title("Lung Cancer Survival Prediction System")



uploaded_file=st.file_uploader("Upload DNA Sequence Here", type=['txt'], accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)


if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)
    
    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
    
    uploadbutton=st.button('Upload',disabled= False)
    
    if uploadbutton:
       st.write('Uploading(add progress bar here)') 

