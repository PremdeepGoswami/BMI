import streamlit as st

st.title("User BMI Demo")

height = st.number_input("Enter your Height")
Weight = st.number_input("Enter your Weight")

if st.button("Click Me"):
    st.success("Button Clicked!")

if height > 0:
    bmi = Weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    st.write("Height:", height)
    st.write("Weight:", Weight)
    st.write("BMI:", round(bmi, 2))
    st.write("Category:", category)
else:
    st.write("Please enter a valid height greater than 0.")
