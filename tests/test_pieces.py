"""Move generation tests"""

from thatcherchess.board import diamond
from thatcherchess.pieces import Piece, legal_targets

DIAMOND = diamond()


def test_rook_slides_until_blocked_by_a_friend():
    rook = Piece(kind="rook", side="player")
    pieces = {(5,5): rook, (5,3): Piece(kind="pawn", side="player")}
    targets = legal_targets(rook, (5,5), DIAMOND, pieces)
    assert (5,4) in targets          #sidle up to friendly pawn
    assert (5,3) not in targets      #can't move onto friendly pawn
    assert (5,2) not in targets      #can't move past friendly pawn


def test_rook_captures_an_enemy_and_stops_there():
    rook = Piece(kind="rook", side="player")
    pieces = {(5,5): rook, (5,3): Piece(kind="pawn", side="thatcher")}
    targets = legal_targets(rook, (5,5), DIAMOND, pieces)
    assert (5,4) in targets          #sidle up to enemy pawn
    assert (5,3) in targets          #can capture enemy pawn
    assert (5,2) not in targets      #can't move past enemy pawn


def test_rook_stops_at_the_edge_of_the_board():
    rook = Piece(kind="rook", side="player")
    targets = legal_targets(rook, (5,5), DIAMOND, {(5,5): rook})
    assert (0,5) in targets          #far left point of diamond
    assert (5,0) in targets          #top of diamond
    assert len(targets) == 20         #5 squares in each direction, minus the square the rook is on


def test_bishop_moves_diagonally_only():
    bishop = Piece(kind="bishop", side="player")
    targets = legal_targets(bishop, (5,5), DIAMOND, {(5,5): bishop})
    assert (4,4) in targets          #down left
    assert (6,6) in targets          #up right
    assert (4,6) in targets          #up left
    assert (6,4) in targets          #down right
    assert (5,6) not in targets          #can't move straight up
    assert (5,4) not in targets          #can't move straight down
    assert (4,5) not in targets          #can't move straight left
    assert (6,5) not in targets          #can't move straight right


def test_knight_moves_in_an_L_shape():
    knight = Piece(kind="knight", side="player")
    targets = legal_targets(knight, (5,5), DIAMOND, {(5,5): knight})
    assert (4,3) in targets          #down left
    assert (6,3) in targets          #down right
    assert (3,4) in targets          #left down
    assert (7,4) in targets          #right down
    assert (3,6) in targets          #left up
    assert (7,6) in targets          #right up
    assert (4,7) in targets          #up left
    assert (6,7) in targets          #up right
    assert len(targets) == 8         #8 possible L-shaped moves


def test_king_moves_one_square_in_any_direction():
    king = Piece(kind="king", side="player")
    targets = legal_targets(king, (5,5), DIAMOND, {(5,5): king})
    assert (4,4) in targets          #down left
    assert (5,4) in targets          #down
    assert (6,4) in targets          #down right
    assert (4,5) in targets          #left
    assert (6,5) in targets          #right
    assert (4,6) in targets          #up left
    assert (5,6) in targets          #up
    assert (6,6) in targets          #up right
    assert len(targets) == 8         #8 possible moves


def test_a_king_on_the_point_of_the_diamond_has_three_squares_to_move_to():
    king = Piece(kind="king", side="player")
    targets = legal_targets(king, (5,10), DIAMOND, {(5,10): king})
    assert set(targets) == {(4,9), (5,9), (6,9)}
