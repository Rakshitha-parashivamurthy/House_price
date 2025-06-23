import streamlit as st
import numpy as np
import joblib

# Load the saved model
model = joblib.load('house_price_model.pkl')

# Title
st.title("🏠 House Price Prediction App")

# Input fields
st.header("Enter House Features")

OverallQual = st.slider("Overall Quality (1-10)", 1, 10, 5)
GrLivArea = st.number_input("Above Ground Living Area (sq ft)", 500, 5000, 1500)
GarageCars = st.slider("Garage Capacity (cars)", 0, 4, 2)
GarageArea = st.number_input("Garage Area (sq ft)", 0, 1500, 500)
TotalBsmtSF = st.number_input("Total Basement Area (sq ft)", 0, 3000, 800)
FirstFlrSF = st.number_input("1st Floor Area (sq ft)", 0, 3000, 1000)
FullBath = st.slider("Number of Full Bathrooms", 0, 4, 2)
TotRmsAbvGrd = st.slider("Total Rooms Above Ground", 1, 14, 6)
YearBuilt = st.slider("Year Built", 1900, 2025, 2000)

# Predict button
if st.button("Predict Sale Price"):
    input_data = np.array([[OverallQual, GrLivArea, GarageCars, GarageArea,
                            TotalBsmtSF, FirstFlrSF, FullBath, TotRmsAbvGrd, YearBuilt]])
    
    prediction = model.predict(input_data)[0]
    st.success(f"🏡 Estimated Sale Price: ₹{int(prediction):,}")
