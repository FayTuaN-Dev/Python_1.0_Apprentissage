nombres = input("Saisissez plusieurs nombres séparer par une virgule: ")

liste = nombres.split(',')


liste_entiers = []
for i in liste:
    nombre = int(i)
    liste_entiers.append(nombre)

resultat = 0
for i in liste_entiers:
    resultat += i

moyenne = resultat / len(liste_entiers)

print(resultat)


#apres correcttion
print("Moyenne des nombres:", moyenne)

nombre_superieur_moyenne = 0
for i in liste_entiers:
    if i > moyenne:
        nombre_superieur_moyenne += 1

print(nombre_superieur_moyenne)




