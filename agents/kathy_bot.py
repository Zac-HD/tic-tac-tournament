"""
kathy bot
A tic tac toe bot

Greetings, Professor Falken. Do you want to play a game?
"""

import random
import operator

"""
Define the winning sequences on the board
"""
# Groups of three spaces where an agent wins if they have played in
# all three spaces.  Three rows, three columns, two diagonals.
# Here's the board:
#       0 1 2
#       3 4 5
#       6 7 8
WINS = (
    (0, 1, 2),  # top row
    (3, 4, 5),  # middle row
    (6, 7, 8),  # bottom row
    (0, 3, 6),  # left column
    (1, 4, 7),  # middle column
    (2, 5, 8),  # right column
    (0, 4, 8),  # top left to bottom right diagonal
    (2, 4, 6),  # top right to bottom left diagonal
)

"""
Assign 'weights' to each square
"""
# Each square has a different weight depending on the frequency
# with which it appears in the winning sequences
# Here's the board:
#       0 1 2 | 3 2 3
#       3 4 5 | 2 4 2
#       6 7 8 | 3 2 3
WEIGHTS = (3, 2, 3, 2, 4, 2, 3, 2, 3)


def kathy_first(board:str) -> str:
    """
    Play the first move by selecting the square with the highest weight
    I've attempted to generalise this function -
    - not just 'choose the centre' but 'choose the centre because it's
      weighted the highest
    What bothers me here is that the `index` and `value` in a 9-grid
    square that begins at 0 are both 4 - so it's hard to distinguish.
    """
    print ('now playing first move ...')
    # Determine the square with the max weight, makes it widely applicable
    index, value = max(enumerate(WEIGHTS), key=operator.itemgetter(1))
    return board.replace(".", "X", index)

def kathy_highest_value_square(board: str) -> str:
    """What I want to do here is pick the highest WEIGHT available square"""
    # This uses a "list comprehension", which is nice and concise.  See also
    # http://greenteapress.com/thinkpython2/html/thinkpython2020.html#sec224
    print ('now calculating highest available value square ...')
    allowed_positions = [i for i, space in enumerate(board) if space == "."]
    allowed_weights = []
    for m in allowed_positions :
        allowed_weights.append(WEIGHTS[m])
    # @TODO max(enumerate) will return a single number.
    # Sometimes there will be multiple highest numbers.
    # Need to find a way to return them all and select from them
    # but I don't know enough Python to do that
    index, value = max(enumerate(allowed_weights), key=operator.itemgetter(1))
    return board.replace(".", "X", index)

def kathy_bot(board: str) -> str:
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
    """Make the first winning move available.
    If there are no winning moves, make a random valid move.

    Extending this to multiple moves and trying to avoid losing
    (instead of trying to win) is a common but reliable strategy.
    """

    # This borrows from Zac's example
    # Generate all boards that could be made by a random_move
    possible_moves = [
        board[:i] + "X" + board[i + 1 :]
        for i, space in enumerate(board)
        if space == "."
    ]

    # This is the Offensive strategy - if we can win, let's win
    # For each resulting board,
    for m in possible_moves:
        # For each possible way to win (row, column, or diagonal)
        for a, b, c in WINS:
            # If we (X) have won,
            if m[a] == m[b] == m[c] == "X":
                # make that move!
                print (m)
                return m

    # This is the Defensive strategy - if we are going to lose, don't
    # Check to see whether we need to "block" a move where an opponent has
    # two of the three squares needed to have all three squares in a winning
    # sequence
    for m in possible_moves:
        for d, e, f in WINS:
            if m[d] == 'X' and m[e] == 'X':
                print ('f is: ', f)
                print (m)
                return m
            elif m[d] == 'X' and m[f] == 'X':
                print (m)
                return m
                print ('e is: ', e)
            elif m[e] == 'X' and m[f] == 'X':
                print (m)
                return m
                print ('d is: ', d)

    # If we haven't returned anything yet, then we weren't going to win,
    # and we weren't going to lose. Choose the highest value square.
    return kathy_highest_value_square(board)
