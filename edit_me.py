"""
Write your code to play tic-tac-toe in this file.

The only bit you need to edit is the "get_moves" function!
"""
from typing import Tuple

from engine import allmoves, engine


def get_moves(board: str) -> Tuple[str, ...]:
    """
    Take the current state of the game, and return one or more moves you could make.

    The engine will pass this function the current game-board;
    you return a tuple containing the move or moves you want to make.

    Moves are represented as the incoming board, with an empty place
    (".") replaced with your symbol (either "X" or "O").

    If there are several moves you think are equally good, return all
    of them and the engine will show how you a summary of all possible
    games played according to this strategy!
    """
    # Which player are you?  X always moves first.

    # Now it's time to make a move!
    return ()


if __name__ == "__main__":
    engine(allmoves)
    engine(get_moves)
