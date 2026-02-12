
#init
#cartes/signes possibles
ranks = "23456789TJQKA"
suits = "cdhs"


def normaliser_carte(token):
    t = token.strip()
    if len(t) < 2:
        return t

    suit = t[-1].lower()
    rank = t[:-1].upper()

    if rank == "10":
        rank = "T"

    return rank + suit


def lire_cartes(texte):
    # Convertire
    morceaux = texte.split()
    cartes = []
    for m in morceaux:
        cartes.append(normaliser_carte(m))
    return cartes


def construire_etat_partie(board_text, holes_text_par_joueur):
    #parsing
    board = lire_cartes(board_text)

    holes = {}
    for joueur, texte in holes_text_par_joueur.items():
        holes[joueur] = lire_cartes(texte)

    return {
        "board": board,
        "holes": holes
    }


def construire_7_cartes_par_joueur(etat):
    #créer les mains à 7 cartes par joueur
    board = etat["board"]
    holes = etat["holes"]

    sept_cartes = {}
    for joueur, cartes_hole in holes.items():
        sept_cartes[joueur] = board + cartes_hole

    return sept_cartes


def afficher_resume(etat, sept_cartes):
    #test
    print("=== BOARD ===")
    print(etat["board"])
    print()

    print("=== HOLE CARDS ===")
    for joueur, cartes in etat["holes"].items():
        print(joueur, ":", cartes)
    print()

    print("=== 7 CARTES PAR JOUEUR ===")
    for joueur, cartes7 in sept_cartes.items():
        print(joueur, ":", cartes7)


if __name__ == "__main__":
    #run
    board_text = "Ac Kd Qh Js 9c"
    holes_text_par_joueur = {
        "P1": "2d 3d",
        "P2": "Ah Ad"
    }

    etat = construire_etat_partie(board_text, holes_text_par_joueur)
    sept_cartes = construire_7_cartes_par_joueur(etat)
    afficher_resume(etat, sept_cartes)
