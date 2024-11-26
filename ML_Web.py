import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import os

# Load the dataset
@st.cache_data
def load_data():
    # Check if the pickle file exists
    if os.path.exists('car_data.pkl'):
        # Load the data from the pickle file
        with open('car_data.pkl', 'rb') as file:
            data = pickle.load(file)
    else:
        # If not, load from CSV and save to pickle
        data = pd.read_csv('CarPrice_Assignment.csv')
        with open('car_data.pkl', 'wb') as file:
            pickle.dump(data, file)
    return data

# Simple prediction function based on user input
def predict_price(highwaympg, curbweight, horsepower):
    # Use a simple linear regression formula (example coefficients)
    # These coefficients are placeholders and should be replaced with actual trained values
    base_price = 5000
    price = (highwaympg * 200) + (curbweight * 0.5) + (horsepower * 100) + base_price
    return price

# Load data
data = load_data()

# Streamlit app title
st.title("Prediksi Harga Mobil")

# Display the dataset
st.header("Dataset")
st.write(data)

# Create graphs
st.header("Graphs")

# Graph for Highway MPG
st.subheader("Highway MPG Distribution")
plt.figure(figsize=(10, 5))
sns.histplot(data['highwaympg'], bins=20, kde=True)
plt.title('Distribution of Highway MPG')
plt.xlabel('Highway MPG')
plt.ylabel('Frequency')
st.pyplot(plt)

# Graph for Curb Weight
st.subheader("Curb Weight Distribution")
plt.figure(figsize=(10, 5))
sns.histplot(data['curbweight'], bins=20, kde=True)
plt.title('Distribution of Curb Weight')
plt.xlabel('Curb Weight (lbs)')
plt.ylabel('Frequency')
st.pyplot(plt)

# Graph for Horsepower
st.subheader("Horsepower Distribution")
plt.figure(figsize=(10, 5))
sns.histplot(data['horsepower'], bins=20, kde=True)
plt.title('Distribution of Horsepower')
plt.xlabel('Horsepower')
plt.ylabel('Frequency')
st.pyplot(plt)

# Input fields for user
st.header("Input nilai dari detail berikut:")

# Input fields for user to enter values
highwaympg = st.number_input("Masukkan nilai Highway MPG:", min_value=0, max_value=50, value=0)
curbweight = st.number_input("Masukkan nilai Curb Weight (lbs):", min_value=0, max_value=5000, value=0)
horsepower = st.number_input("Masukkan nilai Horsepower:", min_value=0, max_value=300, value=0)

# Display the input values and make predictions
if st.button("Submit"):
    predicted_price = predict_price(highwaympg, curbweight, horsepower)
    st.success(f"Prediksi Harga Mobil: ${predicted_price:,.2f}")