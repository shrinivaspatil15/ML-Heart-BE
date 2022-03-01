from click import option
import streamlit as st
import numpy as np
import pickle

def show_predict_page():
    st.title("Cardiovascular disease prediction using Machine Learning")

    st.write("""### For prediction, we need this data to be filled ###""")

    sexOP = {
        'Male',
        'Female'
    }

    

    # st.write('You selected:', sex)
    
    
    fbsOP = {
        "No",
        "Yes"
    }

    ecgOP = {
        "Normal",
        "ST-T wave abnormality",
        "Definite left ventricular hypertrophy"
    }

    exangOP = {
        "No",
        "Yes"
    }

    cpOP = {
        "Asymptomatic(No Chest Pain)",
        "Atypical Angina(Not severe but discomfort in chest)",
        "Non-Anginal chest pain",
        "Typical Angina(Physical or Emotional Stress)"
    }

    slopeOP = {
        "Downsloping",
        "Flat",
        "Upsloping"
    }

    caOP = {
        "0",
        "1",
        "2",
        "3",
        "4"
    }

    thalOP = {
        "Fixed defect (no blood flow in some part of the heart)",
        "Normal blood flow",
        "Reversible defect (a blood flow is observed but it is not normal)"
    }

    name = st.text_input("Enter your Full Name")
    age = st.slider("Enter your age", min_value=25, max_value=80)
    sex = st.selectbox("Gender: ", sexOP)
    cp = st.selectbox("Select the Chest Pain Type",cpOP) 
    trestbps = st.text_input("Enter your Resting Blood Pressure (in mmHG)")
    chol = st.text_input("Enter your Serum Cholestrol (in mg/dl)")
    fbs = st.selectbox("Is your Fasting Blood Sugar > 120mg/dl?",fbsOP)
    restecg = st.selectbox("Resting ECG results?",ecgOP)
    thalach = st.text_input("Maximum Heart Rate Achieved during ECG")
    exang = st.selectbox("Chest Pain during Exercise?",exangOP)
    oldpeak = st.text_input("ST depression induced by exercise relative to rest")
    slope = st.selectbox("The slope of the peak exercise ST segment", slopeOP)
    ca = st.selectbox("The number of major vessels", caOP)
    thal = st.selectbox("A blood disorder called thalassemia", thalOP)
        
    predict = st.button("Predict")

    if predict:
        age = int(age)

        sex = 1 if sex=="Male" else 0

        if cp=="Asymptomatic(No Chest Pain)":
            cp = 3
        elif cp=="Atypical Angina(Not severe but discomfort in chest)":
            cp = 1
        elif cp=="Non-Anginal chest pain":
            cp = 2
        elif cp=="Typical Angina(Physical or Emotional Stress)":
            cp = 0

        trestbps = int(trestbps)

        chol = int(chol)

        fbs = 1 if fbs=="Yes" else 0

        if restecg=="Normal":
            restecg = 0
        elif restecg=="ST-T wave abnormality":
            restecg = 1
        elif restecg=="Definite left ventricular hypertrophy":
            restecg = 2

        thalach = int(thalach)

        exang = 1 if exang=="Yes" else 0

        if slope=="Downsloping":
            slope=2
        elif slope=="Flat":
            slope=1
        elif slope=="Upsloping":
            slope=0

        ca = int(ca)

        if thal=="Fixed defect (no blood flow in some part of the heart)":
            thal = 2
        elif thal=="Normal blood flow":
            thal = 1
        elif thal=="Reversible defect (a blood flow is observed but it is not normal)":
            thal = 3

        st.write("Age : {}".format(age))
        st.write("Sex : {}".format(sex))
        st.write("CP : {}".format(cp))
        st.write("Resting BP : {}".format(trestbps))
        st.write("Cholestrol : {}".format(chol))
        st.write("Fasting Blood Sugar : {}".format(fbs))
        st.write("Resting ECG : {}".format(restecg))
        st.write("Thalach : {}".format(thalach))
        st.write("Exercise Induced Angina : {}".format(exang))
        st.write("Old Peak : {}".format(oldpeak))
        st.write("Slope : {}".format(slope))
        st.write("Number of major vessel : {}".format(ca))
        st.write("Thal : {}".format(thal))

        userdata = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        with open('savedModel.pkl', 'rb') as modelFile:
            modelData = pickle.load(modelFile)

        classifier = modelData["model"]
        prediction = classifier.predict(userdata)

        if prediction[0]==1:
            st.write("""###Heart Disease Detected###""")
        else:
            st.write("""###Heart Disease Not Detected###""")
        st.write(prediction[0])

        


