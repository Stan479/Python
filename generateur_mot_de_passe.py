from random import randint

def mdp_v1() :
    #mdp avec chiffre et lettre minuscule
    nombre_charactere = int(input("Nombre de charactere du mot de passe : "))
    charactere_mdp = "azertyuiopmlkjhgfdsqwxcvbn1234567890"
    mdp = ""
    for k in range(nombre_charactere) :
        mdp += charactere_mdp[randint(0,36)]
    print("Mot de passe : ", mdp)

def mdp_v2() :
    #mdp avec chiffre, lettre min et maj en séparant les différentes catégories de caractères
    #et en mettant aleatoirement les differents types de characteres
    nombre_charactere = int(input("Nombre de charactere du mot de passe : "))
    min = "azertyuiopmlkjhgfdsqwxcvbn"
    maj = "AZERTYUIOPMLKJHGFDSQWXCVBN"
    chiffre = "1234567890"
    mdp = ""
    for k in range(nombre_charactere) :
        type_caratere = randint(0,2)
        if type_caratere == 0 :
            mdp += min[randint(0,25)]
        elif type_caratere == 1 :
            mdp += maj[randint(0,25)]
        else:
            mdp += chiffre[randint(0,9)]
    print("Mot de passe : ", mdp)

mdp_v2()
mdp_v1()
