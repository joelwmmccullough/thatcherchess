"""
    thatcherchess uses a diamond board. 
    this file defines and builds that board.
    confused? don't worry about it
"""

from dataclasses import dataclass, field

GRID_SIZE = 11

ORTHOGONAL_STEPS = [(1,0),(-1,0),(0,1),(0,-1)]

Cell = tuple[int,int]

@dataclass
class StartPiece:
    #defines a chess piece and its starting location
    kind: str
    col: int
    row: int

@dataclass
class Shape:
    #board type. i said there are only diamonds in the intro but there might be more

    id: str
    name: str
    cells: set[Cell]
    player_start: list[StartPiece] = field(default_factory=list)
    thatcher_start: list[StartPiece] = field(default_factory=list)

    def in_bounds(self,cell: Cell) -> bool:
        #true if cell is in the board shape
        return cell in self.cells

#initial definition of both armies

PLAYER_START: list[tuple[str,int,int]] = [
    ("king", 5, 10), 
    ("rook", 4, 9), ("queen", 5, 9), ("rook", 6, 9), 
    ("knight", 3, 8), ("bishop", 4, 8), ("bishop", 6, 8), ("knight", 7, 8),
    ("pawn", 2, 7), ("pawn", 3, 7), ("pawn", 4, 7), ("pawn", 5, 7),
    ("pawn", 6, 7), ("pawn", 7, 7), ("pawn", 8, 7)
]

THATCHER_START: list[tuple[str,int,int]] = [
    ("king", 5, 0), 
    ("rook", 4, 1), ("queen", 5, 1), ("rook", 6, 1), 
    ("knight", 3, 2), ("bishop", 4, 2), ("bishop", 6, 2), ("knight", 7, 2),
    ("pawn", 2, 3), ("pawn", 3, 3), ("pawn", 4, 3), ("pawn", 5, 3),
    ("pawn", 6, 3), ("pawn", 7, 3), ("pawn", 8, 3)
]

def diamond_cells() -> set[Cell]:
    #returns a set of all the cells in a diamond shape
    #every cell of the 11x11 grid within 5 steps of center

    return {
        (col, row)
        for col in range(GRID_SIZE)
        for row in range(GRID_SIZE)
        if abs(col - 5) + abs(row - 5) <= 5
    }

def diamond() -> Shape:
    #returns a diamond shape with the starting pieces defined above

    return Shape(
        id="diamond",
        name="The Diamond",
        cells=diamond_cells(),
        player_start=[StartPiece(kind, col, row) for kind, col, row in PLAYER_START],
        thatcher_start=[StartPiece(kind, col, row) for kind, col, row in THATCHER_START]
    )



def is_connected(cells: set[Cell]) -> bool: 
    #FLOOD FILL BABY YEAHHHH

    if not cells: 
        return False
    
    start = next(iter(cells))
    seen = {start}
    frontier = [start]

    while frontier: 
        col, row = frontier.pop()
        for dcol, drow in ORTHOGONAL_STEPS:
            neighbor = (col + dcol, row + drow)
            if neighbor in cells and neighbor not in seen: 
                seen.add(neighbor)
                frontier.append(neighbor)
    return len(seen) == len(cells)
