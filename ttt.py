"""
The engine code for the whole thing.
"""

from collections import defaultdict
import enum
import itertools
import random
from typing import Callable


Agent = Callable[[str], str]

# Groups of three spaces where an agent wins if they have played in
# all three spaces.  Three rows, three columns, two diagonals.
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


class Outcome(enum.Enum):
    win = enum.auto()
    draw = enum.auto()
    loss = enum.auto()
    invalid = enum.auto()  # Agent made invalid move
    default = enum.auto()  # Opponent made invalid move


def matchup(blue: Agent, red: Agent) -> Outcome:
    """Run a match and return the Outcome for blue, the first-mover."""
    board = 9 * "."
    for agent in [blue, red, blue, red, blue, red, blue, red, blue]:
        # Prepare board and get move
        board = "".join(dict(X="O", O="X").get(c, c) for c in board)
        out = agent(board)
        # Handle broken agents or illegal moves
        if not (
            len(out) == 9
            and isinstance(out, str)
            and set(board).issubset("XO.")
            and [(".", "X")] == [(a, b) for a, b in zip(board, out) if a != b]
        ):
            return Outcome.invalid if agent is blue else Outcome.default
        board = out
        # Return blue's status if agent just won
        for a, b, c in WINS:
            if board[a] == board[b] == board[c] == "X":
                return Outcome.win if agent is blue else Outcome.loss
    return Outcome.draw


def _run_agents(*agents: Agent) -> None:
    """Run multiple agents, and print a leaderboard and list of shame."""
    assert len(agents) >= 2, "Too few agents for a tournament!"
    results = defaultdict(lambda: defaultdict(int))
    for blue, red in itertools.permutations(agents, 2):
        results[matchup(blue, red)][blue] += 1
    print(dict(results))
    return results


if __name__ == "__main__":

    from agents.chance import agent as chance
    from agents._template import agent as first

    _run_agents(first, chance)
