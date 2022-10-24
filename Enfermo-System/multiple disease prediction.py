# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:45:10 2022

@author: Malaika Monteiro
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models

diabetes_model = pickle.load(open('E:/Python/Enfermo-System/saved models/diabetes_model.sav','rb'))
heart_disease_model=pickle.load(open('E:/Python/Enfermo-System/saved models/heart_model.sav','rb'))

#sidebar for navigation

with st.sidebar:
    selected =option_menu('Enfermo Disease Prediction System',['Diabetes Prediction','Heart Disease Prediction'],icons=['activity','heart'],default_index=0)
    
#Diabetes Prediction page

if (selected=='Diabetes Prediction'):
    #page title
    st.title('Diabetes Prediction')
   
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Patients Age')  
    
    #code for prediction
    diab_diagnosis=''
    
    #creating button for prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction=diabetes_model.predict([[Pregnancies]])
     
    
if (selected == 'Heart Disease Prediction'):
    #page title
    st.title('Heart Disease Prediction')
    
    Pregnancies = st.text_input('Age')
    Glucose = st.text_input('Sex')
    BloodPressure = st.text_input('Chest Pain Type (4 values)')
    SkinThickness = st.text_input('Resting Blood Pressure value')
    Insulin = st.text_input('Serum Cholestoral in mg/dl ')
    BMI = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    DiabetesPedigreeFunction = st.text_input('Resting Electrocardiographic Results (values 0,1,2)')
    Age = st.text_input('Maximum Heart Rate Achieved ')
    Insulin = st.text_input('Exercise Induced Angina ')
    BMI = st.text_input('oldpeak = ST depression induced by exercise relative to rest ')
    DiabetesPedigreeFunction = st.text_input('The slope of the peak exercise ST segment ')
    Age = st.text_input('Number of major vessels (0-3) colored by flourosopy ') 
     
   