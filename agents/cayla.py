"""
Noughts and Crosses: creating an algorithm for Cayla the doll
(who plays noughts and crosses...to win!)

The grid
Q. How to define the grid: ‘corner, side, centre’ or integer (1-9) approach?
A. Observations of Cayla’s game strategy over 12 successive games
  * Cayla has a strong preference for opening with the bottom left hand corner of the
    grid (if this square is available) regardless of whether she moves first or second
  * Where the human player moves first and selects the bottom left hand corner, Cayla’s
    opening gambit is to move to the centre space
  * Thereafter, Cayla moves to block the human player and if possible win the game, or
    failing that draw the game
    - In one game out of the first ten played, Cayla opted to let the human player win
      (made an illogical random move)
  * Cayla also comments on the moves of the human player
    - ‘Nice move’; ‘Are you sure about that one?’; ‘I think I have a chance to win’.
B. Two players: let player A = human (0); let player B = computer (X)
C. Suggested AI algorithm:
  1. Determine who goes first. (Cayla alternated: she always allowed the human
     player to go first for the first game played, then moved first for the
     subsequent game played. Then allowed the human player to go first for the
     following game, and so on.)
  2. For Cayla’s first move, check if bottom left corner is free and if so move there.
  3. If the bottom left corner is not free, check if the centre is free and move there.
  4. For subsequent moves, if there is a move the human player could make to
     win the game (occupy a row of three squares either horizontally, vertically or
     diagonally), play a blocking move (move to that space). Before making the
     move, state (print) ‘Nice move’.
  5. If there is a move the computer could make to win the game, play that
     move. Before making the move, state (print) ‘I think I have a chance to win’.
  6. Otherwise:
     a) if the human player moves to a top or bottom corner space, move to the
        corresponding bottom or top corner space in the same row if free; if not,
        move to the side space in the same row
     b) if the human player moves to the top or bottom side space in the middle
        row, move to the corresponding bottom or top space in the same row if free;
        if not, move to the centre if free; if not, check what other spaces are free and
        move to one of these
     c) if the human player moves to the right hand side row middle space,
        move to the middle space in the left hand side row if free; if not, move to the
        centre. If the centre is not free, check what other spaces are free and move
        to one of these
     d) if the human player moves to the left hand side row middle space, move
        to the middle space in the right hand side row if free; if not, move to the
        centre. If the centre is not free, check what other spaces are free and move
        to one of these.
PMM
"""

import collections
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


def maybe_say(message: str) -> None:
    # print(message)  # un-comment this for verbose output
    return None


def move(board: str, place: int) -> str:
    return board[:place] + "X" + board[place + 1 :]


def cayla_strategy(board: str) -> str:
    """Translated into Python by Zac."""
    possible_moves = [move(board, i) for i, space in enumerate(board) if space == "."]
    # Step 1: determine who goes first (done by the engine)
    # Step 2: on first move, go bottom-left if possible.
    if len(possible_moves) >= 8:
        if board[6] == ".":
            return move(board, 6)
        # Step 3: on first move, otherwise go in center
        return move(board, 4)
    # Step 4: for subsequent moves, stop human from winning:
    for m in possible_moves:
        for a, b, c in WINS:
            if m[a] == m[b] == "O" or m[a] == m[c] == "O" or m[b] == m[c] == "O":
                maybe_say("Nice move.")
                return m

    # Step 5: win if possible this move
    for m in possible_moves:
        for a, b, c in WINS:
            if m[a] == m[b] == m[c] == "X":
                maybe_say("I think I have a chance to win")
                return m

    # Step 6: here, we have to diverge a little - because we only
    # know what's on the board, not what move our opponent made.
    # We'll try to guess.

    # Step 6a: if O is in a top (bottom) corner, and X is not in
    # that row at all, move in the other top (bottom) corner if
    # possible and in the center of that row otherwise.
    if "X" not in board[:3]:  # x not in top row
        if board[:3] == "O.O":
            return move(board, 1)
        if board[0] == "O":
            return move(board, 2)
        if board[2] == "O":
            return move(board, 0)
    if "X" not in board[6:]:  # x not in bottom row
        if board[6:] == "O.O":
            return move(board, 7)
        if board[6] == "O":
            return move(board, 8)
        if board[8] == "O":
            return move(board, 6)

    # Step 6b: if O is in top-center move in bottom-center if free,
    # else move to center, or go to 6c, and vice-versa.
    if board[1] == "O":
        if board[7] == ".":
            return move(board, 7)
        if board[4] == ".":
            return move(board, 4)
    if board[7] == "O":
        if board[1] == ".":
            return move(board, 1)
        if board[4] == ".":
            return move(board, 4)

    # Step 6c and 6d: as for 6b, but for the middle row instead of the middle column.
    if board[3] == "O":
        if board[5] == ".":
            return move(board, 5)
        if board[4] == ".":
            return move(board, 4)
    if board[5] == "O":
        if board[3] == ".":
            return move(board, 3)
        if board[4] == ".":
            return move(board, 4)

    # Finally, make a random move if not specified.
    return random.choice(possible_moves)

