
**Git** est un système de contrôle de version distribué créé en 2005 par Linus Torvalds.  Il s'agit d'un logiciel libre et open source qui fonctionne localement sur la machine de l'utilisateur pour suivre chronologiquement les modifications apportées aux fichiers et au code source, permettant ainsi de gérer les versions et de revenir en arrière si nécessaire. 

**GitHub** est une plateforme web en ligne (détenue par Microsoft) qui permet d'héberger des dépôts Git dans le cloud.  Contrairement à Git qui est l'outil technique de gestion des versions, GitHub fournit une interface collaborative, des outils de gestion de projet (comme les tickets et les pull requests) et facilite le travail d'équipe en centralisant le partage et la visibilité du code. 


**Le schéma à retenir** :

Dossier de travail --git add--> zone de préparation --git commit--> historique local --git push--> GitHub

Tout se passe sur ma machine jusqu'au `git push`.


**Commande Windows/linux** :

**Utilisation basique:

- mkdir nomduprojet //Permet de créer un dossier pour le projet

- cd nomduprojet //Permet de ce rendre dans le dossier du projet

**Les commandes Git/Github**:

**Configuration (une seule fois)**:

    - git config --global user.name "Mon nom" // Le nom qui sera associé à mes commits

    - git config --global user.email "mon@mail" // L'email associé à mes commits (le même que sur GitHub)

**Utilisation basique**:

    - git init // Permet de créer un dossier .git caché qui contient tous l'historique (il ne crée pas de .gitignore, je le crée moi-même)

    - git status // Connaitre ce qui na pas encore été validé

    - git log // Liste tous les commits effectué dans le dépot

**Récupération du dépot**:

    - git clone (lien https github) // Récupere le depot github sur votre machine (dans un nouveau dossier, déjà lié à GitHub)

**Lier un dossier existant à GitHub** (si je n'ai pas fait de clone):

    - git remote add origin (lien https github) // Indique à Git où se trouve le dépôt GitHub

    - git push -u origin main // Premier envoi, ensuite un simple "git push" suffit

**Gestion des fichier**:

    - git add nomdufichier // Permet de préparer les fichiers qui seront envoyer au prochain commit (rien n'est envoyé à GitHub ici)

    - git add . // Permet de préparer tous le dossier qui sera envoyer au prochain commit & push

    - git rm nomdufichier // Permet de supprime le fichier en local et sera aussi supprimer de github au prochain commit & push

    - git mv ancien nouveau // Permet de déplacer ou renommer un fichier (ex: git mv exo001.py boucles/exo001.py). Le changement arrive sur github au prochain commit & push

**Gestion des Commit**:

    - git pull // Permet de récuperer la derniere version du depot github

    - git commit -m "message" // Enregistre une étape dans l'historique local avec un message clair (ex: "Ajout exo001 : variables"). Il enregistre ce qui a été préparé avec git add

    - git commit -a -m "message" // Pareil, mais prépare automatiquement les fichiers déjà suivis (ne prend pas les nouveaux fichiers)

    - git push origin main // Permet d'envoyer les commits vers github (main est le nom par défaut, master est l'ancien nom)


**Mon flux de travail pour le stream**:

    1. git status // Voir ce qui a changé
    2. git add . // Préparer les fichiers
    3. git commit -m "message" // Enregistrer l'étape
    4. git push // Envoyer sur GitHub


**Le fichier .gitignore**:

Fichier texte à la racine du projet qui liste ce que Git doit ignorer (jamais envoyé sur GitHub): mots de passe, clés, fichiers de config perso, dossiers inutiles.

Exemple pour Python:

    __pycache__/
    *.pyc
    .env
    venv/


**Utilisation avancée**:

    - git branch // Permet de lister les branch locales

    - git branch nomdelabranch // Permet de créer une branch (en local) pour pouvoir travailler sans casser la branch main pendant le developpement

    - git switch nomdelabranch // Permet de changer de branch (ex: main -> developpement). L'ancienne commande était git checkout nomdelabranch, elle marche toujours

    - git merge nomdelabranch // Je me place sur main, puis je fusionne la branch en developpement dans main

    - git branch -d nomdelabranch // Permet de supprimer la branch en local

    - git push origin --delete nomdelabranch // Supprime la branch sur github

    - git push origin nomdelabranch // Permet d'envoyer la branche vers le depot github

**Comparaison de version**:

- git diff // Compare mes fichiers actuels avec le dernier commit local (pas avec github)

- git fetch puis git diff origin/main // Compare mes fichiers avec la version qui est sur github

- git diff commit1 commit2 // Compare deux commits de l'historique local


