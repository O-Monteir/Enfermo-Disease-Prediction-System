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
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction value')
    Age = st.text_input('Age') 
     
    
if (selected == 'Heart Disease Prediction'):
    #page title
    st.title('Heart Disease Prediction')
    
    Pregnancies = st.text_input('Age')
    Glucose = st.text_input('Sex')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction value')
    Age = st.text_input('Age')
   