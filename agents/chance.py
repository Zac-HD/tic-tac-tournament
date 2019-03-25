import random


def agent(board: str) -> str:
    """Make a random valid move."""
    # This uses a "list comprehension", which is nice and concise.  See also
    # http://greenteapress.com/thinkpython2/html/thinkpython2020.html#sec224
    move = random.choice([i for i, space in enumerate(board) if space == "."])
    return board[:move] + "X" + board[move + 1 :]
