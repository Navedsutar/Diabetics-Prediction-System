import streamlit as st
import numpy as np
import pickle

# Load the trained model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

def diabetes_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data, dtype=float)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    return 'The person is diabetic' if prediction[0] == 1 else 'The person is not diabetic'

def main():
    st.set_page_config(page_title='Diabetes Prediction System', layout='centered')
    st.title('Diabetes Prediction System')
    st.markdown('Enter the required details to predict diabetes:')

    # User input fields
    col1, col2 = st.columns(2)
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1)
        Glucose = st.number_input('Glucose Level (mg/dL)', min_value=0, step=1)
        BloodPressure = st.number_input('Blood Pressure (mm Hg)', min_value=0, step=1)
        SkinThickness = st.number_input('Skin Thickness (mm)', min_value=0, step=1)

    with col2:
        Insulin = st.number_input('Insulin Level (mu U/ml)', min_value=0, step=1)
        BMI = st.number_input('BMI value (kg/m²)', min_value=0.0, step=0.1)
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', min_value=0.0, step=0.01)
        Age = st.number_input('Age of the Person', min_value=0, step=1)

    # Threshold-based warnings/info
    st.markdown("---")
    st.subheader("Health Insights Based on Your Input:")

    if Glucose >= 126:
        st.warning("High Glucose Level: May indicate diabetes.")
    elif 100 <= Glucose < 126:
        st.info("Glucose in pre-diabetic range.")

    if BloodPressure < 60:
        st.warning("Low Blood Pressure: Below normal range.")
    elif BloodPressure > 90:
        st.warning("High Blood Pressure: Could be a health risk.")

    if BMI >= 30:
        st.warning("High BMI: Obesity increases diabetes risk.")
    elif 25 <= BMI < 30:
        st.info("Overweight range.")

    if Age >= 45:
        st.info("Age above 45 increases diabetes risk.")

    if Insulin != 0 and (Insulin < 16 or Insulin > 166):
        st.warning("Insulin level is outside typical range (16-166 mu U/ml).")

    if SkinThickness > 50:
        st.warning("Skin Thickness is quite high (typically < 50 mm).")

    if DiabetesPedigreeFunction > 1.0:
        st.info("High Diabetes Pedigree Function: Strong family history risk.")

    st.markdown("---")
    
    diagnosis = ''
    if st.button('Predict Diabetes'):
        input_values = [
            Pregnancies, Glucose, BloodPressure,
            SkinThickness, Insulin, BMI,
            DiabetesPedigreeFunction, Age
        ]
        diagnosis = diabetes_prediction(input_values)

    if diagnosis:
        st.success(diagnosis)

if __name__ == '__main__':
    main()
