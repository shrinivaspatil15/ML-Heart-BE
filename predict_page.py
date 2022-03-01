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

        fbsOP = {
            "No",
            "Yes"
        }

        ecgOP = {
            "Normal",
            "ST-T wave abnormality",
            "Definite left ventricular hypertrophy"

        }

        cpOP = {
            "No",
            "Yes"
        }

        cptOP = {
            "No Chest Pain",
            "Typical Angina(Physical or Emotional Stress)",
            "Atypical Angina(Not severe but discomfort in chest)",
            "Non-Anginal chest pain",
            "Asymptomatic(None of the above apply"
        }
        
        fbs = st.selectbox("Is your Fasting Blood Sugar > 120mg/dl?",fbsOP)

        ecg = st.selectbox("Resting ECG results?",ecgOP)
        
        Heart_rate = st.text_input("Maximum Heart Rate Achieved during ECG")
        
        cp = st.selectbox("Chest Pain during Exercise?",cpOP)

        cpt = st.selectbox("Select the Chest Pain Type?",cptOP)

        predict = st.form_submit_button("Predict")
       

