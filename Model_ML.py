import pickle
import streamlit as st
import pandas as pd
import os
import numpy as np
import altair as alt

# https://www.kaggle.com/datasets/goyalshalini93/car-data
df_mobil = pd.read_csv("carPrice_Assignment.csv")
df_mobil

filename = 'model_prediksi_harga_mobil.sav'
pickle.dump(model_regresi, open (filename), 'wb')

