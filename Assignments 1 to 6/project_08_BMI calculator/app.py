import streamlit as st 
import pandas as pd 

st.title("BMI Calculator")

height = st.slider("Enter your height in (cm) ",100,250,175)
weight = st.slider("Enter your weight in (kg) ",100,250,175)


bmi = weight / ((height/100)**2)

st.write(f"Your BMI is {bmi:.2f}")


st.write("### BMI Calculator ###")
st.write("- underweight: BMI is less then 18.5")
st.write("- Normal weight: BMI is 18.5 and 24.9")
st.write("- Over weight: BMI beteen 25 and 24.9")
st.write("- Obesty: BMI 30 or greater")