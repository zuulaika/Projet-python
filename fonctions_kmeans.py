from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def methode_coude(df, columns, k_min=1, k_max=10, random_state=42):
    """
    Trace la méthode du coude pour KMeans.
    
    Paramètres
    ----------
    df : pandas.DataFrame
        DataFrame contenant les données
    columns : list
        Liste des colonnes à utiliser pour le clustering
    k_min : int, default=1
        Nombre minimum de clusters
    k_max : int, default=10
        Nombre maximum de clusters
    random_state : int, default=42
        Graine pour la reproductibilité
    """
    
    # Sélection des variables
    X = df[columns]
    
    # Standardisation
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Calcul des inerties
    inertias = []
    k_values = range(k_min, k_max + 1)
    
    for k in k_values:
        km = KMeans(n_clusters=k, random_state=random_state)
        km.fit(X_scaled)
        inertias.append(km.inertia_)
    

    # Plot
    plt.figure(figsize=(6, 4))
    plt.plot(k_values, inertias, marker='o')
    plt.xlabel("k")
    plt.ylabel("Inertie")
    plt.title("Méthode du coude")
    plt.show()

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


