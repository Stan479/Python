print("Jeux pierre,papier,ciseaux")
nombre_manche = int(input("Nombre de manches : "))
def jeux(nombre_manche) :
    from random import randint
    score_joueur = 0
    score_ordinateur = 0
    manche_jouée = 1
    while manche_jouée <= nombre_manche :
        joueur = input("A vous de jouer : ")
        choix_ordi = ("pierre","papier","ciseaux")
        ordinateur = choix_ordi[randint(0,2)]
        if joueur not in ("pierre","papier","ciseaux") :
            print("Rejouer, vous devez ecrire pierre, papier ou ciseaux.")
            continue
        if joueur == ordinateur :
            print("L'ordinateur a joué " + ordinateur + ",rejouez.")
            manche_jouée -= 1
        elif (joueur == "pierre" and ordinateur == "ciseaux") or (joueur == "papier" and ordinateur == "pierre") or (joueur == "ciseaux" and ordinateur == "papier") :
            print("L'ordinateur a joué " + ordinateur + ", vous avez gagné")
            score_joueur += 1
        else :
            print("L'ordinateur a joué " + ordinateur + ", vous avez perdu")
            score_ordinateur += 1
        manche_jouée += 1

    if score_ordinateur > score_joueur :
        winner = "L'ordinateur a gagné la partie"
    elif score_ordinateur < score_joueur :
        winner = "Vous avez gagné la partie"
    else:
        winner = "Il y a égalité, match nul"

    print("\nVous avez gagné ", score_joueur, " manches \n"
            "L'ordinateur a gagné ", score_ordinateur, " manches\n"
             ,winner )

jeux(nombre_manche)