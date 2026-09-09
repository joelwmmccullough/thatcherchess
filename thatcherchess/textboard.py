"""
    renders the chessboard in ASCII. will not be used in final product
"""

from thatcherchess.board import GRID_SIZE, Cell, Shape

LETTERS = {
    "king": "k",
    "queen": "q",
    "rook": "r",
    "bishop": "b",
    "knight": "n",
    "pawn": "p"
}

def _code(kind: str, side: str) -> str:
    #returns a two-character code for each piece. CAPS IS PLAYER, lowercase is thatcher.
    letter = LETTERS[kind]
    return f" {letter.upper()}" if side == "player" else f" {letter}"


def start_codes(shape: Shape) -> dict[Cell, str]:
    #returns a dict of cell->code for all starting pieces
    codes: dict[Cell, str] = {}
    for piece in shape.player_start:
        codes[(piece.col, piece.row)] = _code(piece.kind, "player")
    for piece in shape.thatcher_start:
        codes[(piece.col, piece.row)] = _code(piece.kind, "thatcher")
    return codes


def render_board(shape: Shape) -> str:
    #returns a string of the board in ASCII
    codes = start_codes(shape)
    header = "    " + " ".join(f"{col:2}" for col in range(GRID_SIZE))
    lines = [header]
    for row in range(GRID_SIZE):
        squares = []
        for col in range(GRID_SIZE):
            if (col,row) not in shape.cells:
                squares.append("  ")
            else: 
                squares.append(codes.get((col,row), " ."))
        lines.append(f"{row:>2}   " + " ".join(squares))
    return "\n".join(lines)

if __name__ == "__main__":
    from thatcherchess.board import diamond
    print(render_board(diamond())) 
 