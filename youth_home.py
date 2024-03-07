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

# Target = hmlsmorethan1Yr 
# Features = 'dv_neglect', 'dv_physical', 'dv_physical_rel', 'dv_sexual_rel', 'subsabuse', 'drugabuse', 'SPA'

# Collects user input features into dataframe
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    def user_input_features():
        neglect = st.sidebar.selectbox('Neglect',('Yes','No','Not Sure','Refuse to Answer'))
        physical_abuse = st.sidebar.selectbox('Physical Abuse',('Yes','No', 'Not Sure', 'Refuse to Answer'))
        dv_physical_rel = st.sidebar.slider('Physical Abuse By Parent', 0, 1, 6)
        dv_sexual_rel = st.sidebar.slider('Sexual Abuse By Parent', 0, 1, 6)
        subsabuse = st.sidebar.slider('Whether Did Substance Abuse', 0, 1, 6)
        drugabuse = st.sidebar.slider('Whether Did Drug Abuse', 0, 1, 2)
        SPA = st.sidebar.slider('Service Planning Area', 0, 1, 8)
        data = {'dv_neglect': neglect,
                'dv_physical_rel': dv_physical_rel,
                'dv_sexual_rel': dv_sexual_rel,
                'subsabuse': subsabuse,
                'drugabuse': drugabuse,
                'SPA': SPA,
                'dv_physical': physical_abuse}
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
        