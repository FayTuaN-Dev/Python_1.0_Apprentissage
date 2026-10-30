
nombre1 = input("Nombre n°1 = ")
operation = input("Quel operation choisissez vous ? (+, -, *, /) ")
nombre2 = input("Nombre n°2 = ")

nombre1 = int(nombre1)
nombre2 = int(nombre2)


match operation:
    case "+":
        resultat = nombre1 + nombre2
    case "-":
        resultat = nombre1 - nombre2  
    case "*":
        resultat = nombre1 * nombre2   
    case "/":
        if nombre2 == 0:
            raise SystemExit("On ne divise pas par 0 \nFin du programme")
        resultat = nombre1 / nombre2   
    case _:
        raise SystemExit("Fin du programme")

print(resultat)      

