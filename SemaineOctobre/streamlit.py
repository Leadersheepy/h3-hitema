import streamlit as st
import streamlit as st
import numpy as np
import pandas as pad
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Jeu Vidéo et Film", page_icon=":tada:", layout="wide")

st.subheader("Python et l'analyse de données :computer:")
st.title("Du jeu vidéo au film : Est-ce qu'un film adapté d'un jeu vidéo marchera forcément ?")
st.write("Le monde du jeu vidéo était très connu à l'époque pour ses adaptations de films très peu recommandable.")
st.write("Nous pouvons par exemple prendre la fameuse boîte française 'Infogrames' qui fut fortement moquée par des vidéastes dédiés au jeux vidéos pour ses jeux provenant de film de très mauvaises qualités.")
st.write("Toutefois, l'inverse existait aussi ! Les jeux vidéos étant une source abondante d'idée, certains producteurs ont décidés de les développer en film.")
st.write("Mais est-ce qu'un jeu vidéo qui a très bien fonctionner va aussi fonctionner dans le monde du cinéma ? Ceci est notre problèmatique pour cette analyse de donnée.")


video_game_film = pad.read_csv('video_game_films.csv')