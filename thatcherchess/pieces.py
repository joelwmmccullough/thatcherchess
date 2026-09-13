"""
    defines pieces and where they can move
    movegen is pseudolegal, meaning it confirm whether king is left in check
"""

from dataclasses import dataclass

from thatcherchess.board import Cell, Shape

Occupancy = dict[Cell, "Piece"]

ROOK_DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]
BISHOP_DIRECTIONS = [(1,1), (1,-1), (-1,1), (-1,-1)]
QUEEN_DIRECTIONS = ROOK_DIRECTIONS + BISHOP_DIRECTIONS
KNIGHT_OFFSETS = [(1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1), (-2,1), (-1,2)]
KING_OFFSETS = QUEEN_DIRECTIONS


@dataclass
class Piece: 
    #one chess piece

    kind: str
    side: str


def _slide(
    cell: Cell, shape: Shape, occupancy: Occupancy, side: str,
    directions: list[tuple[int,int]],
) -> list[Cell]:

    #targets for a piece that slides along 'directions' til blocked
    targets: list[Cell] = []
    col, row = cell
    for dcol, drow in directions:
        c, r = col, row
        while True:
            c, r = c + dcol, r + drow
            if not shape.in_bounds((c,r)):
                break
            occupant = occupancy.get((c,r))
            if occupant is None:
                targets.append((c,r))
                continue
            if occupant.side != side:
                targets.append((c,r))
            break
    return targets


def _steps(
    cell: Cell, shape: Shape, occupancy: Occupancy, side: str, offsets: list[tuple[int,int]]
) -> list[Cell]:
    #Targets for a piece that makes a fixed jump

    targets: list[Cell] = []
    col,row = cell
    for dcol, drow in offsets:
        candidate = (col + dcol, row + drow)
        if not shape.in_bounds(candidate):
            continue
        occupant = occupancy.get(candidate)
        if occupant is None or occupant.side != side:
            targets.append(candidate)
    return targets


def legal_targets(
    piece: Piece, cell: Cell, shape: Shape, occupancy: Occupancy
) -> list[Cell]:
    #returns all legal targets for a piece at a cell
    if piece.kind == "rook":
        return _slide(cell, shape, occupancy, piece.side, ROOK_DIRECTIONS)
    elif piece.kind == "bishop":
        return _slide(cell, shape, occupancy, piece.side, BISHOP_DIRECTIONS)
    elif piece.kind == "queen":
        return _slide(cell, shape, occupancy, piece.side, QUEEN_DIRECTIONS)
    elif piece.kind == "knight":
        return _steps(cell, shape, occupancy, piece.side, KNIGHT_OFFSETS)
    elif piece.kind == "king":
        return _steps(cell, shape, occupancy, piece.side, KING_OFFSETS)
    else:
        raise ValueError(f"unknown kind {piece.kind}")

