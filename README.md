# Ecole: ENSAE 
## Projet Python pour la Data Science
 Auteurs : *DIARRA Zulaika*, *MEMET Marie-Camille*, *TIENTCHEU Varnel* 

 # Sujet :
 <div align="justify">
 Les élections constituent un révélateur essentiel des dynamiques sociales, économiques et territoriales. En France, les comportements électoraux présentent de fortes disparités spatiales, notamment entre départements, qui peuvent être liées à des facteurs socio-économiques tels que le chômage ou la criminalité.
 Dans le cadre de ce projet, nous nous intéressons aux élections européennes de 2019 et de 2024, en cherchant à comprendre comment les conditions économiques et sociales locales peuvent influencer les choix de vote. 
 L’objectif est de dépasser l’analyse par partis isolés et de proposer une lecture synthétique et à l'échelle nationale des comportements électoraux à travers les grands bords politiques : gauche, centre et droite

 # Problématique : 
 Quels sont les déterminants socio-économiques des choix de vote aux élections européennes en France ? Les profils électoraux observés en 2019 sont-ils comparables à ceux de 2024 ?

 # Modèle utilisé et outils utiliés: 
 Le travail préparatoire a consisté en une restructuration complète des bases de données électorales, couplée à une stratégie d'enrichissement par des indicateurs socio-économiques tels que le chômage et la criminalité. Cette phase cruciale de nettoyage a permis d'agréger la multitude de listes candidates en trois grands blocs idéologiques (Gauche, Centre, Droite), facilitant ainsi une lecture macroscopique et comparative des dynamiques territoriales.

Sur le plan analytique, une première approche exploratoire non-supervisée par clustering (K-means) a été mise en œuvre pour faire émerger une typologie des départements français. Cette méthode a permis d'identifier des profils électoraux homogènes basés uniquement sur la ressemblance des scores, indépendamment des critères purement géographiques, révélant ainsi des structures territoriales latentes.

Enfin, le cœur de l'étude repose sur une modélisation par Régression Linéaire Multiple (OLS) via statsmodels, préférée aux algorithmes de prédiction complexes pour sa capacité explicative. Cette approche permet d'isoler l'impact spécifique de chaque variable toutes choses égales par ailleurs (Ceteris Paribus). Afin de garantir la rigueur des résultats, toutes les variables explicatives ont été standardisées (Z-Score) pour rendre les coefficients directement comparables, tandis que l'utilisation d'estimateurs de variance robustes (HC1) a permis de corriger l'hétéroscédasticité potentielle et d'assurer la fiabilité statistique des tests de significativité.

 # Données utilisées :
 - Résultats des élections européennes 2019 et 2024, par département:
   https://www.data.gouv.fr/datasets/resultats-des-elections-europeennes-2019
     https://www.data.gouv.fr/datasets/resultats-des-elections-europeennes-du-9-juin-2024

Bien que les données électorales, le taux de chômage et les statistiques de criminalité soient parfaitement synchronisés pour chaque élection, une contrainte technique s'est imposée pour l'analyse de 2019. Faute de disponibilité immédiate des indicateurs socio-économiques précis pour cette année-là (revenu médian, pauvreté, diplômes), nous avons utilisé les données de 2022 comme variables de substitution (proxies). Nous sommes conscients que cette approximation est forte, étant donné les bouleversements majeurs survenus entre ces deux dates (crise sanitaire, inflation), mais ces indicateurs structurels restent suffisamment stables à court terme pour fournir une estimation pertinente des dynamiques territoriales de l'époque, faute de mieux.
     

# Principaux résultats
L'étude montre que le paysage politique a complètement changé entre 2019 et 2024. Le fait le plus marquant, c'est que le vote du Centre ne suit plus les règles économiques d'avant. En 2019, c'était simple : plus un département était riche et avait de l'emploi, plus il votait au Centre. Aujourd'hui, ce lien est cassé. Nos chiffres prouvent qu'en 2024, on ne peut plus prédire le vote centriste grâce au niveau de vie ou au taux de chômage. Ce bloc politique a perdu sa "boussole" économique et semble flotter, sans base sociale aussi claire qu'avant.

À l'inverse, les autres camps se sont radicalisés dans des directions opposées. La Gauche fait désormais un véritable "grand écart" : elle attire à la fois les populations les plus pauvres et les habitants aisés des grandes villes, mais elle n'arrive toujours pas à capter le vote des chômeurs. De l'autre côté, la Droite s'est installée comme le vote de la "France du milieu qui souffre". Elle réalise ses meilleurs scores là où il y a du chômage et des inégalités, mais elle est rejetée par les deux extrêmes : elle ne séduit ni les plus riches, ni les plus pauvres. En résumé, on a trois blocs qui correspondent désormais à trois réalités économiques totalement séparées.

 # Navigation au sein du projet : 
- Le fichier *CODE_PRINCIPAL.ipynb* représente le code de base de notre travail et comporte successivement:
    - Le nettoyage et la mise en forme des données sur les élections;
    - L'analyse cartographique du chômage en 2019 et en 2024;
    - La répartition des départements sous forme de clusters par la méthode K-means;
    - La modélisation des résultats de vote au moyen d'un modèle de régression Linéaire multiple.

- Le fichier *datasets.ipynb* contient le code pour récupérer toutes les variables explicatives nécessaires pour le modèle de regression. C'est grâce à lui qu'on obtient le fichier *df_regressions.csv*.

- Le fichier *criminalite.ipynb* présente une analyse descriptive plus détaillée de l'évolution de la criminalité en France depuis 2013.

- Les fichiers *ee_bp19.csv* et *ee_bp24.csv* représentent les bases finales nettoyées et prêtes à l'emploi, résultant de la partie nettoyage du fichier *CODE_PRINCIPAL.ipynb*


