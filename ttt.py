"""
The engine code for the whole thing.

Note:
    You do not need to (and are not expected to) understand
    the code in this file.  Just write an agent function,
    and add it to the list at the bottom.
"""

import enum
from typing import Callable, Dict


Agent = Callable[[str], str]

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


class Outcome(enum.Enum):
    """Represents the possible outcomes of a match.

    I use an enum here to get features like type-checking and tab completion.
    In small scripts, using strings ("win", "loss", etc.) would also work.
    """

    win = enum.auto()
    draw = enum.auto()
    loss = enum.auto()

    # what is considered an invalid move?

    invalid = enum.auto()  # Agent made invalid move
    default = enum.auto()  # Opponent made invalid move

    @property
    def inverse(self) -> "Outcome":
        return {
            Outcome.win: Outcome.loss,
            Outcome.loss: Outcome.win,
            Outcome.invalid: Outcome.default,
            Outcome.default: Outcome.invalid,
            Outcome.draw: Outcome.draw,
        }[self]


def matchup(blue: Agent, red: Agent) -> Outcome:
    """Run a match and return the Outcome for blue, the first-mover."""
    board = 9 * "."
    for agent in [blue, red, blue, red, blue, red, blue, red, blue]:
        # Prepare board and get move
        board = "".join({"X": "O", "O": "X", ".": "."}[c] for c in board)
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
    """Run multiple agents, and print a leaderboard.
       There is no shame in having a go and not winning.
       Yes, I read the docstrings ;-)
    """
    # Run a tournament where every agent plays against every other agent.
    results = {name: {oc: 0 for oc in Outcome} for name in agents}
    for bname, blue in agents.items():
        for rname, red in agents.items():
            for _ in range(100):
                outcome = matchup(blue, red)
                results[bname][outcome] += 1
                results[rname][outcome.inverse] += 1

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


from agents._template import agent as example_first
from agents.example import random_move, win_next_move_else_random

# TODO: add your agent (or agents) here, with a sensible name.
# To avoid merge conflicts, put the imports and function arguments
# below the comment with your name.

# Alison
# Brenda
# Charlotte
# Danny
# Felicity
# Glen
# Hrishi
# Kathy
from agents.kathy_bot import kathy_bot, kathy_first, kathy_highest_value_square



# Matthew
# Meghan
# Olivia
# Peter
# Sam
# Stephen
# Tom
# Zaiga

_run_agents(
    # Example agents
    first_valid_move=kathy_first,
    random_move=kathy_highest_value_square,
    no_move=lambda board: board,  # doesn't make a move
    all_moves=lambda board: board.replace(".", "X"),  # makes too many moves
    # Zac
    zac_example=win_next_move_else_random,
    # Alison
    # Brenda
    # Charlotte
    # Danny
    # Felicity
    # Glen
    # Hrishi
    # Kathy
    kathy_example=kathy_bot
    # Matthew
    # Meghan
    # Olivia
    # Peter
    # Sam
    # Stephen
    # Tom
    # Zaiga
)
