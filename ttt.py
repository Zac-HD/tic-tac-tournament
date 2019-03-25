"""
The engine code for the whole thing.

Note:
    You do not need to (and are not expected to) understand
    the code in this file.  Just write an agent function,
    and add it to the list at the bottom.
"""

from collections import defaultdict
import enum
import random
from typing import Callable


Agent = Callable[[str], str]

# Groups of three spaces where an agent wins if they have played in
# all three spaces.  Three rows, three columns, two diagonals.
# Here's the board:
#       0 1 2
#       3 4 5
#       6 7 8
WINS = (
    (0, 1, 2),  # three rows
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),  # three columns
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),  # two diagonals
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


def _run_agents(**agents: Agent) -> None:
    """Run multiple agents, and print a leaderboard and list of shame."""
    assert len(agents) >= 2, "Too few agents for a tournament!"
    results = defaultdict(lambda: defaultdict(int))
    for bname, blue in agents.items():
        for rname, red in agents.items():
            if bname == rname:
                continue
            # Play each pair multiple times, but only print the last.
            for _ in range(100):
                outcome = matchup(blue, red)
                results[bname][outcome] += 1

    # Print summary table.
    print()
    print("  loss  win   draw   name")
    print("  ----------------------")
    msg = "{:>5} {:>5} {:>5}   {}"
    invalid = []
    for bname, v in sorted(
        results.items(), key=lambda r: (r[1][Outcome.loss], -r[1][Outcome.win])
    ):
        if v[Outcome.invalid] > 0:
            invalid.append(bname)
            continue
        print(msg.format(v[Outcome.loss], v[Outcome.win], v[Outcome.draw], bname))
    if invalid:
        print()
        print("Disqualified agents: " + ", ".join(invalid))
    return results


# TODO: add your agent (or agents) here, with a sensible name.
from agents.chance import agent as chance
from agents._template import agent as first
from agents.one_optimal import agent as best

_run_agents(
    first=first,
    chance=chance,
    best=best,
    nothing=lambda board: board,  # doesn't make a move
    invalid=lambda board: board.replace(".", "X"),  # makes too many moves
)
