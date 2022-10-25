#!/usr/bin/env python
# coding: utf-8

# # Python et l'analyse de données
# ## Du jeu vidéo au film : Est-ce qu'un film adapté d'un jeu vidéo marchera forcément ? 

# Le monde du jeu vidéo était très connu à l'époque pour ses adaptations de films très peu recommandable. Nous pouvons par exemple prendre la fameuse boîte française 'Infogrames' qui fut fortement moquée par des vidéastes dédiés au jeux vidéos pour ses jeux provenant de film de très mauvaises qualités. 
# 
# Toutefois, l'inverse existait aussi ! Les jeux vidéos étant une source abondante d'idée, certains producteurs ont décidés de les développer en film. 
# 
# Mais est-ce qu'un jeu vidéo qui a très bien fonctionner va aussi fonctionner dans le monde du cinéma ? 
# 
# Ceci est notre problèmatique pour cette analyse de donnée.

# #### Importation

# Avant de commencer quoi que ce soit, nous allons importer toutes les librairies que nous aurons besoin et les documents sur lesquels nous allosn travailler.

# In[4]:

import streamlit as st
import numpy as np
import pandas as pad
import seaborn as sns
import matplotlib.pyplot as plt


# In[6]:
st.set_page_config(page_title="Jeu Vidéo et Film", page_icon=":tada:", layout="wide")

st.subheader("Coucou, je suis Marinouh :sheep:")
st.title("Analyse des jeux vidéos adaptés en film")
st.write("Le monde du jeu vidéo était très connu à l'époque pour ses adaptations de films très peu recommandable.")
st.write("Nous pouvons par exemple prendre la fameuse boîte française 'Infogrames' qui fut fortement moquée par des vidéastes dédiés au jeux vidéos pour ses jeux provenant de film de très mauvaises qualités.")
st.write("Toutefois, l'inverse existait aussi ! Les jeux vidéos étant une source abondante d'idée, certains producteurs ont décidés de les développer en film.")
st.write("Mais est-ce qu'un jeu vidéo qui a très bien fonctionner va aussi fonctionner dans le monde du cinéma ? Ceci est notre problèmatique pour cette analyse de donnée.")
# In[5]:


video_game_film = pad.read_csv('video_game_films.csv');
video_game = pad.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv');

st.write("Pour notre analyse de données, nous allons utiliser deux csv, l'un regroupe les jeux vidéos adaptés en film, tandis que l'autre la vente des jeux vidéos jusqu'en 2016.")

# Pour notre analyse de données, nous allons utiliser deux csv, l'un regroupe les jeux vidéos adaptés en film, tandis que l'autre la vente des jeux vidéos jusqu'en 2016.

# In[6]:

st.dataframe(video_game_film)  # Same as st.write(df)

video_game_film.head()


# In[7]:


video_game.head()
st.dataframe(video_game)  # Same as st.write(df)


st.write("Observons nos deux tableaux grâce au .head(), nous pourrions utiliser tout simplement video_game, mais il affichera beaucoup trop de données pour le moment.")

# Observons nos deux tableaux grâce au .head(), nous pourrions utiliser tout simplement video_game, mais il affichera beaucoup trop de données pour le moment.

# #### Que remarquons nous ?
st.title("Que remarquons nous")

st.write("Nous nous retrouvons avec deux cvs, mais il nous faut maintenant les regrouper. Cependant, si l'on regarde bien les deux tableaux certains élèments ne coincident pas, ce qui engendera des soucis pour plus tard. Nous devons donc modifier les csv sur deux colonnes :")

# Nous nous retrouvons avec deux cvs, mais il nous faut maintenant les regrouper. Cependant, si l'on regarde bien les deux tableaux certains élèments ne coincident pas, ce qui engendera des soucis pour plus tard. Nous devons donc modifier les csv sur deux colonnes :
# 
st.write("Name / Title et Worldwide box office")

# Name / Title et Worldwide box office.

# **Colonne Name/Title** représente le soucis concernant les titres. 
#
st.write("Colonne Name/Title représente le soucis concernant les titres. ")
 
# En effet on a deux problèmes : 
# - Les titres des jeux vidéos d'une même franchise peut être différente
# - La colonne dans les deux csv n'ont pas le même nom

st.write("En effet on a deux problèmes :")
st.write("Les titres des jeux vidéos d'une même franchise peut être différente")
st.write("La colonne dans les deux csv n'ont pas le même nom")

# Nous pouvions essayer de résoudre ce problème en le programmant sur python, mais au vue du temps imparti, le changement fu fait à la main.
# 
# - Une nouvelle colonne dans les deux fichiers nommée "Surnom" furent créer. Si par exemple le film Lara Croft était affiché dans le csv des films, alors tout les Lara croft dans l'autre fichié étaient maintenant surnomée "Lara Croft" dans la colonne Surnom.
# 
# Avec cette technique il n'était plus nécéssaire de modifier le nom de l'autre colonne.
st.write("Nous pouvions essayer de résoudre ce problème en le programmant sur python, mais au vue du temps imparti, le changement fu fait à la main.")
st.write("Une nouvelle colonne dans les deux fichiers nommée 'Surnom' furent créer. Si par exemple le film Lara Croft était affiché dans le csv des films, alors tout les Lara croft dans l'autre fichié étaient maintenant surnomée 'Lara Croft' dans la colonne Surnom.")
st.write("Avec cette technique il n'était plus nécéssaire de modifier le nom de l'autre colonne.")

# ##### Worldwide box office
st.title("Worldwide box office")

# Worldwide box office et Global_Sales sont des valeurs que nous allons utiliser plus tard car les deux sont des valeurs à peu pret comparable (se trouvant tous les deux en million). Le petit soucis est que l'un affiche toutes la somme tandis que l'autre s'affiche en 0.00. Pour régler ce problème, il fallait juste changer le format de l'un des deux csv (celui avec le moins de valeurs fut choisi pour le changement).

st.write("Worldwide box office et Global_Sales sont des valeurs que nous allons utiliser plus tard car les deux sont des valeurs à peu pret comparable (se trouvant tous les deux en million). Le petit soucis est que l'un affiche toutes la somme tandis que l'autre s'affiche en 0.00. Pour régler ce problème, il fallait juste changer le format de l'un des deux csv (celui avec le moins de valeurs fut choisi pour le changement).")

# In[8]:


#rslt_df = final[final['Title'] == 'Super Mario Bros.']
#rslt_df.head()


# #### Importation 2
st.title("Importation 2")

# In[9]:


video_game_film_m = pad.read_csv('video_game_films_modifie.csv');
video_game_m = pad.read_csv('Video_Games_Sales_modifie.csv');


# In[10]:


#video_game_film_m
st.write("video_game_film_m")


# In[11]:


video_game_m.head()
st.dataframe(video_game_m)  # Same as st.write(df)

st.write("On se retrouve donc avec deux nouveaux jeux de données que nous allons maintenant fusionner !")

# On se retrouve donc avec deux nouveaux jeux de données que nous allons maintenant fusionner !

# In[12]:

#final = pd.concat([video_game_m,video_game_film_m])
melange = pad.merge(video_game_m, video_game_film_m, on='Surnom')
st.dataframe(melange) 

#dropna va permettre de retirer les valeurs NaN tandis que reset_index va remettre l index à zero
melange_f = melange.dropna(subset=['Surnom'])

melange_f = melange_f.reset_index(drop=True)

melange_f
st.dataframe(melange_f) 

st.write("Nous obtenons donc un jeu de données sur l'univers des jeux vidéos ayant eu une adaptation au cinéma avec 1172 jeux repartient dans moins de 42 franchises avec 24 caractéristiques.")
st.write(" On peut déjà regarder sur un historigramme")


# Nous obtenons donc un jeu de données sur l'univers des jeux vidéos ayant eu une adaptation au cinéma avec 1172 jeux repartient dans moins de 42 franchises avec 24 caractéristiques.

# On peut déjà regarder sur un historigramme
# 
# #### Les genres les plus crée dans les jeux vidéos

# In[13]:


#plt.figure(figsize= (15,8))
#sns.histplot(x='Genre', data = melange_f, hue="Genre",shrink=0.8)

#penguins = sns.load_dataset("melange_f")
fig = plt.figure(figsize=(15,8))

sns.histplot(
    data=melange_f,
    x="Genre",
    hue ="Genre",
    shrink=0.8
)
plt.title("Les genre les plus crées dans les jeux vidéos")
st.pyplot(fig)
# ### Graphique vente jeux vidéos par année

# In[14]:




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

    

# In[15]:


#melange_f[melange_f['Global_Sales'] > 20]


# In[16]:


#melange_f[melange_f['Global_Sales'] > 5].head()


# In[17]:


#sns.relplot(
#    x="Year_of_Release", y="Global_Sales",
#    data = melange_f.query("5 < Global_Sales < 20"),
#    height=8,
#);


# In[18]:


#sns.relplot(
#    y='Global_Sales',x="Year_of_Release",
#    data = melange_f.query("Global_Sales<10"),
#    height=8,
#);


# ### Graphique échantillon box office des films

# In[35]:
fig3 = plt.figure(figsize=(15,8))
fig33 = plt.xticks(rotation=90)


sns.lineplot(
    data=melange_f.sample(n=50),
    x="Surnom",
    y="Worldwide_box_office_tri",
)
plt.title("Graphique échantillon box office des films")
st.pyplot(fig3,fig33)

# sns.lineplot(
#   x="Surnom", y="Worldwide_box_office_tri", 
#   data=melange_f.sample(n=50))
#plt.xticks(rotation=90)


# #### Global sales par rapport au jeux vidéos

# In[20]:

st.info('Appuyez sur le bouton pour retirer les valeurs incohérentes', icon="ℹ️")

if st.button('Pouf !'):
    fig4 = plt.figure(figsize=(15,8))
    fig44 = plt.xticks(rotation=90)

    sns.barplot(
        data=melange_f.query("5 < Global_Sales"),
        x="Surnom",
        y="Global_Sales",
    )
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






#plt.figure(figsize= (15,8))
#sns.barplot(
#    y='Global_Sales',x='Surnom',
#     data = melange_f)
#plt.xticks(rotation=90)
 

# #### Graphique supérieur global sales et les jeux

# In[21]:




#plt.figure(figsize= (15,8))
#sns.barplot(
#    y='Global_Sales',x='Surnom',
#     data = melange_f.query("5 < Global_Sales"))
#plt.xticks(rotation=90)


# #### Graphique des genres les plus vendu au cinéma

# In[22]:


plt.figure(figsize= (15,8))
sns.barplot(
    y='Worldwide_box_office_tri',x='Genre',
    data = melange_f.query("200 < Worldwide_box_office_tri"));
plt.xticks(rotation=90)


# #### Graphique représentant les meilleurs ventes de films après 200 millions

# In[23]:


plt.figure(figsize= (15,8))
sns.barplot(
    y='Worldwide_box_office_tri',x='Surnom',
    data = melange_f.query("200 < Worldwide_box_office_tri"));
plt.xticks(rotation=90)


# In[24]:


#LC = melange_f[melange_f['Surnom']=="Lara Croft"]
#LC = LC.reset_index(drop=True)
#LC


# In[25]:


#sns.relplot(data=LC, x="Year_of_Release", y="Global_Sales", hue="Global_Sales",height=9)


# #### TEST AVEC DES JEUX VIDEOS / FILMS INDIVIDUELLEMENT 

# ##### Resident Evil

# In[27]:


RE = melange_f[melange_f['Surnom']=="Resident Evil"]
RE = RE.reset_index(drop=True)
RE


# In[28]:


sns.boxplot(
    y='Title',x='Global_Sales',
    data = RE.query("Global_Sales<3.5"),
);


# In[36]:


plt.figure(figsize= (15,8))
sns.barplot(
    y='Name',x='Global_Sales',
    data = RE,
);


# In[41]:


plt.figure(figsize= (15,8))
sns.barplot(
    y='Title',x='Worldwide_box_office_tri',
    data = RE,
);


# ##### Lara Croft

# In[31]:


LC = melange_f[melange_f['Surnom']=="Lara Croft"]
LC = LC.reset_index(drop=True)
LC


# In[37]:


plt.figure(figsize= (15,8))
sns.barplot(
    y='Name',x='Global_Sales',
    data = LC,
);


# In[39]:


plt.figure(figsize= (15,8))
sns.barplot(
    y="Title", x='Worldwide_box_office_tri',
    data = LC,
);


# In[34]:


#plt.figure(figsize= (15,8))
#sns.catplot(
#    y='Worldwide_box_office_tri',x='Global_Sales',
#    data = melange_f,
#);


# In[37]:


plt.figure(figsize= (15,8))
sns.barplot(
    y='Name',x='Global_Sales',
    data = LC,
);


# #### Alone in the Dark

# In[42]:


AID = melange_f[melange_f['Surnom']=="Alone in the Dark"]
AID = AID.reset_index(drop=True)
AID


# In[44]:


plt.figure(figsize= (15,8))
sns.barplot(
    y='Name',x='Global_Sales',
    data = AID,
);


# In[52]:


print("Worldwide box office pour Alone in the Dark : ", AID['Worldwide_box_office_tri'][0])


# #### Conclusion

# Nous pouvons conclure que même si le film dont vient le jeux vidéo peut influencer la réussite du film, cela n'est pas toujours le cas. Il faut aussi choisir des meilleurs données car les csv n'étaient pas si compatible que ça.

# In[ ]:





# In[ ]:




