import pickle
import streamlit as st

import pandas as pd
import numpy as np


st.write("""
# Youth Homeless in LA Prediction App

This app predicts whether a young individual will become homeless more than 1 year.

Data obtained from the [LA County Homeless Count Data Library](https://economicrt.org/publication/los-angeles-county-homeless-count-data-library/).

""")

st.sidebar.header('User Input Features')

st.sidebar.markdown("""
[Example CSV input file](https://github.com/dxk613/capstone_project/blob/main/datasets/youth_model.csv)
""")

# Collects user input features into dataframe
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    def user_input_features():
        island = st.sidebar.selectbox('Island',('Biscoe','Dream','Torgersen'))
        sex = st.sidebar.selectbox('Sex',('male','female'))
        bill_length_mm = st.sidebar.slider('Bill length (mm)', 32.1,59.6,43.9)
        bill_depth_mm = st.sidebar.slider('Bill depth (mm)', 13.1,21.5,17.2)
        flipper_length_mm = st.sidebar.slider('Flipper length (mm)', 172.0,231.0,201.0)
        body_mass_g = st.sidebar.slider('Body mass (g)', 2700.0,6300.0,4207.0)
        data = {'island': island,
                'bill_length_mm': bill_length_mm,
                'bill_depth_mm': bill_depth_mm,
                'flipper_length_mm': flipper_length_mm,
                'body_mass_g': body_mass_g,
                'sex': sex}
        features = pd.DataFrame(data, index=[0])
        return features
    input_df = user_input_features()
    
# Combines user input features with entire penguins dataset
# This will be useful for the encoding phase
youth_homeless = pd.read_csv('datasets/youth_model.csv')
youth = youth_homeless.drop(columns=['hmlsmorethan1Yr'])
df = pd.concat([input_df,youth],axis=0)

# Displays the user input features
st.subheader('User Input features')

if uploaded_file is not None:
    st.write(df)
else:
    st.write('Awaiting CSV file to be uploaded. Currently using example input parameters (shown below).')
    st.write(df)
        