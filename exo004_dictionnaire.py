"""
# Création du dictionnaire
nouvelle_campagne = {
"responsable_de_campagne": "Jeanne d'Arc",
"nom_de_campagne": "Campagne nous aimons les chiens",
"date_de_début": "01/01/2020",
"influenceurs_importants": ["@MonAmourDeChien", "@MeilleuresFriandisesPourChiens"]
}

# Affiche un valeur de la clé choisi dans le dictionnaire
print(nouvelle_campagne['responsable_de_campagne'])

# Créer une nouvelle clé-valeur et ajout dan sle dictionnaire
nouvelle_campagne['Nombre_de_follower'] = 3589
print(nouvelle_campagne)

# Supprime une clé et sa valeur du dictionnaire
del nouvelle_campagne["date_de_début"]
print(nouvelle_campagne)

# Test des différentes méthode du dictionnaire

# Affiche uniquement les clés du dictionnaire
print(nouvelle_campagne.keys())
# Affiche uniquement les valeurs du dictionnaire
print(nouvelle_campagne.values())
# Affiche une vue des couples (clé-valeur) du dictionnaire
print(nouvelle_campagne.items())

# Affiche un valeur de la clé choisi dans le dictionnaire
print(nouvelle_campagne['influenceurs_importants'])
print(nouvelle_campagne.get("influenceurs_importants"))

# Verifie l'existence d'une clé dans le dictionnaire
print("responsable_de_campagne" in nouvelle_campagne)

# Supprime toutes les clé et valeur du dictionnaire
nouvelle_campagne.clear()
print(nouvelle_campagne)

"""

fruits = dict()

fruits["pomme"] = "rouge"
fruits["banane"] = "jaune"
fruits["orange"] = "orange"

print(fruits)

fruits["kiwi"] = 'vert'

print(fruits)

couleur_banane = fruits["banane"]
print(couleur_banane)

fruits['pomme'] = 'vert'
print(fruits)

del fruits['banane']
print(fruits.keys())