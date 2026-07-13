import streamlit as st
import math

st.title("EMI Calculator by Premdeep")

Principal_Loan_Amount = st.number_input("Enter your Loan Amount", min_value=0.0)

Annual_Interest_Rate = st.number_input("Enter your Loan Interest Rate (%)", min_value=0.0)

Tenure_type = st.selectbox("Select Tenure Unit", ["Months", "Years"])

Tenure = st.number_input("Enter Loan Tenure", min_value=1)

Monthly_income = st.number_input("Enter your Monthly Salary", min_value=0.0)

# Button
if st.button("Calculate EMI"):

    # Convert tenure to months
    if Tenure_type == "Years":
        months = Tenure * 12
    else:
        months = Tenure

    st.write("**Loan Tenure (in Months):**", int(months))

    # Monthly interest rate
    monthly_rate = (Annual_Interest_Rate / 12) / 100

    # EMI Calculation
    if monthly_rate > 0:
        emi = (
            Principal_Loan_Amount
            * monthly_rate
            * (1 + monthly_rate) ** months
        ) / (((1 + monthly_rate) ** months) - 1)
    else:
        emi = Principal_Loan_Amount / months

    st.subheader("📋 EMI Result")
    st.success(f"Your Monthly EMI is ₹{emi:.2f}")

    # Optional: EMI as % of salary
    if Monthly_income > 0:
        emi_percent = (emi / Monthly_income) * 100
        st.write(f"EMI is **{emi_percent:.1f}%** of your monthly salary.")

        if emi_percent <= 40:
            st.success("✅ Your EMI is within a comfortable range.")
        else:
            st.warning("⚠️ Your EMI is more than 40% of your salary.")

