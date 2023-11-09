import streamlit as st
import pandas as pd

df1 = pd.read_csv("2023-03-08 Precios Casas RM.csv")
df2= pd.read_csv("2023-07-18 Propiedades Web Scrape.csv")

st.write("Una App")

st.write(df1)
st.dataframe(df2)
