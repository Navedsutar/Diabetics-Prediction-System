import streamlit as st
import numpy as np
import pickle

# Load the trained model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

def diabetes_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data, dtype=float)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    return prediction[0] == 1  # Returns True if diabetic, False if not

def main():
    # Custom CSS for tight layout and styling
    st.markdown("""
    <style>
        /* Layout adjustments */
        html, body, [class*="css"] {
            overflow: hidden !important;
            width: 100% !important;
            margin: 0 !important;
            padding: 0 !important;
        }
        
        .main {
            background-color: #f5f7fa;
            padding: 1rem 5% !important;
            height: 100vh !important;
            overflow: auto !important;
        }
        
        .main::-webkit-scrollbar {
            display: none !important;
        }
        
        .stApp {
            max-width: 100% !important;
            padding: 0 !important;
            margin: 0 auto !important;
        }
        
        .st-emotion-cache-1y4p8pa {
            width: 100% !important;
            max-width: 1200px !important;
            margin: 0 auto !important;
            padding: 0 5% !important;
        }
        
        /* Health insights tight spacing */
        .stAlert {
            margin: 0.25rem 0 !important;
            padding: 0.5rem 1rem !important;
            font-size: 0.9rem !important;
            border-radius: 6px !important;
        }
        
        /* Improved risk messaging */
        .risk-high {
            background-color: #e74c3c !important;
            color: white !important;
            padding: 1.5rem !important;
            border-radius: 10px !important;
            text-align: center !important;
            margin: 1rem 0 !important;
        }
        
        .risk-low {
            background-color: #2ecc71 !important;
            color: white !important;
            padding: 1.5rem !important;
            border-radius: 10px !important;
            text-align: center !important;
            margin: 1rem 0 !important;
        }
        
        div.stButton > button:first-child {
        background-color: #007bff !important;
        color: white !important;
        border: none !important;
        padding: 0.75rem 1.5rem !important;
        font-weight: bold;
        border-radius: 8px;
        }
        
        /* Other existing styles... */
    </style>
    """, unsafe_allow_html=True)

    # Header Section
    st.markdown("""
    <div style="text-align: center; margin-bottom: 1.5rem;">
        <img src="https://img.icons8.com/color/96/000000/diabetes.png" width="80">
        <h1 style="margin: 0.5rem 0 0.25rem 0;">Diabetes Risk Assessment</h1>
        <p style="color: #666; margin: 0;">Get your personalized diabetes risk analysis</p>
    </div>
    """, unsafe_allow_html=True)

    # Health Information Section
    st.markdown("---")
    st.subheader("Your Health Metrics")
    
    col1, col2 = st.columns(2, gap="large")
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1)
        Glucose = st.number_input('Glucose Level (mg/dL)', min_value=0, step=1)
        BloodPressure = st.number_input('Blood Pressure (mm Hg)', min_value=0, step=1)
        SkinThickness = st.number_input('Skin Thickness (mm)', min_value=0, step=1)

    with col2:
        Insulin = st.number_input('Insulin Level (mu U/ml)', min_value=0, step=1)
        BMI = st.number_input('BMI value (kg/m²)', min_value=0.0, step=0.1)
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', min_value=0.0, step=0.01)
        Age = st.number_input('Age (years)', min_value=0, step=1)

    # Health Insights Section - Tightly Spaced
    st.markdown("---")
    st.subheader("Health Indicators")
    
    # Create container for tight spacing
    insights_container = st.container()
    with insights_container:
        if Glucose > 0:
            if Glucose >= 126:
                st.warning("⚠️ Elevated Glucose: Fasting level suggests diabetes risk (≥126 mg/dL)")
            elif 100 <= Glucose < 126:
                st.info("ℹ️ Borderline Glucose: Pre-diabetic range (100-125 mg/dL)")
            else:
                st.success("✓ Normal Glucose: Within healthy range")

        if BloodPressure > 0:
            if BloodPressure < 60:
                st.warning("⚠️ Low Blood Pressure: Below normal range")
            elif BloodPressure > 90:
                st.warning("⚠️ Elevated Blood Pressure: Above optimal range")
            else:
                st.success("✓ Normal Blood Pressure: Within healthy range")

        if BMI > 0:
            if BMI >= 30:
                st.warning("⚠️ Obesity: Significant diabetes risk factor (BMI ≥30)")
            elif 25 <= BMI < 30:
                st.info("ℹ️ Overweight: Moderate risk factor (BMI 25-29.9)")
            else:
                st.success("✓ Healthy Weight: Lower diabetes risk")

        if Age >= 45:
            st.info("ℹ️ Age Factor: Increased risk after 45 years")

        if Insulin != 0 and (Insulin < 16 or Insulin > 166):
            st.warning("⚠️ Atypical Insulin: Outside normal range (16-166 mu U/ml)")

    # Prediction Section
    st.markdown("---")
    st.subheader("Risk Analysis")
    
    if st.button('Calculate My Diabetes Risk', use_container_width=True, type='primary'):
        with st.spinner('Analyzing your health profile...'):
            input_values = [
                Pregnancies, Glucose, BloodPressure,
                SkinThickness, Insulin, BMI,
                DiabetesPedigreeFunction, Age
            ]
            is_diabetic = diabetes_prediction(input_values)
            
            # Improved Risk Messaging
            if is_diabetic:
                st.markdown("""
                <div class="risk-high">
                    <h2 style="margin: 0 0 0.5rem 0;">🛑 Significant Diabetes Risk Detected</h2>
                    <p style="margin: 0;">Based on your metrics, you show signs of potential diabetes.</p>
                </div>
                <div style="text-align: center; margin: 1rem 0 1.5rem 0;">
                    <p>This suggests a high likelihood of diabetes. We strongly recommend:</p>
                    <p>• Consulting a healthcare provider promptly</p>
                    <p>• Getting formal diagnostic testing</p>
                    <p>• Beginning preventive measures</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="risk-low">
                    <h2 style="margin: 0 0 0.5rem 0;">✅ Low Diabetes Risk Identified</h2>
                    <p style="margin: 0;">Your metrics suggest low current risk for diabetes.</p>
                </div>
                <div style="text-align: center; margin: 1rem 0 1.5rem 0;">
                    <p>While your risk appears low, we recommend:</p>
                    <p>• Maintaining healthy lifestyle habits</p>
                    <p>• Annual screening if over 45 years</p>
                    <p>• Monitoring if family history exists</p>
                </div>
                """, unsafe_allow_html=True)
            
            # Recommendations
            st.markdown("---")
            st.subheader("Personalized Guidance")
            
            col1, col2 = st.columns(2, gap="large")
            with col1:
                st.markdown("""
                **For Everyone:**
                - Regular physical activity (150 mins/week)
                - Balanced, portion-controlled meals
                - Annual comprehensive check-ups
                - Stress management techniques
                """)
            
            with col2:
                if is_diabetic:
                    st.markdown("""
                    **If High Risk:**
                    - HbA1c and glucose testing
                    - Nutritionist consultation
                    - Regular foot/eye exams
                    - Blood pressure monitoring
                    """)
                else:
                    st.markdown("""
                    **Prevention Focus:**
                    - Limit processed carbohydrates
                    - Increase fiber intake
                    - Maintain healthy weight
                    - Avoid sugary beverages
                    """)

    # Footer
    st.markdown("""
    <div style="text-align: center; color: #666; font-size: 0.85rem; margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #eee;">
        <p>This assessment tool provides risk estimation only, not a diagnosis.</p>
        <p>Results should be discussed with your healthcare provider.</p>
        <p>© 2023 DiabetesPredict | Terms & Privacy</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()