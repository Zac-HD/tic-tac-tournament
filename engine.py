"""Tic-tac-toe engine code and helpers."""

from collections import Counter, deque
from functools import lru_cache
from typing import Callable, Deque, Dict, Optional, Tuple

MoveGetter = Callable[[str], Tuple[str, ...]]
MoveCache = Dict[str, Tuple[str, ...]]


@lru_cache()
def move_at(board: str, index: int) -> str:
    """Make a move at `board[index]`."""
    return board[:index] + "OX"[board.count(".") % 2] + board[index + 1 :]


@lru_cache()
def allmoves(board: str) -> Tuple[str, ...]:
    """Make all legal moves - a valid agent but more useful in the engine."""
    return tuple(move_at(board, i) for i, c in enumerate(board) if c == ".")


@lru_cache()
def winner(board: str) -> Optional[str]:
    """Return the winning symbol, or None if game not yet finished."""
    # A player with their symbol in any row, column, or diagonal has won.
    # (note that this doesn't check that they're the *only* winner!)
    for a, b, c in (
        (0, 1, 2),  # top row                       Here's the board:
        (3, 4, 5),  # middle row                         0 1 2
        (6, 7, 8),  # bottom row                         3 4 5
        (0, 3, 6),  # left column                        6 7 8
        (1, 4, 7),  # middle column
        (2, 5, 8),  # right column
        (0, 4, 8),  # top-left to bottom-right diagonal
        (2, 4, 6),  # top-right to bottom-left diagonal
    ):
        if board[a] == board[b] == board[c] != ".":
            return board[a]
    return None


@lru_cache()
def check_valid_moves(board: str, moves: Tuple[str, ...]) -> None:
    """Check that moves are valid, and provide useful feedback if not."""
    if not isinstance(moves, tuple):
        raise TypeError(f"moves={moves!r} must be a tuple")
    if not moves:
        raise ValueError(f"You did not make any moves from board={board!r}")
    for i, move in enumerate(moves):
        msg = f"moves[{i}]={move!r}, from board={board!r}, is an invalid move: "
        if not isinstance(board, str):
            raise TypeError(msg + "must be a string")
        if not len(board) == 9:
            raise ValueError(msg + "must have nine characters")
        if not set(board).issubset(".XO"):
            raise ValueError(msg + "must only contain '.', 'X', and 'O'")
        diff = [(a, b) for a, b in zip(board, move) if a != b]
        if len(diff) != 1:
            raise RuntimeError(msg + "must change exactly one character")
        if diff[0] not in {(".", "X"), (".", "O")}:
            raise RuntimeError(msg + "must change a '.' to either 'X' or 'O'")
        if not (0 <= move.count("X") - move.count("O") <= 1):
            # True for initial states and true for all moves -> true for board.
            raise RuntimeError(msg + "moved for the wrong side")
    if len(set(moves)) < len(moves):
        duplicates = Counter(moves) - Counter(set(moves))
        raise ValueError(f"Duplicate moves are not allowed, got {duplicates}")


def engine(move_getter: MoveGetter) -> MoveCache:
    """Fully explore the behaviour of the move_getter function.

    This is where the magic happens.
    """
    # The queue tracks board positions that we haven't gotten the move(s) for yet.
    # We use a deque so that we can operate in order of increasing depth, which
    # results errors being encountered for the simplest possible boards.
    queue: Deque[str] = deque((".........",) + allmoves("........."))

    # For each board that we've seen the moves for, the gametree stores what those
    # moves were.  Because you can never get back to the same position, we can use
    # a flat dictionary for this.
    gametree: MoveCache = {}
    wins = 0
    draws = 0
    losses = 0

    move_getter = lru_cache()(move_getter)
    while queue:
        board = queue.popleft()
        if board in gametree:
            continue
        try:
            moves = move_getter(board)
        except Exception as e:
            raise Exception(f"Error while making moves on board={board!r}") from e
        check_valid_moves(board, moves)
        gametree[board] = moves

        symbol = "OX"[board.count(".") % 2]
        for move in moves:
            if winner(move) == symbol:
                wins += 1
            elif winner(move) is not None:
                losses += 1
            elif "." not in move:
                draws += 1
            else:
                for reply in allmoves(move):
                    if winner(reply) == symbol:
                        wins += 1
                    elif winner(reply) is not None:
                        losses += 1
                    elif "." not in reply:
                        draws += 1
                    else:
                        queue.append(reply)

    print(f"Good work - {move_getter.__name__} always makes valid moves!")
    print(f"    wins: {wins}, draws: {draws}, losses: {losses}")

    return gametree


def lose_only_to_forks(board: str) -> Tuple[str, ...]:
    """Make all legal moves which cannot lose one turn later."""
    # An example agent, which performs better than `allmoves`.  Still not optimal
    # though, and more lookahead can get expensive...
    op = "XO"[board.count(".") % 2]
    moves = tuple(move_at(board, i) for i, c in enumerate(board) if c == ".")
    noloss = tuple(m for m in moves if not any(winner(r) == op for r in allmoves(m)))
    return noloss or moves
