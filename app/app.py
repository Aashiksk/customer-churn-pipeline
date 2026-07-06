import streamlit as st
from pyspark.sql import SparkSession
from pyspark.ml import PipelineModel

spark = SparkSession.builder \
    .appName("Customer Churn Prediction") \
    .getOrCreate()

model = PipelineModel.load("saved_model/churn_rf_pipeline")

st.title("📊 Customer Churn Prediction")

st.write("Enter customer information below.")

gender = st.selectbox("Gender", ["Male", "Female"])

SeniorCitizen = st.selectbox(
    "Senior Citizen",
    [0, 1]
)

Partner = st.selectbox(
    "Partner",
    ["Yes", "No"]
)

Dependents = st.selectbox(
    "Dependents",
    ["Yes", "No"]
)

tenure = st.number_input(
    "Tenure (months)",
    min_value=0,
    max_value=100,
    value=12
)

PhoneService = st.selectbox(
    "Phone Service",
    ["Yes", "No"]
)

MultipleLines = st.selectbox(
    "Multiple Lines",
    ["Yes", "No", "No phone service"]
)

InternetService = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

OnlineSecurity = st.selectbox(
    "Online Security",
    ["Yes", "No", "No internet service"]
)

OnlineBackup = st.selectbox(
    "Online Backup",
    ["Yes", "No", "No internet service"]
)

DeviceProtection = st.selectbox(
    "Device Protection",
    ["Yes", "No", "No internet service"]
)

TechSupport = st.selectbox(
    "Tech Support",
    ["Yes", "No", "No internet service"]
)

StreamingTV = st.selectbox(
    "Streaming TV",
    ["Yes", "No", "No internet service"]
)

StreamingMovies = st.selectbox(
    "Streaming Movies",
    ["Yes", "No", "No internet service"]
)

Contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

PaperlessBilling = st.selectbox(
    "Paperless Billing",
    ["Yes", "No"]
)

PaymentMethod = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

MonthlyCharges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=70.0
)

TotalCharges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=1500.0
)

if st.button("Predict Churn"):
      new_customer = [(
        gender,
        SeniorCitizen,
        Partner,
        Dependents,
        tenure,
        PhoneService,
        MultipleLines,
        InternetService,
        OnlineSecurity,
        OnlineBackup,
        DeviceProtection,
        TechSupport,
        StreamingTV,
        StreamingMovies,
        Contract,
        PaperlessBilling,
        PaymentMethod,
        MonthlyCharges,
        TotalCharges,
        "No"   # Dummy value for Churn
    )]

      columns = [
        "gender",
        "SeniorCitizen",
        "Partner",
        "Dependents",
        "tenure",
        "PhoneService",
        "MultipleLines",
        "InternetService",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies",
        "Contract",
        "PaperlessBilling",
        "PaymentMethod",
        "MonthlyCharges",
        "TotalCharges",
        "Churn"
    ]

      new_df = spark.createDataFrame(new_customer, schema=columns)

      prediction = model.transform(new_df)
      
      result = prediction.select(
        "prediction",
        "probability"
    ).first()
      
      if result.prediction == 1:
        st.error("⚠️ Customer is likely to Churn")
      else:
        st.success("✅ Customer is likely to Stay")

      churn_probability = result.probability[1] * 100

      st.write(f"### Churn Probability: {churn_probability:.2f}%")