# tests/test_generation.py
from pokerRef import build_7cards_by_player, combinations_5_from_7, generate_candidate_hands

def test_build_7cards_by_player():
    board = ["Ac", "Kd", "Qh", "Js", "9c"]
    holes = {"P1": ["2d", "3d"]}
    out = build_7cards_by_player(board, holes)
    assert len(out["P1"]) == 7
    assert out["P1"][:5] == board

def test_combinations_5_from_7_count_and_size():
    cards7 = ["Ac", "Kd", "Qh", "Js", "9c", "2d", "3d"]
    combos = combinations_5_from_7(cards7)
    assert len(combos) == 21
    assert all(len(h) == 5 for h in combos)

def test_generate_candidate_hands_smoke():
    out = generate_candidate_hands(
        "Ac Kd Qh Js 9c",
        {"P1": "2d 3d", "P2": "Ah Ad"}
    )
    assert len(out["P1"]) == 21
    assert len(out["P2"]) == 21
