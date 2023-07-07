

#import streamlit as streamlit
#conda activate pyenv310
#tuch dashboard_tuto.py
#!pip install streamlit


import streamlit as st


st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)

from fastapi import FastAPI
import uvicorn
import time
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


def load_data ()  :
    ## Chargement de la base de donné###
    base1 = pd.read_csv("achats.csv", parse_dates=['timestamp'])
    base2 = pd.read_csv("clics.csv", parse_dates=['timestamp'])
    base3 = pd.read_csv("impressions.csv", parse_dates=['timestamp'])
    base_n = pd.merge(base3, base2, on='cookie_id', how='left')
    base = pd.merge(base_n, base1, on='cookie_id', how='left')
    return base

df = load_data()


#Titre du dashboard
st.title("TP : Creation d'un dashborad avec Streamlit")

#Les filtres en début
#age_filter = st.selectbox("Selection des âges", pd.unique(df["age"]))
identifian_filter = st.selectbox("Selectionner une campagne", pd.unique(df["campaign_id"]))

# Application du filtre à la base de données
#df = df[df["age"] == age_filter]
#df = df[df["campaign_id"] == identifian_filter]
df = df[df["campaign_id"] == identifian_filter]

# creation de  colonnes pour les graphiques
fig_col11, fig_col12, fig_col21 = st.columns([0.20, 0.55, 0.25])

with fig_col11:
    #st.markdown("### premier graphique")
    #fig = px.density_heatmap(
        #data_frame=df, y="age", x="product_id"
    #)
    chif_affaire = df['price'].sum()
    st.write(st.write(f"<span style='color:red; font-size:40px;'>Chiffre d'affaires : {chif_affaire} € </span>", unsafe_allow_html=True))

with fig_col12:
    st.markdown("### Nombre de clique par heure")
    fig2 = px.histogram(data_frame=df, x='timestamp_x')
    st.write(fig2)

#fig_col21, fig_col22 = st.columns(2)
with fig_col21:
    st.markdown("### Age des clients en fontion des produits")
    fig3 = px.box(df, x='product_id', y="age", points="outliers")
    st.write(fig3)

#with fig_col22:
    #st.markdown("### Evolution des prix de vente a chaque achat")
    #fig4 = px.line(df, x='timestamp_x', y="price")
    #st.write(fig4)



st.write(df)