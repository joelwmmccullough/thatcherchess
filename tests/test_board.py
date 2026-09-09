from thatcherchess.board import diamond, is_connected


def test_the_diamond_has_61_cells():
    assert len(diamond().cells) == 61

def test_the_diamond_is_contiguous():
    assert is_connected(diamond().cells) == True

def test_two_islands_are_not_connected():
    assert not is_connected({(0, 0), (10, 10)})

def test_the_diamond_widens_then_narrows():
    cells = diamond().cells
    widths = [sum(1 for col, row in cells if row == r) for r in range(11)]
    assert widths == [1,3,5,7,9,11,9,7,5,3,1]

def test_every_starting_piece_is_in_bounds():
    shape = diamond()
    for piece in shape.player_start + shape.thatcher_start:
        assert shape.in_bounds((piece.col, piece.row))
