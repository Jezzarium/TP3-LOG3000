# Calculatrice Web Simple (Flask)

**Numéro d'équipe :** 20
**Cours :** LOG3000 - Devoir #3

## Description du Projet

Ce projet est une application web de calculatrice simple développée avec **Python** et **Flask**. Elle permet aux utilisateurs d'effectuer des opérations arithmétiques de base (addition, soustraction, multiplication, division) via une interface web intuitive.

L'objectif principal est de fournir une base de code structurée pour démontrer les bonnes pratiques de développement logiciel, incluant la documentation, les tests unitaires et d'intégration, ainsi que la gestion de versions avec Git.

## Fonctionnalités

- Interface web simple pour saisir des expressions mathématiques.
- Supporte les opérations : `+`, `-`, `*`, `/`.
- Gestion des erreurs de syntaxe et de calcul.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- **Python 3.9+** (requis par Flask)
- **pip** (gestionnaire de paquets Python)
- **Git**

## Installation

1. **Cloner le dépôt**

   ```bash
   git clone https://github.com/Jezzarium/TP3-LOG3000.git
   cd TP3-LOG3000
   ```

2. **Créer un environnement virtuel (Recommandé)**

   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Installer les dépendances**
   ```bash
   pip install flask
   ```

## Utilisation

1. **Lancer l'application**

   ```bash
   python app.py
   ```

   Vous devriez voir une sortie indiquant que le serveur tourne sur `http://127.0.0.1:5000`.

2. **Accéder à la calculatrice**
   Ouvrez votre navigateur web et allez à l'adresse : [http://localhost:5000](http://localhost:5000)

3. **Calculer**
   - Entrez une expression (ex: `10 + 5`) dans le champ de saisie.
   - Appuyez sur le bouton "=".
   - Le résultat s'affichera à l'écran.

## Tests

Ce projet inclut une suite de tests pour vérifier le bon fonctionnement du backend et des opérateurs.

Pour exécuter les tests :

```bash
python -m unittest discover tests
```

_Note : Si des tests échouent, cela peut indiquer des bogues connus qui seront résolus dans les branches de correction._

## Contribution

Nous suivons un flux de travail basé sur les branches pour la contribution :

1. **Signaler un problème** : Ouvrez une Issue GitHub pour décrire le bogue ou la fonctionnalité manquante.
2. **Créer une branche** : Créez une nouvelle branche à partir de `main` pour votre travail.
   ```bash
   git checkout -b nom-du-correctif
   ```
3. **Développer et Tester** : Apportez vos modifications et assurez-vous que les tests passent.
4. **Soumettre une Pull Request (PR)** : Poussez votre branche et ouvrez une PR vers `main` pour revue.

## Structure du Projet

- `app.py` : Point d'entrée de l'application Flask et routes.
- `operators.py` : Logique métier des opérations mathématiques.
- `templates/` : Fichiers HTML.
- `static/` : Fichiers CSS et assets.
- `tests/` : Tests unitaires et d'intégration.
