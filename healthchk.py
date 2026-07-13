import streamlit as st

st.title("HealthMate by Premdeep")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age")

# Height Input
feet = st.number_input("Enter Height (Feet)", min_value=0, max_value=8, value=1)
inches = st.number_input("Enter Height (Inches)", min_value=0, max_value=11, value=5)

# Weight Input
weight = st.number_input("Enter Weight (kg)", min_value=1.0, value=60.0)

if st.button("Calculate BMI"):

    # Convert feet & inches to meters
    total_inches = (feet * 12) + inches
    height = total_inches * 0.0254

    if height > 0:

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal Weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        # Ideal weight range
        ideal_min = 18.5 * (height ** 2)
        ideal_max = 24.9 * (height ** 2)

        st.subheader("Result")

        st.write("Name:", name)
        st.write("Age:", age)
        st.write(f"**Height:** {feet} ft {inches} in")
        st.write(f"**Weight:** {weight:.1f} kg")
        st.write(f"**BMI:** {bmi:.2f}")
        st.write(f"**Category:** {category}")

        st.subheader("🎯 Ideal Weight Range")
        st.success(f"{ideal_min:.1f} kg to {ideal_max:.1f} kg")

        if weight < ideal_min:
            st.warning(f"You are {(ideal_min - weight):.1f} kg below the ideal weight.")
        elif weight > ideal_max:
            st.warning(f"You are {(weight - ideal_max):.1f} kg above the ideal weight.")
        else:
            st.success("🎉 Your weight is within the ideal range!")

    else:
        st.error("Please enter a valid height.")
