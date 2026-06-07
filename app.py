import streamlit as st
import pandas as pd
import joblib

# Load model and columns
model = joblib.load("vehicle_price_model.pkl")
model_columns = joblib.load("model_columns.pkl")

st.title("🚗 Vehicle Price Prediction")

# User Inputs
year = st.selectbox("Year", [2023, 2024, 2025])
mileage = st.number_input("Mileage", min_value=0.0, value=10000.0)

make = st.selectbox(
    "Make",
    ["Jeep", "BMW", "Audi", "Ford", "Toyota"]
)

fuel = st.selectbox(
    "Fuel Type",
    ["Gasoline", "Diesel", "Hybrid", "Electric"]
)

transmission = st.selectbox(
    "Transmission",
    ["Automatic", "Manual"]
)

body = st.selectbox(
    "Body Type",
    ["SUV", "Sedan", "Pickup Truck", "Coupe"]
)

drivetrain = st.selectbox(
    "Drivetrain",
    ["Front-wheel Drive",
     "Rear-wheel Drive",
     "Four-wheel Drive",
     "All-wheel Drive"]
)

if st.button("Predict Price"):

    # Create empty row
    input_df = pd.DataFrame(
        0,
        index=[0],
        columns=model_columns
    )

    # Numerical features
    input_df["year"] = year
    input_df["mileage"] = mileage

    # One-hot encoded features
    make_col = f"make_{make}"
    fuel_col = f"fuel_{fuel}"
    transmission_col = f"transmission_{transmission}"
    body_col = f"body_{body}"
    drivetrain_col = f"drivetrain_{drivetrain}"

    for col in [
        make_col,
        fuel_col,
        transmission_col,
        body_col,
        drivetrain_col
    ]:
        if col in input_df.columns:
            input_df[col] = 1

    prediction = model.predict(input_df)[0]

    st.success(
        f"Estimated Vehicle Price: ${prediction:,.2f}"
    )