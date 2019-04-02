#!/usr/bin/env python
# coding: utf-8

# copy everything below for my actual agent upload.

import random


def gb_tacky_toes(board: str) -> str:
    # Generate all boards that could be made by a random_move.
    # we are indexing elements in the board. moving through the board string,
    # looking for spaces that are empty. If the space is empty make that space an X.

    possible_winning_moves = [
        board[:i] + "X" + board[i + 1 :]
        for (i, space) in enumerate(board)
        # enumerate creates a list from the a string.
        if space == "."
    ]

    possible_losing_moves = [
        board[:i] + "O" + board[i + 1 :]
        for (i, space) in enumerate(board)
        # enumerate creates a list from the a string.
        if space == "."
    ]

    # We need to define what winning moves are -- here we are listing the wins, horizontally,
    # then vertically, then diagonally.

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

    # PART ONE: LOOK FOR WINNING MOVE

    for m in possible_winning_moves:
        # For each possible way to win (row, column, or diagonal)
        for a, b, c in WINS:
            # If we (X) have won,
            if m[a] == m[b] == m[c] == "X":
                # make that move!
                return m

    # PART TWO: LOOK FOR AN IMMINENT LOSS

    for n in possible_losing_moves:
        for a, b, c in WINS:
            if n[a] == n[b] == n[c] == "O":
                for move in range(9):
                    if n[move] != board[move]:
                        return n[:move] + "X" + n[move + 1 :]

    # PART THREE:

    # Introducing some basic heuristics for specific situations

    # Board is blank, go in the centre square
    if board == ".........":
        return "....X...."

    # You go centre first, opponent plays an edge - go in for the kill
    if board == ".O..X....":
        return ".O..X.X.."

    if board == "....XO...":
        return "X...XO..."

    if board == "....X..O.":
        return "X...X..O."

    if board == "...OX....":
        return "...OX...X"

    # You go centre first, opponent plays a corner -- try to trap

    if board == "O...X....":
        return "O...X...X"

    if board == "..O.X....":
        return "..O.X.X.."

    if board == "....X...O":
        return "X...X...O"

    if board == "....X.O..":
        return "..X.X.O.."

    # if you go centre first, and the trap is successful
    if board == "O...X..OX":
        return "O.X.X..OX"

    if board == "O...XO..X":
        return "O...XOX.X"

    if board == "..OOX.X..":
        return "..OOX.X.X"

    if board == "..O.X.XO.":
        return "X.O.X.XO."

    if board == "XO..X...O":
        return "XO..X.X.O"

    if board == "X..OX...O":
        return "X.XOX...O"

    if board == "..X.XOO..":
        return "X.X.XOO.."

    if board == ".OX.X.O..":
        return ".OX.X.O.X"

    # Opponent goes first, and they go in the center

    if board == "....O....":
        return "....O...X"

    # Opponent goes first, plays center, and then plays far corner

    if board == "O...O...X":
        return "O.X.O...X"

    if board == "X...O...O":
        return "X...O.X.O"

    if board == "..X.O.O..":
        return "..X.O.O.X"

    if board == "..O.O.X..":
        return "..O.O.X.X"

    # Opponent goes first, plays a corner -- make sure to move center

    if board == "O........":
        return "O...X...."

    if board == "........O":
        return "....X...O"

    if board == "..O......":
        return "..O.X...."

    if board == "......O..":
        return "....X.O.."

    # Opponent goes first, plays a corner, then goes for the squeeze, by going opposite corner

    if board == "O...X...O":
        return "O...X..XO"

    if board == "..O.X.O..":
        return ".XO.X.O.."

    # LAST RESORT
    # Otherwise make a random move.

    if board[4] == ".":
        return board[:4] + "X" + board[4 + 1 :]

    if board[8] == ".":
        return board[:8] + "X"

    if board[6] == ".":
        return board[:6] + "X" + board[6 + 1 :]

    if board[2] == ".":
        return board[:2] + "X" + board[2 + 1 :]

    if board[0] == ".":
        return "X" + board[0 + 1 :]

    return random.choice(possible_winning_moves)
