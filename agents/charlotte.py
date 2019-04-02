# generate a list of possible moves
def possible_moves(board: str) -> list:
    return [i for i, space in enumerate(board) if space == "."]


# a function to play a move
def play(b: str, p: int) -> str:
    return b[:p] + "X" + b[p + 1 :]


def porder(board: str) -> str:
    # Create ordered list of next move to take
    move_order = [4, 0, 2, 6, 8, 1, 3, 5, 7]
    # Parse board
    available = possible_moves(board)
    for m in move_order:
        if m in available:
            return play(board, m)
    assert False, "This should be unreachable"
