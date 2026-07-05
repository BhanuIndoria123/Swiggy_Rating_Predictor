import streamlit as st
import pandas as pd
import joblib

# -------------------------
# LOAD MODEL + DATA
# -------------------------
model = joblib.load("swiggy_rating_model.joblib")
city_list = joblib.load("city_list.joblib")
area_list = joblib.load("area_list.joblib")
food_list = joblib.load("food_list.joblib")

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(page_title="Swiggy Rating Predictor", page_icon="🍽️", layout="centered")

# -------------------------
# BACKGROUND + STYLE
# -------------------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f5f7fa;
    }
    .main-title {
        font-size:40px;
        font-weight:bold;
        color:#ff4b4b;
        text-align:center;
    }
    .sub-text {
        text-align:center;
        font-size:16px;
        color:gray;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main-title">🍽️ Swiggy Rating Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Predict restaurant rating using Machine Learning</div>', unsafe_allow_html=True)

st.divider()

# -------------------------
# SIDEBAR INPUTS (Professional Look)
# -------------------------
st.sidebar.header("📌 Enter Details")

city = st.sidebar.selectbox("City", city_list)
area = st.sidebar.selectbox("Area", area_list)
food_type = st.sidebar.selectbox("Food Type", food_list)

price = st.sidebar.number_input("Price", 50, 5000, 300)
total_ratings = st.sidebar.number_input("Total Ratings", 0, 50000, 100)
delivery_time = st.sidebar.number_input("Delivery Time (min)", 5, 120, 30)

# -------------------------
# PREDICTION BUTTON
# -------------------------
if st.button("🚀 Predict Rating"):

    # Input DataFrame
    input_df = pd.DataFrame([{
        "City": city,
        "Area": area,
        "Food type": food_type,
        "Price": price,
        "Total ratings": total_ratings,
        "Delivery time": delivery_time
    }])

    # Prediction
    prediction = model.predict(input_df)[0]

    # -------------------------
    # OUTPUT UI
    # -------------------------
    st.success(f"⭐ Predicted Rating: {prediction:.2f}")

    # Confidence (simple interpretation)
    if prediction >= 4:
        st.info("🔥 High rated restaurant")
    elif prediction >= 3:
        st.warning("⚡ Average restaurant")
    else:
        st.error("❌ Low rated restaurant")
