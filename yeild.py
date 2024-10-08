import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load the trained model and preprocessor
model = joblib.load(r'C:\Users\sahil\OneDrive\Documents\AgriArogya\dtr.pkl')  # Update the path if needed
preprocessor = joblib.load(r'C:\Users\sahil\OneDrive\Documents\AgriArogya\preprocessor.pkl')

# Function to handle the app logic
def app():
    st.title("Crop Yield Prediction 🌾")

    st.write("### Enter the following details to predict crop yield")

    # Create user input fields for all required features
    year = st.number_input("Year", min_value=1900, max_value=2100, step=1)
    rainfall = st.number_input("Average Rainfall (mm)", min_value=0.0, max_value=5000.0, step=0.1)
    pesticides = st.number_input("Pesticides used (tonnes)", min_value=0.0, max_value=1000.0, step=0.1)
    avg_temp = st.number_input("Average Temperature (°C)", min_value=-10.0, max_value=50.0, step=0.1)
    area = st.text_input("Area", "")
    item = st.text_input("Item (Crop Type)", "")

    # When the user clicks the "Predict" button
    if st.button("Predict Yield"):
        # Use the input directly as the crop type
        crop = item.strip()

        if crop:
            # Convert the input to DataFrame with proper column names
            input_data = pd.DataFrame({
                'Year': [year],
                'average_rain_fall_mm_per_year': [rainfall],
                'pesticides_tonnes': [pesticides],
                'avg_temp': [avg_temp],
                'Area': [area],
                'Item': [crop]  # Use individual crop
            })

            try:
                # Process the user input using the preprocessor
                processed_data = preprocessor.transform(input_data)

                # Predict the yield using the model
                prediction = model.predict(processed_data)
                st.success(f"Predicted Crop Yield for {crop}: {prediction[0]:.2f} tons per hectare")

            except Exception as e:
                st.error(f"Error during prediction for {crop}: {e}")
        else:
            st.warning("Please enter a valid crop type.")

    # Add a sidebar with navigation options
    st.sidebar.title("Navigation")
    st.sidebar.info("Use this app to predict crop yield based on soil and climate data.")

# No need to call app() here; it will be called from app.py
