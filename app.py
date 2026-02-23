import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("product_return_model.pkl")

st.title("🛒 Product Return Risk Prediction")

st.write("Enter product and customer details to predict return risk.")

# ---- Input Fields ----

age = st.number_input("Age", min_value=18, max_value=80, value=30)

gender = st.selectbox("Gender", ["Male", "Female"])

state = st.selectbox("State", ["State1", "State2", "State3"])  # replace with actual states

category = st.selectbox("Category", ["Electronics", "Clothing", "Home"])  # replace

brand = st.selectbox("Brand", ["BrandA", "BrandB", "BrandC"])  # replace

quantity = st.number_input("Quantity", min_value=1, value=1)

price = st.number_input("Price", min_value=0.0, value=100.0)

discount = st.number_input("Discount (%)", min_value=0.0, max_value=100.0, value=10.0)

product_rating = st.slider("Product Rating", 1.0, 5.0, 3.5)

# ---- Predict Button ----

if st.button("Predict Return Risk"):

    input_data = pd.DataFrame({
        "age": [age],
        "gender": [gender],
        "state": [state],
        "category": [category],
        "brand": [brand],
        "quantity": [quantity],
        "price": [price],
        "discount": [discount],
        "product_rating": [product_rating]
    })

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ High Return Risk")
    else:
        st.success("✅ Low Return Risk")
        