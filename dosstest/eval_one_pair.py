from pokerRef import evaluer_main_5

def test_one_pair_bat_high_card():
    pair = ["As", "Ad", "9h", "5c", "2d"]
    high = ["Ks", "Qd", "Jh", "8c", "3d"]
    assert evaluer_main_5(pair)["score"] > evaluer_main_5(high)["score"]

def test_one_pair_kicker():
    p1 = ["As", "Ad", "Kh", "5c", "2d"]
    p2 = ["As", "Ad", "Qh", "5c", "2d"]
    assert evaluer_main_5(p1)["score"] > evaluer_main_5(p2)["score"]
