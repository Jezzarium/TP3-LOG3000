# Fichiers Statiques (Static Assets)

Ce répertoire contient les fichiers statiques de l'application web, tels que les feuilles de style (CSS), les fichiers JavaScript et les images.

## Structure

- `style.css` : Définit le style visuel et la mise en page de l'interface de la calculatrice.

## Utilisation

Flask sert automatiquement les fichiers de ce répertoire via le chemin URL `/static/`.
Par exemple, `style.css` est lié dans les modèles HTML comme ceci :

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" />
```
