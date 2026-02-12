
#init
#cartes/signes possibles
ranks = "23456789TJQKA"
suits = "cdhs"

rang_vers_valeur = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
    "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14
}

ordre_suit = {"c": 0, "d": 1, "h": 2, "s": 3}


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
        
def generer_mains_5_parmi_7(cartes7):
    #loop pour générer les mains 5 cartes
    resultats = []
    n = len(cartes7)

    for i in range(0, n - 4):
        for j in range(i + 1, n - 3):
            for k in range(j + 1, n - 2):
                for l in range(k + 1, n - 1):
                    for m in range(l + 1, n):
                        resultats.append([cartes7[i], cartes7[j], cartes7[k], cartes7[l], cartes7[m]])

    return resultats

def iterer_toutes_les_cartes(board, holes):
    for c in board:
        yield c
    for joueur in holes:
        for c in holes[joueur]:
            yield c

def lister_doublons(board, holes):
    vus = {}
    doublons = []
    for c in iterer_toutes_les_cartes(board, holes):
        vus[c] = vus.get(c, 0) + 1
        if vus[c] == 2:
            doublons.append(c)
    return doublons


def valeur_carte(carte):
    c = normaliser_carte(carte)
    return rang_vers_valeur[c[0]]


def trier_cartes_desc(cartes):
    normalisees = [normaliser_carte(c) for c in cartes]
    return sorted(
        normalisees,
        key=lambda c: (rang_vers_valeur[c[0]], ordre_suit[c[1]]),
        reverse=True
    )


def evaluer_main_5(main5):
    #hight card (0)
    chosen5 = trier_cartes_desc(main5)
    score = [0] + [rang_vers_valeur[c[0]] for c in chosen5]

    return {
        "categorie": "HIGH_CARD",
        "score": score,
        "chosen5": chosen5
    }

def run_demo(scenario):
    if scenario == "validation":
        board = ["Ac", "Kd", "Qh", "Js", "9c"]
        holes = {"P1": ["Ac", "2d"], "P2": ["Th", "3c"]}
        print("Doublons:", lister_doublons(board, holes))

    elif scenario == "highcard":
        m1 = ["As", "Kd", "9h", "5c", "2d"]
        m2 = ["Ks", "Qd", "Jh", "8c", "3d"]
        s1 = evaluer_main_5(m1)
        s2 = evaluer_main_5(m2)
        print("m1:", s1)
        print("m2:", s2)
        print("m1 > m2 ?", s1["score"] > s2["score"])

    else:
        print("Scenario inconnu. Utilise: validation | highcard")
    
        


if __name__ == "__main__":
    #run
    import sys
    s = sys.argv[1] if len(sys.argv) > 1 else "base"
    run_demo(s)
    # board_text = "Ac Kd Qh Js 9c"
    # holes_text_par_joueur = {
    #     "P1": "2d 3d",
    #     "P2": "Ah Ad"
    # }

    # etat = construire_etat_partie(board_text, holes_text_par_joueur)
    # sept_cartes = construire_7_cartes_par_joueur(etat)
    # afficher_resume(etat, sept_cartes)
