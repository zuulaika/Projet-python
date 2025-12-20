
import numpy as np
import pandas as pd

def selection_top_partis(df_parti, cols_par_bloc=2, n_top=10):
    somme_voix_exp = []
    #Calcul du poids national de chaque parti
    for i in range(0, df_parti.shape[1], cols_par_bloc):
        bloc = df_parti.iloc[:, i:i+cols_par_bloc]
        nom_parti = bloc.iloc[0, 0]
        total_parti = bloc.iloc[:, 1].sum()
        somme_voix_exp.append((nom_parti, total_parti))

    df_somme = pd.DataFrame(somme_voix_exp, columns=["Parti", "total_%"])
    df_somme = df_somme.sort_values("total_%", ascending=False)

    #Sélection des 10 partis les plus representés
    top_partis = df_somme.iloc[:n_top, 0].unique()

    #Filtrage du tableau initial
    cols_a_garder = []
    for i in range(0, df_parti.shape[1], cols_par_bloc):
        bloc = df_parti.iloc[:, i:i+cols_par_bloc]
        if bloc.iloc[0, 0] in top_partis:
            cols_a_garder.extend(range(i, i+cols_par_bloc))

    df_filtre = df_parti.iloc[:, cols_a_garder]
    return df_filtre, df_somme


def chang_col(df, cols_par_bloc=2):
    cols_a_garder = []
    noms_colonnes = []
    for i in range(0, df.shape[1], cols_par_bloc):
        bloc = df.iloc[:, i:i+cols_par_bloc]
        nom_parti = bloc.iloc[0, 0]

        col_index = i + 1
        cols_a_garder.append(col_index)
        noms_colonnes.append(nom_parti)

    df_final = df.iloc[:, cols_a_garder].copy()
    df_final.columns = noms_colonnes

    return df_final
