

import pandas as pd
import pickle as pk
import streamlit as st


# ----------------------------
# PAGE CONFIG (must be first Streamlit command)
# ----------------------------
st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="wide"
)


# ----------------------------
# LOAD EXTERNAL CSS
# ----------------------------
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Load trained model
model = pk.load(open("model.pkl", "rb"))


# Page title (styled via .hero class in style.css)
st.markdown("""
<div class="hero">
    <h1>🚗 Car Price Prediction</h1>
    <p>Enter the car details below to predict its selling price.</p>
</div>
""", unsafe_allow_html=True)


# Car Brand
name = st.selectbox(
    "Car Brand",
    ["Maruti", "Skoda", "Honda", "Ford",
     "Renault", "Hyundai", "Mahindra", "Toyota"]
)

# Year
year = st.number_input(
    "Year",
    min_value=2000,
    max_value=2025,
    value=2015
)

# Kilometers driven
km_driven = st.number_input(
    "Kilometers Driven",
    min_value=0,
    value=50000
)

# Fuel
fuel = st.selectbox(
    "Fuel Type",
    ["Diesel", "Petrol", "CNG", "LPG"]
)

# Seller type
seller_type = st.selectbox(
    "Seller Type",
    ["Individual", "Dealer", "Trustmark Dealer"]
)

# Transmission
transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)

# Owner
owner = st.selectbox(
    "Owner",
    ["First Owner",
     "Second Owner",
     "Third Owner",
     "Fourth & Above Owner"]
)

# Mileage
mileage = st.number_input(
    "Mileage (kmpl)",
    min_value=0.0,
    value=20.0
)

# Engine
engine = st.number_input(
    "Engine (CC)",
    min_value=0.0,
    value=1200.0
)

# Maximum Power
max_power = st.number_input(
    "Max Power (bhp)",
    min_value=0.0,
    value=80.0
)

# Seats
seats = st.number_input(
    "Number of Seats",
    min_value=2.0,
    max_value=10.0,
    value=5.0
)


# Convert categorical values to numbers
name_mapping = {
    "Maruti": 1,
    "Skoda": 2,
    "Honda": 3,
    "Ford": 4,
    "Renault": 5,
    "Hyundai": 6,
    "Mahindra": 7,
    "Toyota": 8
}

fuel_mapping = {
    "Diesel": 1,
    "Petrol": 2,
    "CNG": 3,
    "LPG": 4
}

seller_mapping = {
    "Individual": 1,
    "Dealer": 2,
    "Trustmark Dealer": 3
}

transmission_mapping = {
    "Manual": 1,
    "Automatic": 2
}

owner_mapping = {
    "First Owner": 1,
    "Second Owner": 2,
    "Third Owner": 3,
    "Fourth & Above Owner": 4
}


# Prediction button
if st.button("Predict Car Price"):

    input_data = pd.DataFrame(
        [[
            name_mapping[name],
            year,
            km_driven,
            fuel_mapping[fuel],
            seller_mapping[seller_type],
            transmission_mapping[transmission],
            owner_mapping[owner],
            mileage,
            engine,
            max_power,
            seats
        ]],
        columns=[
            "name",
            "year",
            "km_driven",
            "fuel",
            "seller_type",
            "transmission",
            "owner",
            "mileage",
            "engine",
            "max_power",
            "seats"
        ]
    )

    prediction = model.predict(input_data)

    st.markdown(f"""
    <div class="result-card">
        <p>Estimated Selling Price</p>
        <h2>₹ {prediction[0]:,.2f}</h2>
    </div>
    """, unsafe_allow_html=True)


# Footer (styled via .footer class in style.css)
st.markdown("""
<div class="footer">
    Built with ❤️ using Streamlit &nbsp;|&nbsp; Linear Regression Model
</div>
""", unsafe_allow_html=True)