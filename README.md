# astro-scripts

Scripts Python (principalement astropy) utilisés pour mon activité de vulgarisation scientifique en astronomie et astrophysique : calculs d'éphémérides, préparation d'articles sur des évènements astronomiques (éclipses, oppositions, etc.), et traitements associés à l'astrophotographie.

Ce dépôt contient le code. La documentation de chaque script (objectif, dépendances, exemple d'usage, lien vers les concepts associés) vit séparément dans mon vault Obsidian, dossier `03 - Python`.

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
