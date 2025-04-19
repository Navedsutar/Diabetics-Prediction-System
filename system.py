import numpy as np
import pickle
import pandas as pd

# Load the trained model
with open('trained_model.sav', 'rb') as file:
    loaded_model = pickle.load(file)

# # Input data for prediction
# input_data = (1, 103, 30, 38, 83, 43.3, 0.183, 33)

# # Define the feature names in the same order as used in training
# columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
#            'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

# # Convert input data to a DataFrame to avoid warning
# input_df = pd.DataFrame([input_data], columns=columns)

# # Make prediction
# prediction = loaded_model.predict(input_df)

# # Output the result
# print(prediction)
# if prediction[0] == 0:
#     print('The person is not diabetic')
# else:
#     print('The person is diabetic')
