####################################################################################################
#  Program name:        DougBot   <dougbot.py>                                                     #
#  Version:             v1.0                                                                       #
#  Code last modified:  10 Apr 19                                                                  #
#                                                                                                  #
#  Description:         An amateur tic-tac-toe agent, written as part of the ANU 3Ai CECS 8001     #
#                       Laboratory (Week 6, Block I). I was absent for this class due to illness;  #
#                       this is my attempt whilst physically dislocated! DougBot plays as an X,    #
#                       whilst its opponent plays as an O. This code includes portions written by  #
#                       Zac Hatfield-Dodds, and was initially based on his <_template.py> program  #
#                       (annotated in here as appropriate). DougBot is pitted against other agents #
#                       by Zac's <ttt.py> program.                                                 #
#                                                                                                  #
#                       DougBot takes a board state (represented as a string), and returns a new   #
#                       board state, with its move (i.e. an additional X).                         #
#                                                                                                  #
#  Author:              Stephen J. Fry                                                             #
#                       stephen.fry(at)anu.edu.au                                                  #
####################################################################################################

import random

# Zac's code for creating the possible ways of winning (three up, down, or diagonally); WINS is a tuple.
WINS = (
    (0, 1, 2),  # top row
    (3, 4, 5),  # centre row
    (6, 7, 8),  # bottom row
    (0, 3, 6),  # left-most column
    (1, 4, 7),  # centre column
    (2, 5, 8),  # right-most column
    (0, 4, 8),  # backward diagonal
    (2, 4, 6),  # forward diagonal
)


def dougbot(board: str) -> str:

    possiblemoves = [
        board[:i] + "X" + board[i + 1 :]
        for i, space in enumerate(board)
        if space == "."
    ]  # From Zac's example; generate all boards that could be made by the next move
    opponentmoves = [
        board[:i] + "O" + board[i + 1 :]
        for i, space in enumerate(board)
        if space == "."
    ]  # Generate all boards that the opponent could make with their next move.

    for m in possiblemoves:
        # From Zac's example; for each possible way to win (row/column/diagonal)
        for a, b, c in WINS:  # if we (X) have won,
            if m[a] == m[b] == m[c] == "X":
                return m  # make that move.

    for n in opponentmoves:
        # From Zac's example; for each possible way to lose (row/column/diagonal)
        for a, b, c in WINS:  # if our opponent (O) has won,
            if n[a] == n[b] == n[c] == "O":
                for move in range(9):
                    if n[move] != board[move]:
                        return n[:move] + "X" + n[move + 1 :]  # block their win.

    if board.count(".") == 9:  # Check if we are going first
        # print("We get to go first... the odds are in our favour!")
        om = random.choice(
            [0, 2, 6, 8]
        )  # Randomly selects a corner position to play the opening move (om) in.
        return board[:om] + "X" + board[om + 1 :]

    if board.count(".") == 7:  # Check if it's our second turn
        # Artificially recreates the randomised om variable by looking it up, and then converting it from a list to an integer (via a string)
        om = int("".join(str(i) for i, char in enumerate(board) if char == "X"))
        # If they have taken the centre position
        if [pos for pos, char in enumerate(board) if char == "O"] == [4]:
            # if board[4] == "O":  # Another way I could have performed the centre position check
            # Create a list for lookup to enable an opposite corner play. I couldn't use reverse because my original list omitted the centre.
            cubes = [8, 6, 4, 2, 0]
            # Make my move (mm) in the opposite corner to where I played my opening move (om).
            mm = cubes[om // 2]
        elif (
            [pos for pos, char in enumerate(board) if char == "O"] == [1]
            or [pos for pos, char in enumerate(board) if char == "O"] == [3]
            or [pos for pos, char in enumerate(board) if char == "O"] == [5]
            or [pos for pos, char in enumerate(board) if char == "O"] == [7]
        ):  # If they have taken an edge position.
            # board[1] == "O" or board[3] == "O" or board[5] == "O" or board[7] == "O":  # A better (shorter) way to perform the check.
            mm = 4  # Play in the centre position.
        else:  # If they have taken a corner position instead of the centre or an edge position.
            mm = 4  # Play in the centre position.
        return board[:mm] + "X" + board[mm + 1 :]

    if board.count(".") == 8:  # Check if we are going second.
        # print("You've gone first... it's going to be close!")
        if board[4] == ".":  # check if the centre is open/legal - if so,
            cm = 4  # make my countermove (cm) in the centre position
        cm = random.choice([0, 2, 6, 8])
        # Otherwise, randomly selects a corner position to play my countermove (cm) in.
        return board[:cm] + "X" + board[cm + 1 :]

    if board.count(".") == 6:  # Check if it's our second turn.
        cm = int(
            "".join(
                [str(i) for i in [pos for pos, char in enumerate(board) if char == "X"]]
            )
        )  # Artificially recreates the randomised cm variable by looking it up, and then converting it from a list to an integer (via a string).
        edges = [1, 3, 5, 7]  # Create a list for lookup to enable an edge play.
        openslots = [pos for pos, char in enumerate(board) if char == "."]
        # Finds open slots (i.e. legal moves).
        if cm == 4:
            mm = random.choice([elem for elem in edges if elem in openslots])
            # Randomly selects an available edge position to play my move (mm) in.
        elif cm == 0:
            mm = random.choice([1, 3])
            # Randomly selects an adjacent (to the corner I played in my countermove (cm)) edge position to play my move in.
        elif cm == 2:
            mm = random.choice([1, 5])
            # Randomly selects an adjacent edge position to play my move in.
        elif cm == 6:
            mm = random.choice([3, 7])
            # Randomly selects an adjacent edge position to play my move in.
        elif cm == 8:
            mm = random.choice([5, 7])
            # Randomly selects an adjacent edge position to play my move in.
        return board[:mm] + "X" + board[mm + 1 :]

    else:

        return random.choice(possiblemoves)
        # From Zac's example; if all else fails with the aforementioned code/strategy, play a random (legal) move.
