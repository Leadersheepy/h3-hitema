#!/usr/bin/env python
# coding: utf-8

# # Python et l'analyse de données
# ## Du jeu vidéo au film : Est-ce qu'un film adapté d'un jeu vidéo marchera forcément ? 


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


video_game_film = pad.read_csv(open('h3-hitema/SemaineOctobre/video_game_films.csv'))
video_game = pad.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')

st.write("Pour notre analyse de données, nous allons utiliser deux csv, l'un regroupe les jeux vidéos adaptés en film, tandis que l'autre la vente des jeux vidéos jusqu'en 2016.")


st.dataframe(video_game_film)  # Same as st.write(df)

video_game_film.head()


video_game.head()
st.dataframe(video_game)  # Same as st.write(df)


st.write("Observons nos deux tableaux grâce au .head(), nous pourrions utiliser tout simplement video_game, mais il affichera beaucoup trop de données pour le moment.")

st.title("Que remarquons nous")

st.write("Nous nous retrouvons avec deux cvs, mais il nous faut maintenant les regrouper. Cependant, si l'on regarde bien les deux tableaux certains élèments ne coincident pas, ce qui engendera des soucis pour plus tard. Nous devons donc modifier les csv sur deux colonnes :")
st.write("Name / Title et Worldwide box office")
st.write("Colonne Name/Title représente le soucis concernant les titres. ")
 
st.write("En effet on a deux problèmes :")
st.write("- Les titres des jeux vidéos d'une même franchise peut être différente")
st.write("- La colonne dans les deux csv n'ont pas le même nom")

st.write("Nous pouvions essayer de résoudre ce problème en le programmant sur python, mais au vue du temps imparti, le changement fu fait à la main.")
st.write("Une nouvelle colonne dans les deux fichiers nommée 'Surnom' furent créer. Si par exemple le film Lara Croft était affiché dans le csv des films, alors tout les Lara croft dans l'autre fichié étaient maintenant surnomée 'Lara Croft' dans la colonne Surnom.")
st.write("Avec cette technique il n'était plus nécéssaire de modifier le nom de l'autre colonne.")

st.title("Worldwide box office")

st.write("Worldwide box office et Global_Sales sont des valeurs que nous allons utiliser plus tard car les deux sont des valeurs à peu pret comparable (se trouvant tous les deux en million). Le petit soucis est que l'un affiche toutes la somme tandis que l'autre s'affiche en 0.00. Pour régler ce problème, il fallait juste changer le format de l'un des deux csv (celui avec le moins de valeurs fut choisi pour le changement).")

st.title("Importation 2")

video_game_film_m = pad.read_csv('video_game_films_modifie.csv')

video_game_m = pad.read_csv('Video_Games_Sales_modifie.csv')

st.write("video_game_film_m")


video_game_m.head()
st.dataframe(video_game_m)  # Same as st.write(df)

st.write("On se retrouve donc avec deux nouveaux jeux de données que nous allons maintenant fusionner !")

melange = pad.merge(video_game_m, video_game_film_m, on='Surnom')
st.dataframe(melange) 

st.write("dropna va permettre de retirer les valeurs NaN tandis que reset_index va remettre l index à zero")
melange_f = melange.dropna(subset=['Surnom'])

melange_f = melange_f.reset_index(drop=True)

melange_f
st.dataframe(melange_f) 

st.write("Nous obtenons donc un jeu de données sur l'univers des jeux vidéos ayant eu une adaptation au cinéma avec 1172 jeux repartient dans moins de 42 franchises avec 24 caractéristiques.")
st.write(" On peut déjà regarder sur un historigramme")

fig = plt.figure(figsize=(15,8))

sns.histplot(
    data=melange_f,
    x="Genre",
    hue ="Genre",
    shrink=0.8
)
plt.title("Les genre les plus crées dans les jeux vidéos")
st.pyplot(fig)

#sns.lineplot(data=melange_f, y='Global_Sales',x="Year_of_Release")
st.info('Appuyez sur le bouton pour retirer les valeurs incohérentes', icon="ℹ️")

if st.button('Adieu !'):
    fig2 = plt.figure(figsize=(12,8))

    sns.lineplot(
        data=melange_f[melange_f['Year_of_Release'] > 1986],
        x="Year_of_Release",
        y ="Global_Sales"
    )
    plt.title("Vente des jeux vidéos par année")
    st.pyplot(fig2)
else:
    fig2 = plt.figure(figsize=(12,8))

    sns.lineplot(
        data=melange_f,
        x="Year_of_Release",
        y ="Global_Sales"
    )
    plt.title("Vente des jeux vidéos par année")
    st.pyplot(fig2) 

fig3 = plt.figure(figsize=(15,8))
fig33 = plt.xticks(rotation=90)


sns.lineplot(
    data=melange_f.sample(n=50),
    x="Surnom",
    y="Worldwide_box_office_tri",
)
plt.title("Graphique échantillon box office des films")
st.pyplot(fig3,fig33)


st.info('Appuyez sur le bouton pour retirer les valeurs incohérentes', icon="ℹ️")

if st.button('Pouf !'):
    fig4 = plt.figure(figsize=(15,8))
    fig44 = plt.xticks(rotation=90)

    sns.barplot(
        data=melange_f.query("5 < Global_Sales"),
        x="Surnom",
        y="Global_Sales",
    )
    plt.title("Gloal sales par rapport aux jeux vidéos")
    st.pyplot(fig4,fig44)

else:
    fig4 = plt.figure(figsize=(15,8))
    fig44 = plt.xticks(rotation=90)

    sns.barplot(
        data=melange_f,
        x="Surnom",
        y="Global_Sales",
    )
    plt.title("Gloal sales par rapport aux jeux vidéos")
    st.pyplot(fig4,fig44)



fig5 = plt.figure(figsize=(15,8))
fig55 = plt.xticks(rotation=90)

sns.barplot(
    data=melange_f.query("200 < Worldwide_box_office_tri"),
        y='Worldwide_box_office_tri',
        x='Genre',

)
plt.title("Graphique des genres les plus vendu au cinéma")
st.pyplot(fig5,fig55)


fig6 = plt.figure(figsize=(15,8))
fig66 = plt.xticks(rotation=90)

sns.barplot(
    data=melange_f.query("200 < Worldwide_box_office_tri"),
        y='Worldwide_box_office_tri',
        x='Surnom',

)
plt.title("Graphique représentant les meilleurs ventes de films après 200 millions")
st.pyplot(fig6,fig66)



# #### TEST AVEC DES JEUX VIDEOS / FILMS INDIVIDUELLEMENT 
st.title("TEST AVEC DES JEUX VIDEOX / FILMS INDIVIDUELLEMENTS")

# ##### Resident Evil

st.title("RESIDENT EVIL :zombie:")

RE = melange_f[melange_f['Surnom']=="Resident Evil"]
RE = RE.reset_index(drop=True)
RE


fig7 = plt.figure(figsize=(15,8))

sns.boxplot(
    data=RE.query("Global_Sales<3.5"),
        y='Title',
        x='Global_Sales',

)
st.pyplot(fig7)

fig8 = plt.figure(figsize=(15,8))
sns.boxplot(
    data=RE,
        y='Name',
        x='Global_Sales',

)
st.pyplot(fig8)


fig9 = plt.figure(figsize=(15,8))
sns.barplot(
    data=RE,
        y='Title',
        x='Worldwide_box_office_tri',

)
st.pyplot(fig9)

# ##### Lara Croft


st.title("LARA CROFT :woman:")

LC = melange_f[melange_f['Surnom']=="Lara Croft"]
LC = LC.reset_index(drop=True)
LC


fig10 = plt.figure(figsize=(15,8))
sns.barplot(
    data=LC,
        y='Name',
        x='Global_Sales',

)
st.pyplot(fig10)


fig11 = plt.figure(figsize=(15,8))
sns.barplot(
    data=LC,
        y='Title',
        x='Worldwide_box_office_tri',

)
st.pyplot(fig11)

fig12 = plt.figure(figsize=(15,8))
sns.barplot(
    data=LC,
        y='Name',
        x='Global_Sales',

)
st.pyplot(fig12)


# #### Alone in the Dark


st.title("Alone in the dark :ghost:")
AID = melange_f[melange_f['Surnom']=="Alone in the Dark"]
AID = AID.reset_index(drop=True)
AID



fig11 = plt.figure(figsize=(15,8))
sns.barplot(
    data=AID,
        y='Name',
        x='Global_Sales',

)
st.pyplot(fig11)



st.write("Worldwide box office pour Alone in the Dark : ", AID['Worldwide_box_office_tri'][0])

#print("Worldwide box office pour Alone in the Dark : ", AID['Worldwide_box_office_tri'][0])


# #### Conclusion
st.title("Conclusion")
st.write("Nous pouvons conclure que même si le film dont vient le jeux vidéo peut influencer la réussite du film, cela n'est pas toujours le cas. Il faut aussi choisir des meilleurs données car les csv n'étaient pas si compatible que ça.")
