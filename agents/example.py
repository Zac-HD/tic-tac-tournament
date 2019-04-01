"""
Two example tic-tac-toe agents, by Zac.

Neither are optimal, but I hope that they illustrate some ways
that you can implement a game-playing algorithm ("AI").
"""

import random


def random_move(board: str) -> str:
    """Make a random valid move."""
    # This uses a "list comprehension", which is nice and concise.  See also
    # http://greenteapress.com/thinkpython2/html/thinkpython2020.html#sec224
    allowed_positions = [i for i, space in enumerate(board) if space == "."]
    move = random.choice(allowed_positions)
    return board[:move] + "X" + board[move + 1 :]


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


def win_next_move_else_random(board: str) -> str:
    """Make the first winning move available.
    If there are no winning moves, make a random valid move.

    Extending this to multiple moves and trying to avoid losing
    (instead of trying to win) is a common but reliable strategy.
    """
    # Generate all boards that could be made by a random_move
    possible_moves = [
        board[:i] + "X" + board[i + 1 :]
        for i, space in enumerate(board)
        if space == "."
    ]
    # For each resulting board,
    for m in possible_moves:
        # For each possible way to win (row, column, or diagonal)
        for a, b, c in WINS:
            # If we (X) have won,
            if m[a] == m[b] == m[c] == "X":
                # make that move!
                return m
    # Otherwise make a random move.
    return random.choice(possible_moves)
