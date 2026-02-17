# Modèles (Templates)

Ce répertoire contient les modèles HTML Jinja2 utilisés par l'application Flask pour afficher l'interface utilisateur.

## Structure

- `index.html` : L'interface principale de la calculatrice. Elle contient le formulaire de saisie des expressions et affiche le résultat.

## Utilisation

Ces modèles sont rendus par le backend `app.py` en utilisant la fonction `render_template` de Flask.
Exemple :

```python
return render_template('index.html', result=result)
```

Les modèles utilisent la syntaxe Jinja2 (par ex. `{{ result }}`) pour insérer du contenu dynamique transmis par le backend.
