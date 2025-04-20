import streamlit as st

st.title("Unit Converter 😉")
st.markdown("### Converts length, width and time")
st.write("Select a categaory!")

category = st.selectbox("Choose from here", ["Length", "Width", "Time"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "kilometers to miles":
            return value * 0.621371
        elif unit == "miles to kilometer":
            return value / 0.621371
        
    elif category == "Weight":
        if unit == "kilograms to pounds":
            return value * 2.20462
        elif unit == "pounds to kilograms":
            return value / 2.20462
    
    elif category == "Time":
        if unit == "second to minutes":
            return value / 60
        elif unit == "minutes to seconds":
            return value * 60
        elif unit == "minutes to hours":
            return value / 60
        elif unit == "hours to minutes":
            return value * 60 
        elif unit == "hours to days":
            return value / 24
        elif unit == "days to hours":
            return value * 24 
        
if category == "Length":
    unit = st.selectbox("Select conversion", ["kilometers to miles", "miles to kilometer"])

elif category == "Weight":
    unit = st.selectbox("Select conversion", ["kilograms to pounds", "pounds to kilograms"])

elif category == "Time":
    unit = st.selectbox(
        "Select conversion",
        ["seconds to minutes", "minutes to seconds", "minutes to hours", "hours to minutes", "hours to days", "days to hours"])

value = st.number_input("enter ur value to convert")

if st.button("convert"):
    result = convert_units(category, value, unit)
    st.success(f"the result is {result:.2f}")