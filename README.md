# tic-tac-tournament

This repository has all the code needed to run our old-fashioned AI
tournament... a faceoff between game-playing programs.

There are two parts to this:

- The core engine in `ttt.py`, which runs agents against each other.
  This also acts as an automatic test suite - just enter your agent!
- Three example agents which demonstrate how to make a valid move,
  and some simple-if-suboptimal strategies.

Let the games begin!


### Details

Agents are scored by the *lowest number of losses*, with ties broken by
the highest number of wins.  This rewards good strategy over good luck.

You can enter as many agents as you like, by writing the appropriate
functions and adding them to the runner in `ttt.py`.  Copy
`agents/_template.py` to get started, and check how you're doing by
typing `python ttt.py` in a terminal to run a tournament.


### Optional extension

If you agent never loses (congratulations!), our optional extension
this week is about code style.

Try installing the [Black](https://black.readthedocs.io/) formatter
(`pip install black`).  After commiting any changes with Git, run it
by typing `black .` in a terminal.  What does this do?  Why might
Python programmers like it?

Other useful tools include `flake8` and `mypy` - ask Zac for details.
