


def decimal_binaire(n, precision):
    # Récupération de la partie entière et décimale de nombre choisi par l'utilisateur
    p_entiere, p_decimale = str(n).split(".")
    p_entiere = int(p_entiere)
    p_decimale = int(p_decimale) * 10**-(len(p_decimale))

    # Calcul du nombre de bits pour coder la partie entière du nombre
    puissance = 1
    while 2**puissance - 1 < p_entiere:
        puissance += 1

    # Conversion de la partie entière en binaire
    binaire_entiere = ""
    for i in range(puissance):
        reste = p_entiere % 2
        quotient = p_entiere // 2

        binaire_entiere += str(reste)
        p_entiere = quotient
    # Changement de sens de la chaine de charactère dans laquelle il y a la partie entière du nombre
    binaire_entiere = binaire_entiere[len(binaire_entiere)::-1]

    # Conversion de la partie décimale en binaire
    binaire_decimal  = ","
    compteur = 0
    arret = False
    while p_decimale != 1:
        p_decimale = p_decimale * 2
        if p_decimale > 1:
            p_decimale -= 1
            binaire_decimal += "1"
        else:
            binaire_decimal += "0"
        compteur += 1
        if compteur == precision:
            binaire_decimal += "..."
            arret = True
            break
    if arret == False:
        binaire_decimal += "1"
        
    binaire = "(" + str(n) + ")₁₀  =  " + " (" + binaire_entiere + binaire_decimal + ")₂"
    return binaire

print(decimal_binaire(1234.347, 20))