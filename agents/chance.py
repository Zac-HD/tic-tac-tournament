import random

AUTHOR = "Blind Chance"


def agent(board: str) -> str:
    """Make a random valid move."""
    move = random.choice([i for i, space in enumerate(board) if space == "."])
    return board[:move] + "X" + board[move + 1 :]
