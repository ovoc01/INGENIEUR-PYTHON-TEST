          
# README - Test Tanyah Consulting

Ce README fournit les instructions pour lancer et utiliser les deux projets contenus dans ce dépôt : "applaudissement" et "interaction-kili".

## Table des matières
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Projet Applaudissement](#projet-applaudissement)
  - [Description](#description-applaudissement)
  - [Structure du projet](#structure-applaudissement)
  - [Utilisation](#utilisation-applaudissement)
- [Projet Interaction-Kili](#projet-interaction-kili)
  - [Description](#description-interaction-kili)
  - [Configuration](#configuration-interaction-kili)
  - [Structure du projet](#structure-interaction-kili)
  - [Utilisation](#utilisation-interaction-kili)

## Prérequis

- Python 3.x
- pip (gestionnaire de paquets Python)

## Installation

1. Clonez ce dépôt sur votre machine locale :
```bash
git clone https://github.com/ovoc01/INGENIEUR-PYTHON-TEST.git
cd INGENIEUR-PYTHON-TEST
```

2. Installez les dépendances requises :
```bash
pip install -r requirements.txt
```

## Projet Applaudissement

### Description Applaudissement

Le projet "applaudissement" est conçu pour résoudre un problème algorithmique. Il analyse un fichier d'entrée contenant des données sur le nombre de personnes debout à chaque instant et calcule le nombre minimum d'amis nécessaires pour que tout le monde puisse se lever et applaudir.

### Structure Applaudissement

```
applaudissement/
├── dataset/
│   ├── A-large-practice.in
│   └── A-small-practice.in
├── output/
└── main.py
```

### Utilisation Applaudissement

Pour exécuter le programme avec les fichiers d'exemple :

```bash
python -c "from applaudissement.main import resolve; resolve('applaudissement/dataset/A-small-practice.in', 'applaudissement/output/A-small-practice.out')"
```

Vous pouvez également modifier le fichier `main.py` pour utiliser d'autres fichiers d'entrée/sortie.

## Projet Interaction-Kili

### Description Interaction-Kili

Le projet "interaction-kili" est conçu pour interagir avec l'API Kili. Il récupère des données d'annotations d'objets (Asterix et Obelix) à partir d'un projet Kili, calcule les aires des boîtes englobantes et enregistre les résultats dans un fichier JSON.

### Configuration Interaction-Kili

1. Créez un fichier `.env` à la racine du projet en vous basant sur le fichier `.env.example` :
```bash
cp .env.example .env
```

2. Modifiez le fichier `.env` pour ajouter votre clé API Kili :
```
KILI_API_KEY=votre_clé_api
```

### Structure Interaction-Kili

```
interaction-kili/
├── main.py
└── results.json (généré après exécution)
```

### Utilisation Interaction-Kili

Pour exécuter le programme et récupérer les données depuis Kili :

```bash
python interaction-kili/main.py
```

Le programme va :
1. Se connecter à l'API Kili avec votre clé API
2. Récupérer les annotations du projet spécifié
3. Calculer les aires des boîtes englobantes pour les objets Asterix et Obelix
4. Afficher les résultats dans la console
5. Enregistrer les résultats dans un fichier `results.json`

---

Pour toute question ou problème, veuillez créer une issue dans ce dépôt.

        