"""
# Les listes et leurs fonctionnements

plateforme_socials = ["Facebook", "Youtube", "Twitch"]

print(plateforme_socials)
print(len(plateforme_socials))

plateforme_socials.append("Tiktok")
print(plateforme_socials)

print(plateforme_socials[0])

plateforme_socials.remove("Facebook")
print(plateforme_socials)

plateforme_socials.sort()
print(plateforme_socials)

plateforme_socials.insert(2, "Facebook")
print(plateforme_socials)

plateforme_socials.reverse()
print(plateforme_socials)


# Les Tuples et leurs fonctionnements
# Les tuple sont donc des liste immuable, impossible a modifier


plateformes_sociales_tuple = ("Facebook", "Instagram", "TikTok", "Twitter")
print(plateformes_sociales_tuple)

print(plateformes_sociales_tuple[2])

print("Facebook" in plateformes_sociales_tuple)

"""

# Création de la liste fruit
fruits = ["Pomme", "Banane", "Orange"]
print(fruits)

# Ajout de kiwi en fin de liste
fruits.append("kiwi")
print(fruits)

# Suppression de Orange dans la liste
fruits.remove("Orange")
print(fruits)

# Remplacement de Kiwi par Ananas dans la liste
fruits[1] = "Ananas"
print(fruits)

# Affiche la longeur de la liste
print(len(fruits))

# Trie de la liste par ordre alphabétique et affichage
fruits.sort()
print(fruits)