#FAO Datalab : Analyse de la Sous-Nutrition au niveau mondial

Bienvenue dans le dépôt du projet **FAO Datalab**. Ce projet s'inscrit dans le cadre d'une mission de conseil réalisée pour un cabinet spécialisé en politiques alimentaires.

---

## Contexte et Problématique de la Mission

### Contexte
La FAO (Organisation des Nations Unies pour l'Alimentation et l'Agriculture) collecte chaque année des données sur la disponibilité alimentaire, la sous-nutrition et la population à l'échelle mondiale. Les données transmises sont de véritables données FAO, non modifiées de **2023**.

La sous-nutrition touche des centaines de millions de personnes à travers le monde, représentant un défi humanitaire et sanitaire majeur qui compromet le développement socio-économique des populations vulnérables. Ses conséquences directes se traduisent par des retards de croissance chez les enfants, un affaiblissement durable du système immunitaire et une baisse significative de la productivité active. 

Face à cette urgence, l'exploitation rigoureuse des données officielles de la FAO devient un levier stratégique indispensable pour guider l'action des ONG et optimiser l'aide internationale.

### Problématique
La mission consiste à produire une analyse (étude) complète des données permettant d'identifier les facteurs associés à la **sous-nutrition** dans le monde et de formuler des recommandations opérationnelles à destination du commanditaire. 

Selon la FAO, la **sous-alimentation** (souvent appelée **PoU** pour *Prevalence of Undernourishment*) désigne l'état d'un individu dont la consommation alimentaire habituelle est insuffisante pour fournir l'apport d'énergie alimentaire nécessaire pour mener une vie normale, active et en bonne santé.

### Objectifs techniques 
* **Étape 1 - Diagnostic qualité et préparation :** Auditer rigoureusement les 5 fichiers de données (valeurs manquantes, doublons, couverture géographique, unités, symboles de fiabilité, valeurs extrêmes) via la POO, puis nettoyer et fusionner les sources pour créer un dataset global.
* **Étape 2 - Analyse exploratoire et corrélations :** Mener des analyses univariées, bivariées et des tests statistiques de corrélation pour cartographier les disparités de disponibilité alimentaire et de sous-nutrition.
* **Étape 3 - Modélisation prédictive et ACP :** Développer un modèle de régression pour imputer les valeurs manquantes de sous-nutrition et réaliser une Analyse en Composantes Principales (ACP) sur les indicateurs nutritionnels.
* **Étape 4 - Clustering et restitution :** Segmenter les pays selon leurs profils alimentaires et nutritionnels via un clustering *K-Means* ($k$ déterminé par la méthode du coude).

### Objectifs opérationnels
* Cartographie des zones critiques : Identifier sans ambiguïté les pays et les régions du monde les plus touchés par la sous-nutrition chronique pour prioriser l'allocation des aides d'urgence.

* Compréhension des facteurs structurels de la malnutrition : Mesurer l'impact réel des déséquilibres alimentaires (ex: dépendance excessive aux céréales vs diversité des apports en protéines animales) sur la prévalence de la sous-alimentation.

* Aide à la décision face aux données manquantes : Grâce au modèle d'imputation, estimer la situation alimentaire de pays ou de territoires sous-dotés en statistiques officielles, permettant aux ONG d'intervenir là où l'information fait défaut.

* Ciblage par profils de pays (Clustering) : Catégoriser les pays selon leurs vulnérabilités structurelles (ex: pays souffrant de déficit calorique pur vs pays ayant des déséquilibres de distribution) afin de concevoir des politiques d'aide sur-mesure (aide alimentaire d'urgence vs transition agricole à long terme).

* Formulation de recommandations opérationnelles : Traduire les résultats statistiques en plans d'action concrets (ex: diversification des cultures, sécurisation des chaînes d'approvisionnement) présentés aux commanditaires.Conduire un diagnostic qualité rigoureux portant sur les limites réelles du jeu de données.

---
## Aperçu Visuel des Résultats
*( visuel clé généré dans  outputs a intégrer)*

> ![Carte ou Graphique de synthèse](Outputs/apercu_analyse.png)  
*Légende : Aperçu de la segmentation des pays / cartographie de la sous-nutrition.*
---

## Architecture du Projet

Le projet suit une structure modulaire et organisée pour séparer les données brutes, le code source, les scripts utilitaires et les résultats :

```text
FAO_DATALAB/
│
├── .venv/                      # Environnement virtuel Python
├── Data/
│   ├── 2023/
│   │   ├── fr_animaux.csv      # Données des produits animaux
│   │   ├── fr_céréales.csv     # Données des céréales (sous-ensemble de végétaux)
│   │   ├── fr_population.csv   # Données de population par pays (en milliers)
│   │   └── fr_vegetaux.csv     # Données des produits végétaux
│   └── Périodes_glissantes/
│       └── fr_sousalimentation.csv # Prévalence de la sous-nutrition (5 périodes glissantes)
│
├── notebooks/
│   └── Analyse_FAO.ipynb       # Notebook principal structuré par étapes
│
├── Outputs/                    # Résultats exportés (datasets propres, graphiques)
│
├── Scripts/
│   ├── __init__.py
│   └── profiler.py             # Classes orientées objet (POO : DataProfiler / ProfileurFAO)
│
├── .gitignore
├── README.md
└── requirements.txt            # Dépendances du projet


