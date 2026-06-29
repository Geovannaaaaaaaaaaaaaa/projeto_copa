import streamlit as st from google.oauth2 
import service_account from google.cloud 
import bigquery 

st.header("Indicadores") 

col1, col2, col3 = st.columns(3) 

with col1: st.metric(label="Média de gols", value="00") 
with col2: st.metric(label="Porc. de jogos sem derrotas", value="00") 
with col3: st.metric(label="Partidas disputadas", value="00")

