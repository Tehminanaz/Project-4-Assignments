import streamlit as st 
import pandas as pd 

st.title("BMI Calculator")

# Get user input for height and weight
height = st.slider("Enter your height in (cm) ", 100, 250, 175)
weight = st.slider("Enter your weight in (kg) ", 100, 250, 175)

# Calculate BMI
bmi = weight / ((height/100)**2)

# Display the calculated BMI
st.write(f"Your BMI is {bmi:.2f}")

# Display BMI categories
st.write("### BMI Categories ###")
st.write("- Underweight: BMI is less than 18.5")
st.write("- Normal weight: BMI is between 18.5 and 24.9")
st.write("- Overweight: BMI is between 25 and 29.9")
st.write("- Obesity: BMI is 30 or greater")
