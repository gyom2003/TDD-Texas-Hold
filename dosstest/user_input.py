from pokerRef import normalize_card, parse_game

def test_normalize_card_accepts_10_and_uppercases_rank():
    assert normalize_card("10h") == "Th"
    assert normalize_card("aS") == "As"

def test_parse_game_board_and_holes_sizes():
    board, holes = parse_game(
        "Ac Kd Qh Js 9c",
        {"P1": "2d 3d", "P2": "Ah Ad"}
    )
    assert len(board) == 5
    assert len(holes["P1"]) == 2
    assert len(holes["P2"]) == 2
