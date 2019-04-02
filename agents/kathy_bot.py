"""
kathy bot
A tic tac toe bot

This is an attempt to deduce a tic tac toe algorithm
without having to look it up on Google.
It's probably rudimentary, but is a genuine attempt.

Insert lots of swearing here about strings in Python
and how they're immutable :X

"""

import operator


def print(*args):
    """Delete this function out to un-silence output."""
    pass


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

iterations = 0


def kathy_first(board: str) -> str:
    """
    Play the first move by selecting the square with the highest weight
    I've attempted to generalise this function -
    - not just 'choose the centre' but 'choose the centre because it's
      weighted the highest
    What bothers me here is that the `index` and `value` in a 9-grid
    square that begins at 0 are both 4 - so it's hard to distinguish.
    """
    # Determine the square with the max weight, makes it widely applicable
    index, value = max(enumerate(WEIGHTS), key=operator.itemgetter(1))
    print("now returning the first square with the highest weight: ", index)
    # turn the string into a list because string manipulation
    # in Python is immutable and FFS I wish I had grokked this 5 hours ago
    # but that's what alcohol is for, right? :(
    boardlist = list(board)
    boardlist[index] = "X"
    board = "".join(boardlist)
    print("current state of board is: ", board)
    return board


def kathy_highest_value_square(board: str) -> str:
    """What I want to do here is pick the highest WEIGHT available square"""
    # This uses a "list comprehension", which is nice and concise.  See also
    # http://greenteapress.com/thinkpython2/html/thinkpython2020.html#sec224
    print("now calculating highest available value square ...")
    allowed_positions = [i for i, space in enumerate(board) if space == "."]
    allowed_weights = []
    for m in allowed_positions:
        allowed_weights.append(WEIGHTS[m])
    # @TODO max(enumerate) will return a single number.
    # Sometimes there will be multiple highest numbers.
    # Need to find a way to return them all and select from them
    # but I don't know enough Python to do that
    index, value = max(enumerate(allowed_weights), key=operator.itemgetter(1))
    boardlist = list(board)
    boardlist[index] = "X"
    board = "".join(boardlist)
    print("current state of board is: ", board)
    return board


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

    print("\n" + "=================== beginning iteration ====================")
    # This is a recursive function, so this tells us what the current state
    # of the `board` string is. len() is a validation criterion, check that too
    print("current state of board is: ", board)
    print("length of string of board is: ", len(board))
    print("the number of unoccupied squares on the board is : ", board.count("."))

    # This is the base case for recursion - there are no more unoccupied squares
    # on the grid. The game has either won, lost or been drawn.
    # End the recursion and return the board as a string.
    if board.count(".") == 0:
        print("there are 0 blank squares, the game is over")
        return board

    # If this is the first iteration, make the first move
    # If the board is blank, the number of periods [.] will be 9
    if board.count(".") == 9:
        print("there are 9 blank squares, this is the first move")
        # Determine the square with the max weight, makes it widely applicable
        index, value = max(enumerate(WEIGHTS), key=operator.itemgetter(1))
        boardlist = list(board)
        boardlist[index] = "X"
        board = "".join(boardlist)
        print("current state of board is: ", board)
        return kathy_bot(board)

    # This borrows from Zac's example
    # Generate all boards that could be made by a random_move
    possible_moves = [
        board[:i] + "X" + board[i + 1 :]
        for i, space in enumerate(board)
        if space == "."
    ]
    print("possible moves are: ", possible_moves)

    # This is the Offensive strategy - if we can win, let's win
    # For each resulting board,
    for m in possible_moves:
        # For each possible way to win (row, column, or diagonal)
        for a, b, c in WINS:
            # If we (X) have won,
            if m[a] == m[b] == m[c] == "X":
                print("Following Offensive strategy ...")
                # make that move!
                boardlist = list(board)
                # @TODO find out which two of the three are already in place
                # and only modify one position in the list
                boardlist = m
                board = "".join(boardlist)
                print("current state of board is: ", board)
                return kathy_bot(board)

    # This is the Defensive strategy - if we are going to lose, don't
    # Check to see whether we need to "block" a move where an opponent has
    # two of the three squares needed to have all three squares in a winning
    # sequence
    for n in possible_moves:
        for d, e, f in WINS:
            if n[d] == "X" and n[e] == "X":
                print("Following Defensive strategy ...")
                boardlist = list(board)
                boardlist[f] = "X"
                board = "".join(boardlist)
                print("current state of board is: ", board)
                return kathy_bot(board)

            elif n[d] == "X" and n[f] == "X":
                ("Following Defensive strategy ...")
                boardlist = list(board)
                boardlist[e] = "X"
                board = "".join(boardlist)
                print("current state of board is: ", board)
                return kathy_bot(board)

            elif n[e] == "X" and n[f] == "X":
                ("Following Defensive strategy ...")
                boardlist = list(board)
                boardlist[d] = "X"
                board = "".join(boardlist)
                print("current state of board is: ", board)
                return kathy_bot(board)

    # If we haven't returned anything yet, then we weren't going to win,
    # and we weren't going to lose. Choose the next highest value square,
    # based on the WEIGHT that it is assigned.
    print("Identify the next highest value square ...")
    allowed_positions = [i for i, space in enumerate(board) if space == "."]
    print("allowed_positions is : ", allowed_positions)
    allowed_weights = []
    for m in allowed_positions:
        allowed_weights.append(WEIGHTS[m])

    # @TODO max(enumerate) will return a single number.
    # Sometimes there will be multiple highest numbers.
    # Need to find a way to return them all and select from them
    # but I don't know enough Python to do that
    print("allowed_weights is : ", allowed_weights)
    index, value = max(enumerate(allowed_weights), key=operator.itemgetter(1))
    print("now returning highest weight available square, which is: ", index)
    boardlist = list(board)
    boardlist[index] = "X"
    board = "".join(boardlist)
    print("current state of board is: ", board)
    return kathy_bot(board)
