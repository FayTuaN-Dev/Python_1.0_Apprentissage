**Commande Windows/linux** :

**Commande Python**:

    - python3 --version // Voir la version python installé

    - python3 -m venv .venv // Permet de créer l'environnement isolé dans un dossier .venv

    - source .venv/bin/activate // Permet d'activer l'environnement isolé du dossier (Linux)
    
    - .venv\Scripts\activate // Permet d'activer l'environnement isolé du dossier (Windows, PowerShell ou CMD). Dans Git Bash : source .venv/Scripts/activate

    - deactivate // Permet de sortir de l'environnement isolé du dossier

    - python3 nomdufichier.py // Permet de lancer le script dans la console

Note : sur la Pi (Linux) on tape python3, sous Windows on tape souvent python.
Quand le venv est actif, (.venv) s'affiche au début de la ligne de commande.

**Commande pip**

    - pip install nomdupaquet // Permet d'installer une bibliothèque (dans le venv actif)

    - pip list // Permet de voir tous ce qui est installée en tant que bibliothèque

    - pip freeze > requirements.txt // Permet de sauvegarder la liste des dépandances

    - pip install -r requirements.txt // Permet d'installer les dépandances

**Bon à savoir**

    - Ajouter .venv/ dans le .gitignore : on n'envoie jamais le venv sur GitHub, seulement requirements.txt

    - Sur la Pi, si la création du venv ne marche pas : sudo apt install python3-venv
