from pokerRef import generate_5_from_7

def test_21_combinations():
    cartes7 = ["Ac", "Kd", "Qh", "Js", "9c", "2d", "3d"]
    mains = generate_5_from_7(cartes7)
    assert len(mains) == 21