"""
    renders the chessboard in ASCII. will not be used in final product
"""

from thatcherchess.board import GRID_SIZE, Cell, Shape
from thatcherchess.pieces import Piece, Occupancy


LETTERS = {
    "king": "k",
    "queen": "q",
    "rook": "r",
    "bishop": "b",
    "knight": "n",
    "pawn": "p"
}


def _code(piece: Piece | None, is_target: bool) -> str:
    # returns a two-character code for each piece. 
    # CAPS IS PLAYER, lowercase is thatcher.
    # . is empty
    # * is a valid target square
    
    if piece is None:
        return " *" if is_target else " ."
    letter = LETTERS[piece.kind]
    if piece.side == "player":
        letter = letter.upper()
    return f"x{letter}" if is_target else f" {letter}"


def start_position(shape: Shape) -> Occupancy:
    # Both armies in their starting squares, as cell -> Piece
    pieces: Occupancy = {}
    for start in shape.thatcher_start:
        pieces[(start.col, start.row)] = Piece(kind=start.kind, side="thatcher")
    for start in shape.player_start:
        pieces[(start.col, start.row)] = Piece(kind=start.kind, side="player")
    return pieces


def render_board(shape: Shape, pieces: Occupancy, targets: list[Cell] | None = None) -> str:
    #returns a string of the board in ASCII

    marked = set(targets or [])
    header = "    " + " ".join(f"{col:>2}" for col in range(GRID_SIZE))
    lines = [header]
    for row in range(GRID_SIZE):
        squares = []
        for col in range(GRID_SIZE):
            cell = (col,row)
            if cell not in shape.cells:
                squares.append("  ")
            else:
                squares.append(_code(pieces.get(cell), cell in marked))
        lines.append(f"{row:>2}  " + " ".join(squares))
    return "\n".join(lines)


if __name__ == "__main__":
    from thatcherchess.board import diamond
    from thatcherchess.pieces import legal_targets

    shape = diamond()
    pieces = start_position(shape)
    rook = Piece(kind = "rook", side = "player")
    pieces[(5,5)] = rook
    print(render_board(shape,pieces,legal_targets(rook,(5,5), shape, pieces)))

