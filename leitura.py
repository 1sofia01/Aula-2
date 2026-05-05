import streamlit as st
import pandas as pd

df = pd.read_csv('deputados_2022.csv')
st.dataframe(df)

st.write("Colunas do arquivo:")
st.write(df.columns)

sigla = st.text_input('Digite a sigla do partido')
if sigla:
  st.dataframe(dt[df['partido']==sigla.upper()]
  
