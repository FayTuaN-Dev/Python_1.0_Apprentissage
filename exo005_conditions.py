
nombre1 = input("Nombre n°1 = ")
operation = (input("Quel operation choisissez vous ? (+, -, *, /) "))
nombre2 = input("Nombre n°2 = ")

nombre1 = int(nombre1)
nombre2 = int(nombre2)

resultat = None

if operation not in ["+", "-","*","/"]:
    raise SystemExit("Le symbole d'operation n'est pas valide")

match operation:
    case "+":
        resultat = nombre1 + nombre2
        print(resultat)
    case "-":
        resultat = nombre1 - nombre2
        print(resultat)
    case "*":
        resultat = nombre1 * nombre2
        print(resultat)
    case "/":
        if nombre1 == 0 or nombre2 == 0:
            raise SystemExit("On ne divise pas par 0 \nFin du programme")
        resultat = nombre1 / nombre2
        print(round(resultat))
    case _:
        raise SystemExit("Fin du programme")

