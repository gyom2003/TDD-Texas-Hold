
#init
#cartes/signes possibles
ranks = "23456789TJQKA"
suits = "cdhs"

rank_value = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
    "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14
}

suit_order = {"c": 0, "d": 1, "h": 2, "s": 3}


def normalize_card(token):
    t = token.strip()
    if len(t) < 2:
        return t

    suit = t[-1].lower()
    rank = t[:-1].upper()

    if rank == "10":
        rank = "T"

    return rank + suit


def parse_cards(texte):
    # Convertire
    morceaux = texte.split()
    cartes = []
    for m in morceaux:
        cartes.append(normalize_card(m))
    return cartes


def build_game_state(board_text, holes_text_par_joueur):
    #parsing
    board = parse_cards(board_text)

    holes = {}
    for joueur, texte in holes_text_par_joueur.items():
        holes[joueur] = parse_cards(texte)

    return {
        "board": board,
        "holes": holes
    }


def build_7cards_by_player(etat):
    #créer les mains à 7 cartes par joueur
    board = etat["board"]
    holes = etat["holes"]

    sept_cartes = {}
    for joueur, cartes_hole in holes.items():
        sept_cartes[joueur] = board + cartes_hole

    return sept_cartes


def print_summary(etat, sept_cartes):
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
        
def generate_5_from_7(cartes7):
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

def iter_all_cards(board, holes):
    for c in board:
        yield c
    for joueur in holes:
        for c in holes[joueur]:
            yield c

def list_duplicates(board, holes):
    vus = {}
    doublons = []
    for c in iter_all_cards(board, holes):
        vus[c] = vus.get(c, 0) + 1
        if vus[c] == 2:
            doublons.append(c)
    return doublons


def card_value(carte):
    c = normalize_card(carte)
    return rank_value[c[0]]


def sort_cards_desc(cartes):
    normalisees = [normalize_card(c) for c in cartes]
    return sorted(
        normalisees,
        key=lambda c: (rank_value[c[0]], suit_order[c[1]]),
        reverse=True
    )


def evaluate_hand_5(main5):
    cartes = [normalize_card(c) for c in main5]
    counts = {}
      
    for c in cartes:
        r = c[0]
        counts[r] = counts.get(r, 0) + 1

    # détecter one pair
    paires = []
    for r, n in counts.items():
        if n == 2:
            paires.append(r)
            
    if len(paires) == 1:
        pair_rank = paires[0]
    
        pair_cards = [c for c in cartes if c[0] == pair_rank]
        pair_cards = sorted(pair_cards, key=lambda c: suit_order[c[1]], reverse=True)

        kickers = [c for c in cartes if c[0] != pair_rank]
        kickers = sort_cards_desc(kickers)
        
        chosen5 = pair_cards + kickers
        score = [1, rank_value[pair_rank]] + [rank_value[c[0]] for c in kickers]  # 1 = ONE_PAIR

        return {
            "categorie": "ONE_PAIR",
            "score": score,
            "chosen5": chosen5
        }


    chosen5 = sort_cards_desc(cartes)
    score = [0] + [rank_value[c[0]] for c in chosen5]

    return {
        "categorie": "HIGH_CARD",
        "score": score,
        "chosen5": chosen5
    }



def run_demo(scenario):
    if scenario == "validation":
        board = ["Ac", "Kd", "Qh", "Js", "9c"]
        holes = {"P1": ["Ac", "2d"], "P2": ["Th", "3c"]}
        print("Doublons:", list_duplicates(board, holes))

    elif scenario == "highcard":
        m1 = ["As", "Kd", "9h", "5c", "2d"]
        m2 = ["Ks", "Qd", "Jh", "8c", "3d"]
        s1 = evaluate_hand_5(m1)
        s2 = evaluate_hand_5(m2)
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

    # etat = build_game_state(board_text, holes_text_par_joueur)
    # sept_cartes = build_7cards_by_player(etat)
    # print_summary(etat, sept_cartes)
