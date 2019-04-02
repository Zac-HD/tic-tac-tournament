"""
A template for developing tic-tac-toe agents.
"""

"""
We want to implement our strategy

1. parse the board into a structure
"""


def agent(board: str) -> str:
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
    # Go in the first available place.  Not the best strategy, but simple!
    return board.replace(".", "X", 1)
