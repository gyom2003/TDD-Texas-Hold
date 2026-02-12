from pokerRef import evaluer_main_5

def test_high_card_compare_as_haut():
    m1 = ["As", "Kd", "9h", "5c", "2d"]
    m2 = ["Ks", "Qd", "Jh", "8c", "3d"]

    s1 = evaluer_main_5(m1)
    s2 = evaluer_main_5(m2)

    assert s1["score"] > s2["score"]
    assert s1["categorie"] == "HIGH_CARD"
