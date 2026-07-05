# astro-scripts

Ce dépôt est un espace de calcul partagé regroupant mes scripts Python, principalement basés sur astropy : calculs d'éphémérides, préparation des évènements astronomiques (éclipses, oppositions, etc.), et traitements associés à l'astrophotographie.

## Structure

Un script ou un petit groupe de scripts liés par fichier dans `scripts/`. Chaque script commence par un docstring décrivant :

- son objectif en une phrase
- ses dépendances principales
- un exemple d'usage concret

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Licence

MIT, voir `LICENSE`.
