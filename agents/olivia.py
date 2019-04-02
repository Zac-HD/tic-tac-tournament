"""
A template for developing tic-tac-toe agents.
"""
import random

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


def olivia(board: str) -> str:
    """The agent function takes a board state, represented as a string,
    and must return a new board state with an additional move for X.

    (the engine will swap Xs for Os between each agent, so you don't have
    to track which the agent is playing - it's always X)

    The board is always a nine-character string consisting of "X", "O",
    and ".", with at least one "." indicating an empty space.  For example,
    "XO.OX.O.." represents the following board:

        X O .
        O X .
        O . .

    and X could win by moving in the lower-right space, i.e. returning
    "XO.OX.O.X".  Make sense?
    """

    # start of an imperfect and super inefficniet brute force approach...

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
                # Otherwise make a blocking  move.

    possible_movesO = [
        board[:i] + "O" + board[i + 1 :]
        for i, space in enumerate(board)
        if space == "."
    ]

    # For each resulting board,
    for n in possible_movesO:
        # For each possible way to lose (row, column, or diagonal)
        for a, b, c in WINS:
            # If we (O) have lost,
            if n[a] == n[b] == n[c] == "O":

                for move in range(9):
                    if n[move] != board[move]:
                        # make that move!
                        return n[:move] + "X" + n[move + 1 :]

    if board[4] == ".":  # is centre spot is empty?
        return board[:4] + "X" + board[4 + 1 :]  # yes? put X in centre spot (4)...

        # no? put X in first available corner (0,2,6,8)...
    if board[0] == ".":
        return board[:0] + "X" + board[0 + 1 :]

    if board[2] == ".":
        return board[:2] + "X" + board[2 + 1 :]

    if board[6] == ".":
        return board[:6] + "X" + board[6 + 1 :]

    if board[8] == ".":
        return board[:8] + "X" + board[8 + 1 :]

    else:  # check for a winning or blocking move and do that, or do a random move...

        # Generate all boards that could be made by a random_move
        possible_moves = [
            board[:i] + "X" + board[i + 1 :]
            for i, space in enumerate(board)
            if space == "."
        ]

        # Otherwise make a random  move.

        return random.choice(possible_moves)
