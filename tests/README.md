# Tests

Ce répertoire contient la suite de tests pour l'application de calculatrice.

## Structure

- `test_operators.py` : Tests unitaires pour `operators.py`.
- `test_app.py` : Tests d'intégration pour `app.py`.

## Exécution des tests

Pour exécuter tous les tests, lancez la commande suivante depuis la racine du projet :

```bash
python -m unittest discover tests
```

Pour exécuter un fichier de test spécifique :

```bash
python -m unittest tests/test_operators.py
```
