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


def weighted_moves(board: str) -> str:
    # Initialise the board with the corners more heavily weighted.
    # corners = [0, 2, 6, 8]
    board_weights = {i: 1 for i in range(9)}
    # for i in corners:
    #   board_weights[i] += 1

    # Cross out the squares that have had counters placed in them.
    for a in range(9):
        if board[a] == "X" or board[a] == "O":
            board_weights[a] = 0

    # Adjust the board weightings to stop any potential wins.
    board_weights = block_wins(board, board_weights)
    board_weights = winning_positions(board, board_weights)

    # Make a random choice from the list of best options.
    inverse = [(value, key) for key, value in board_weights.items()]
    maxValue = max(inverse)[0]
    best_moves = [key for key in board_weights.keys() if board_weights[key] == maxValue]
    move = random.choice(best_moves)
    return board[:move] + "X" + board[move + 1 :]


def block_wins(board: str, board_weights) -> str:
    # Idenitfy the indexes of all the possible moves.
    spaces = [pos for pos, char in enumerate(board) if char == "."]
    # Create the future boards for all the possible moves (if the opposition were to move).
    possible_moves = [
        board[:i] + "O" + board[i + 1 :]
        for i, space in enumerate(board)
        if space == "."
    ]

    # Identify immediate losing boards in possible moves
    for m in possible_moves:
        # For each possible way to win (row, column, or diagonal)
        for a, b, c in WINS:
            # If we (X) have won,
            if m[a] == m[b] == m[c] == "O":
                losing_spot = spaces[possible_moves.index(m)]
                board_weights[losing_spot] += 6
    return board_weights


def winning_positions(board: str, board_weights) -> str:
    # Idenitfy the indexes of all the possible moves.
    spaces = [pos for pos, char in enumerate(board) if char == "."]
    # Create the future boards for all the possible moves (if we were to move).
    possible_moves = [
        board[:i] + "X" + board[i + 1 :]
        for i, space in enumerate(board)
        if space == "."
    ]
    # Identify winnable positions
    for m in possible_moves:
        # For each possible way to win (row, column, or diagonal)
        for a, b, c in WINS:
            # If we (X) have won,
            if m[a] == m[b] == m[c] == "X":
                losing_spot = spaces[possible_moves.index(m)]
                board_weights[
                    losing_spot
                ] += 10  # This indicates that you should definitely do this move.

            # Identify the positions that will set us up to be winnable next time. Count how many of these exist for each position.
            if m[a] == m[b] == "X" and m[c] == ".":
                winning_spot = spaces[possible_moves.index(m)]
                board_weights[winning_spot] += 1

            if m[b] == m[c] == "X" and m[a] == ".":
                winning_spot = spaces[possible_moves.index(m)]
                board_weights[winning_spot] += 1

            if m[a] == m[c] == "X" and m[b] == ".":
                winning_spot = spaces[possible_moves.index(m)]
                board_weights[winning_spot] += 1

    return board_weights


# print(winning_positions("X...O....",{0:0,1:1,2:2,3:1,4:0,5:1,6:2,7:1,8:2}))
