# Ecole: ENSAE 
## Projet Python pour la Data Science
 Auteurs : *DIARRA ZULAIKA*, *MEMET Marie-Camille*, *TIENTCHEU Varnel* 

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
     

# Principaux résultats
L'analyse comparative entre 2019 et 2024 met en évidence une rupture structurelle majeure dans les déterminants économiques du vote en France. Alors que le paysage politique s'organisait auparavant selon une logique de classe lisible, où le Centre incarnait le vote de la stabilité et de la prospérité économique, l'année 2024 marque l'effondrement de ce modèle. Nos résultats révèlent que le vote centriste s'est déconnecté de ses ancrages matériels traditionnels : la richesse du territoire et le dynamisme de l'emploi ne sont plus des facteurs prédictifs significatifs. Ce bloc central semble désormais flotter sociologiquement, ayant perdu sa boussole économique pour ne conserver qu'une base électorale définie par défaut, isolée des réalités locales de production.

Face à ce centre devenue illisible, les oppositions se sont radicalisées autour d'une nouvelle tripartition sociale rigide. La Gauche opère un "grand écart" territorial inédit en devenant simultanément le refuge des zones de grande précarité et le choix des centres urbains aisés, tout en échouant durablement à capter le vote lié au chômage. En miroir, la Droite consolide sa position de vote du "milieu en tension", capitalisant sur les inégalités et le sentiment de déclassement intermédiaire. Elle se heurte cependant à un double rejet explicite : elle ne parvient à séduire ni les territoires les plus riches, ni les foyers de grande exclusion. Le paysage électoral français ne reflète plus une simple opposition idéologique, mais trois réalités économiques cloisonnées : la protection et l'aisance pour la Gauche, la frustration du déclassement pour la Droite, et une incertitude structurelle pour le Centre.

 # Navigation au sein du projet : 
- Première partie: Nettoyage et modelisation des données sur les élections dans les codes ... et ... et de celles sur la criminalité dans le code (Varnel)
- Deuxieme partie: Camille
- Troisième partie: Regression (Varnel) ( oublie pas de faire celle avec criminalite et chomage uniquement stp) 
     