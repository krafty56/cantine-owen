
import streamlit as st
import pandas as pd
import math
from datetime import date

# Chargement des coefficients
k1_df = pd.read_csv("data/k1_races.csv")
k2_df = pd.read_csv("data/k2_activite.csv")
k3_df = pd.read_csv("data/k3_statut.csv")

# Interface Streamlit
st.set_page_config(page_title="La Cantine d'Owen : le lab", layout="centered")
st.title("🐾 La Cantine d’Owen : le lab")
st.markdown("### Création du profil animal")

# Formulaire
name = st.text_input("Nom du chien")
dob = st.date_input("Date de naissance", value=date(2020, 1, 1))
weight = st.number_input("Poids (kg)", min_value=0.5, step=0.1)

race = st.selectbox("Race", k1_df['race'].tolist())
activity = st.selectbox("Niveau d’activité", k2_df['niveau'].tolist())
status = st.selectbox("Statut physiologique", k3_df['statut'].tolist())

if name and weight > 0:
    k1 = k1_df.loc[k1_df['race'] == race, 'k1'].values[0]
    k2 = k2_df.loc[k2_df['niveau'] == activity, 'k2'].values[0]
    k3 = k3_df.loc[k3_df['statut'] == status, 'k3'].values[0]

    # Calcul BEE
    bee_base = 130 * math.pow(weight, 0.75)
    bee_final = bee_base * k1 * k2 * k3

    st.markdown("### 🧮 Besoin Énergétique Estimé")
    st.success(f"{bee_final:.0f} kcal / jour")
else:
    st.info("Veuillez remplir le nom et le poids pour obtenir le besoin énergétique.")
