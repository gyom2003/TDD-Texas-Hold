from pokerRef import list_duplicates

def test_detecte_doublon_global():
    board = ["Ac", "Kd", "Qh", "Js", "9c"]
    holes = {"P1": ["Ac", "2d"], "P2": ["Th", "3c"]}
    assert list_duplicates(board, holes) == ["Ac"]
