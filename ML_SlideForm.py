import streamlit as st
import datetime

st.title('this is the app title')
st.markdown('this is the app markdown')
st.header('this is the app header')
st.subheader('this is the app subheader')
st.caption('this is the app caption')
st.code('X=2021')

agree = st.checkbox("Yes")

st.button("Click")

# Radio button for gender selection
gender = st.radio("Pick your gender:", ("Male", "Female"))

gender2 = st.selectbox("Choose a gender:", 
                       options=["Male","Female"],
                       index=0)  # Set index to 0 to show the first option (empty string)

# Select box for choosing a planet with a placeholder
planet = st.selectbox(
    "Choose a planet:",   
    options=[
        "Choose an option", 
        "Mercury", 
        "Venus", 
        "Earth", 
        "Mars", 
        "Jupiter", 
        "Saturn", 
        "Uranus", 
        "Neptune"],
    index=0)  # Set index to 0 to show the first option (empty string)

rating = st.select_slider(
    "Choose a rating",
    options=[
        "Bad",
        "Good",
        "Excellent"],
        value="Good")

slider_value = st.slider("pick a number", min_value=0, max_value=50, value=9)

number = st.number_input("Pick a number",min_value=1, max_value=50)

text_input = st.text_input(
        "Email address")

d = st.date_input("Travelling date", datetime.date(2024, 11, 26))

t = st.time_input("School time", datetime.time(8, 00))

txt = st.text_area(
    "Description",
    "")

uploaded_files = st.file_uploader(
    "Choose a CSV file", accept_multiple_files=True
)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

color = st.color_picker("Pick A Color", "#663399")