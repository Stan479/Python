print("Bienvenue dans le jeu du juste prix")
print("Le chiffre sera compris entre une valeur a et b ")
a = int(input("a = "))
b = int(input("b = "))
if a == b:
    print("a et b doivent être différents")


def croissant(a, b):
    if a < b:
        return a, b
    else:
        return b, a


def gagnant():
    from random import randint
    intervalle = croissant(a, b)
    chiffre = randint(intervalle[0], intervalle[1])
    gagner = False
    score = 0
    while gagner == False:  # on pourrait remplacer la condiotion par "not gagner" pour simplifier
        test = int(input("Donner un chiffre : "))
        if test < chiffre:
            print("C'est plus")
            score += 1
        elif test > chiffre:
            print("C'est moins")
            score += 1
        else:
            print("Vous avez gagné après " + str(score) + " tentatives")
            gagner = True


gagnant()

# ca serait mieux de faire "donner un chiffre" la premiere fois et ensuite de faire "essayer encore"
