# Mini Éditeur Hexadécimal (Python / PyQt6)

Application desktop simple permettant de :

- Convertir du texte en hexadécimal
- Convertir de l’hexadécimal en texte
- Modifier les données
- Ouvrir un fichier texte
- Sauvegarder le résultat

---

## Technologies utilisées

- MacOs
- Python 3.9.6
- PyQt6
- Environnement virtuel (`venv`)

---

## Structure du projet

binary_editor/
├── app/
│ ├── main.py
│ ├── gui.py
│ ├── converter.py
│ ├── validator.py
│ └── file_manager.py
├── tests/
│ ├── sample.txt
│ └── output.txt
├── requirements.txt
├── README.md
└── .gitignore

---

## Installation

### 1. Cloner le projet

```bash
git clone <repo_url>
cd binary_editor

2. Créer un environnement virtuel

python3 -m venv venv

3. Activer le venv

macOS / Linux :

source venv/bin/activate

Windows :

venv\Scripts\activate

4. Installer les dépendances

pip install -r requirements.txt

⸻

▶️ Lancer l’application

python3 app/gui.py

⸻

🧠 Fonctionnalités

Conversion texte → hex

Exemple :

salut → 73 61 6c 75 74

Conversion hex → texte

Exemple :

73 61 6c 75 74 → salut

Validation

* Vérifie que l’entrée hex est valide
* Évite les erreurs de conversion

Fichiers

* Ouvrir un fichier .txt
* Sauvegarder le résultat

⸻

⚠️ Limitations

* Pas un vrai éditeur hexadécimal (pas d’offset, etc.)
* Format simplifié : 1 octet = 2 caractères hex séparés par des espaces
* Support limité aux caractères ASCII / UTF-8 simples

⸻

Dépendances

Exemple (requirements.txt) :

PyQt6==6.x.x

(Version exacte selon environnement → voir pip freeze)

⸻

Auteur
Reynier Pascal
Projet réalisé dans le cadre d’un module Python dans la formation ZeroDay Académie.
```
