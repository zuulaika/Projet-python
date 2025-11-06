# %%
!pip install openpyxl
!pip install xlrd

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# %%

url = "https://www.data.gouv.fr/api/1/datasets/r/93438d99-b493-499c-b39f-7de46fa58669"
del_dep = pd.read_csv(url, sep=';')
print(del_dep.head())
print(del_dep.shape)


# %%
url = "https://www.data.gouv.fr/api/1/datasets/r/2690a1ed-13fb-4164-a006-2878000bf4c1"
ee2024= pd.read_excel(url, sheet_name=0)
ee2024.head()

# %%
url= "https://www.data.gouv.fr/api/1/datasets/r/4a26fcae-494b-4ef6-82bb-49fdd32c8159"
ee2019= pd.read_excel(url, sheet_name=0)
ee2019.head()

# %%
# a partir d'ici je travaille sur les tableaux des elections afin de les nettoyer. Je travaille sur un seul et j'appliquerai les memes codes a l'autre
#je divise en deux pour avoir un tableau uniquement sur les partis qui est organisé par blocs de 7 colonnes par 34 partis

# %%
ee2019_info = ee2019.iloc[:, :16]  
ee2019_parti= ee2019.iloc[:, 16:]

# %%
ee2019_parti.head()


# %%
#je renomme les colonnes car il n'ya pas de noms de colonnes à par pour le LFI

noms_premieres_colonnes = ['N°Liste', 'Libellé Abrégé Liste', 'Libellé Etendu Liste','Nom Tête de Liste', 'Voix', '% Voix/Ins', '% Voix/Exp']

#je reporte les noms dans tout le tableau
nb_blocs = len(ee2019_parti.columns)//7  
nouveaux_noms = noms_premieres_colonnes * nb_blocs
ee2019_parti.columns = nouveaux_noms

print(ee2019_parti.columns)


# %%
#Sachant qu'il ya des colonnes inutiles, on va juste se concentre sur le nom du parti et les infos sur le nbr de voix
cols_par_parti = 7
cols_utiles = [1,4,5,6] 

# on selectionne les colonnes correspondantes pour chaque partie 
cols_a_garder = []
for i in range(0, 238, cols_par_parti):
    cols_a_garder.extend([i + j for j in cols_utiles])

ee2019_parti_n = ee2019_parti.iloc[:, cols_a_garder]


ee2019_parti_n.head()


# %%
#on veut garder que les partis avec un % de voix/exp > 0.1 sinon on a trop de partie
#je prends cette decision sur a une recherche sur internet qui dit qu'il ya 11 parties principaux, les autres ayant des resultats trop faibles
#j'ai pas d'idée de comment faire mais je vais y reflechir

# %%



