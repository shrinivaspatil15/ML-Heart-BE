from click import option
import streamlit as st
import numpy as np

def show_predict_page():
    st.title("Cardiovascular disease prediction using Machine Learning")

    st.write("""### For prediction, we need this data to be filled ###""")

    
    with st.form("form1", clear_on_submit=True):
        name = st.text_input("Enter your Full Name")
        option = st.selectbox(
            'What is your gender?',
                ('Male', 'Female'))

        st.write('You selected:', option)
        age = st.slider("Enter your age", min_value=10, max_value=100)
        Resting_blood_pressure = st.text_input("Enter your Resting Blood Pressure (in mmHG)")
        Serum_cholestrol = st.text_input("Enter your Serum Cholestrol (in mg/dl)")

        option = st.selectbox(
            'Is your Fasting Blood Sugar > 120mg/dl?',
                ('Yes', 'No'))

        option = st.selectbox(
            'Resting ECG results?',
                ('Normal', 'ST-T wave abnormality', 'Definite left ventricular hypertrophy'))
        
        Heart_rate = st.text_input("Maximum Heart Rate Achieved during ECG")
        
        option = st.selectbox(
            'Chest Pain during Exercise?',
                ('Yes', 'No'))

        option = st.selectbox(
            'Select the Chest Pain Type?',
                ('No Chest Pain', 'Typical Angina(Physical or Emotional Stress)','Atypical Angina(Not severe but discomfort in chest)', 'Non-Anginal chest pain', 'Asymptomatic(None of the above apply'))

        submit = st.form_submit_button("Submit")
       

