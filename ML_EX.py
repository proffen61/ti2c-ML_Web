import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('Agg')

menu = st.sidebar.selectbox("Select Page", ["Home"])


st.image("https://dnycf48t040dh.cloudfront.net/Random-Module-Python.jpeg")

df = pd.read_csv("data.csv")
st.write(df)

plt.figure(figsize=(10, 5))
plt.bar(df['Category'], df['Value'], color='skyblue')
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Graph of Values by Category')


st.pyplot(plt)

if __name__ == "__main__":
    st.write("")