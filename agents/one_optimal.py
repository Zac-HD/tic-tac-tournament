import random

AUTHOR = "Easy Win"

# Groups of three spaces where an agent wins if they have played in
# all three spaces.  Three rows, three columns, two diagonals.
WINS = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


def agent(board: str) -> str:
    """Make the first winning move available.
    If there are no winning moves, make a random valid move.
    """
    possible_moves = [
        board[:i] + "X" + board[i + 1 :]
        for i, space in enumerate(board)
        if space == "."
    ]
    for m in possible_moves:
        for a, b, c in WINS:
            if m[a] == m[b] == m[c] == "X":
                return m
    return random.choice(possible_moves)
