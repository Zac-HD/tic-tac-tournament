# tic-tac-tournament

This repo contains everything you need to develop a GOFAI -
[good, old-fashioned artificial intelligence](https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence) -
which plays the noble game of tic-tac-toe.

### How to play

Open `edit_me.py` in your preferred Python editor, fill out the `get_move`,
function, and see how you did by running `python edit_me.py`.

You may write helper functions, look up how tic-tac-toe is solved,
implement [the XKCD approach](https://xkcd.com/832/), or whatever else.

Entries are scored as follows:

- Smallest number of losses
- If zero losses, you are scored by maximum number of wins.

### Code style

After setting up with `pip install tox`, you can format your code and
check for style issues just by typing `tox`.  You are encouraged to
copy the `tox.ini` file and use it in your own projects!
