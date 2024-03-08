import pickle
import streamlit as st

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, GridSearchCV
from imblearn.pipeline import make_pipeline
from imblearn.over_sampling import RandomOverSampler
from sklearn.svm import SVC


st.write("""
# Homeless Youth in LA Prediction App

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
        neglect = st.sidebar.slider('Neglect', 0, 1, 6)
        physical_abuse = st.sidebar.slider('Physical Abuse', 0, 1, 6)
        dv_physical_rel = st.sidebar.slider('Physical Abuse By Parent', 0, 1, 6)
        dv_sexual_rel = st.sidebar.slider('Sexual Abuse By Parent', 0, 1, 6)
        subsabuse = st.sidebar.slider('Whether Did Substance Abuse', 0, 1, 6)
        drugabuse = st.sidebar.slider('Whether Did Drug Abuse', 0, 1, 2)
        SPA = st.sidebar.slider('Service Planning Area', 0, 1, 8)
        data = {'dv_neglect': neglect,
                'dv_physical': physical_abuse,
                'dv_physical_rel': dv_physical_rel,
                'dv_sexual_rel': dv_sexual_rel,
                'subsabuse': subsabuse,
                'drugabuse': drugabuse,
                'SPA': SPA
                }
        features = pd.DataFrame(data, index=[0])
        return features
    input_df = user_input_features()
    
# Combines user input features with entire youth_model dataset
# This will be useful for the encoding phase
youth_homeless = pd.read_csv('datasets/youth_model.csv')
youth = youth_homeless.drop(columns=['hmlsmorethan1Yr'])
df = pd.concat([input_df,youth],axis=0)
df = df[:1] # Selects only the first row (the user input data)


# Displays the user input features
st.subheader('User Input features')

if uploaded_file is not None:
    st.write(df)
else:
    st.write('Awaiting CSV file to be uploaded. Currently using example input parameters (shown below).')
    st.write(df)

# Load your dataset
youth_model = pd.read_csv("datasets/youth_model.csv")

# Define features (X) and target variable (y)
features = ['dv_neglect', 'dv_physical', 'dv_physical_rel', 'dv_sexual_rel', 'subsabuse', 'drugabuse', 'SPA']
target = 'hmlsmorethan1Yr'

X = youth_model[features]
y = youth_model[target]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)

# Load the grid search object
with open('youth_pipe.pkl', 'rb') as file:
    gs = pickle.load(file)

gs = SVC(probability=True)
# Fit the model to your data
gs.fit(X_train, y_train) 

# Apply model to make predictions
prediction = gs.predict(df)
prediction_proba = gs.predict_proba(df)

st.subheader('Prediction')
homeless_more_than_1_year = np.array(['No','Yes'])
st.write(homeless_more_than_1_year[prediction])

st.subheader('Prediction Probability')
st.write(prediction_proba)