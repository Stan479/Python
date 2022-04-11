#import numpy

def convert_romain():
    """
    I = 1; V = 5; X = 10; L = 50; C= 100;D = 500; M = 1000
    https://fr.wikipedia.org/wiki/Numération_romaine#Modes_de_représentation
    sauf qu'un symbole ne se repetera pas plus de 3 fois
    se lit de gauche a droite
    IX = 9 ; XI = 11,  si symbole av + petit = soustraction et si + grand = addition
    marche pour nombre de 2 rang au dessus (addition) ou en dessous (soustraction)
    ex : IV ok ; IX ok ; IC non 99 s'écrit XCIX
    """
    nombre_decimal = int(input("Entrer un nombre (entre 1 et 3999) : "))
    if not 1 <= nombre_decimal <= 3999:
        print("Entrer un nombre entier entre 1 et 3999.")
        convert_romain()
    romain = [1, 5, 10, 50, 100, 500, 1000]
    lettre_romain = ["I", "V", "X", "L", "C", "D", "M"]
    # nombre_romain = [0] * 7  # stocke le nombre de fois que je soustrait une certaine valeur
    difference = nombre_decimal  # stocke le résultat des soustraction successive
    test = -1  # permet de faire varier la valeur soustraite
    conversion = ""
    while difference != 0:
        if (difference - romain[test]) >= 0:  # and nombre_romain[test] < 3:
            # pour respecter la règle des 3 symboles successifs
            # nombre_romain[test] += 1
            conversion += lettre_romain[test]  # j'ajoute les lettre progressivement
            difference -= romain[test]
            continue
        if difference - romain[test] < 0 and difference > abs(difference - romain[test]):
            if str(difference)[0] == "9":
                conversion += lettre_romain[test - 2] + lettre_romain[test]
                difference = difference + romain[test - 2] - romain[test]
                # print("boucle 2")
                continue
            if str(difference)[0] == "4":  # adapter a 4
                conversion += lettre_romain[test - 1] + lettre_romain[test]
                difference = difference + romain[test - 1] - romain[test]
                # print("boucle 3")
                continue
        if -test < len(romain):
            test -= 1

    print(nombre_decimal, " = ", conversion)

convert_romain()