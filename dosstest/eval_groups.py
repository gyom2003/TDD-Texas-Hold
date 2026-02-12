from pokerRef import evaluate_hand_5

def test_two_pair_bat_high_card():
    two_pair = ["As", "Ad", "Kh", "Kc", "2d"]
    one_pair = ["Qs", "Qd", "Jh", "8c", "3d"]
    assert evaluate_hand_5(two_pair)["score"] > evaluate_hand_5(one_pair)["score"]


def test_three_kind_bat_two_pair():
    trips = ["As", "Ad", "Ah", "5c", "2d"]
    two_pair = ["Ks", "Kd", "Qh", "Qc", "3d"]
    assert evaluate_hand_5(trips)["score"] > evaluate_hand_5(two_pair)["score"] 


