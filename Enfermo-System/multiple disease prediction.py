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
    
    #columns for input field
    col1,col2,col3 =st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Patients Age')  

   
    
    
    
    
    
    
    
  
    
    #code for prediction
    diab_diagnosis=''
    
    #creating button for prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction=diabetes_model.predict([[Pregnancies, Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if(diab_prediction[0]==1):
            diab_diagnosis='The person is Diabetic'
        else:
            diab_diagnosis='The person is not Diabetic'
        
    st.success(diab_diagnosis)
    
if (selected == 'Heart Disease Prediction'):
    #page title
    st.title('Heart Disease Prediction')
    
    #columns for input field
    col1,col2,col3 =st.columns(3)
    
    with col1:
        age = st.number_input('Age')
    with col2:
        sex = st.number_input('Sex')
    with col3:
        cp = st.number_input('Chest Pain Type (4 values)')
    with col1:
        trestbps = st.number_input('Resting Blood Pressure value')
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl ')
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.number_input('Resting Electrocardiographic Results')
    with col2:
        thalach = st.number_input('Maximum Heart Rate Achieved ')
    with col3:
        exang = st.number_input('Exercise Induced Angina ')
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')
    with col2:
        slope = st.number_input('The slope of the peak exercise ST segment ')
    with col3:
        ca = st.number_input('Number of vessels colored by flourosopy ')
    with col1:
        thal =st.number_input('thal:0 = normal; 1 = fixed defect; 2 = reversible defect')
   
    
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person has a heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
    
    
    
    
   
    
    
     
     
   