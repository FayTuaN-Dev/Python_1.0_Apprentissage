salaire_annuel = float(input("Quel est votre salaire annuel ? "))
heures_travaillees = float(input("Quel est votre temps de travaille hebdo ? "))

def salaire_mensuels(salaire_annuel):
    salaire_mensuel = salaire_annuel / 12

    return salaire_mensuel
salaire_mensuel = salaire_mensuels(salaire_annuel)


def salaire_hebdomadaires(salaire_mensuel):
    salaire_hebdomadaire = salaire_mensuel / 4

    return salaire_hebdomadaire
salaire_hebdomadaire = salaire_hebdomadaires(salaire_mensuel)


def salaire_horaires(salaire_hebdomadaire, heures_travaillees):
    heure_travaillees = salaire_hebdomadaire / heures_travaillees

    return heure_travaillees
heure_travaillees = salaire_horaires(salaire_hebdomadaire, heures_travaillees)


#print(salaire_mensuels(salaire_annuel), salaire_hebdomadaires(salaire_mensuel), salaire_horaires(salaire_hebdomadaire, heures_travaillees))
print(f"Votre salaire horaire est de {heure_travaillees} euros")