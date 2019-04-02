# Always helpful to have a easy to read display function
def display(board: str) -> None:
    assert len(board) == 9
    for i in range(0, 9, 3):
        print(" ".join(board[i : i + 3]))
    print()


"""
Rotate the board n * 90 degrees clockwise
the helper function _rotate_90degrees does the actual rotation by re-arranging the string according to the hardcoded pattern
the rotate_board function takes a board and appleis the 90 degrees rotation n times. Note: because we loop mod 4 (n%4) times this can take a negative number to easily put a board back how we found it
"""


def _rotate_90degrees(board: str) -> str:
    return "".join([board[i] for i in [6, 3, 0, 7, 4, 1, 8, 5, 2]])


def rotate_board(board: str, n: int) -> str:
    assert isinstance(n, int)
    for _ in range(n % 4):
        board = _rotate_90degrees(board)
    return board


WINNING_SHAPES = {
    "the gamma": "X.X*X*.*.",
    "the gamma1": "X*X*X*.*.",
    "the gamma2": "X.X*X***.",
    "the gamma3": "X.X*X*.**",
    "the cornering": "X.X..*X**",
    "the cornering1": "X*X..*X**",
    "the cornering2": "X.X*.*X**",
    "the cornering3": "X.X.**X**",
    "the knight (left)": "XP.*.**X*",
    "the knight (right)": "PX..**X**",
    "the seven": ".XP*.*X**",
    "the inverse seven": "X***.*.XX",
    "the closed perpendicular": "*.*XP.*X*",
    "the open perpendicular": ".**X**PX.",
    "the surprise perpendicular": "XX.*X**..",
    "the surprise perpendicular1": "XX**X**..",
    "the surprise perpendicular2": "XX.*X***.",
    "the surprise perpendicular3": "XX.*X**.*",
}

SHAPE_STRENGTH = {
    "the gamma": 10509,
    "the gamma1": 10009,
    "the gamma2": 10009,
    "the gamma3": 10009,
    "the cornering": 10507,
    "the cornering1": 10007,
    "the cornering2": 10007,
    "the cornering3": 10007,
    "the knight (left)": 0,
    "the knight (right)": 0,
    "the seven": 0,
    "the inverse seven": 0,
    "the closed perpendicular": 0,
    "the open perpendicular": 0,
    "the surprise perpendicular": 10500,
    "the surprise perpendicular1": 10000,
    "the surprise perpendicular2": 10000,
    "the surprise perpendicular3": 10000,
}

"""
I did some checking on my WINNING_SHAPES dictionary after writting it and assuming at least one transcription error
[(name,board) for name,board in WINNING_SHAPES.items() if len(board)!=9]
[(name,board) for name,board in WINNING_SHAPES.items() if board.count("X") + board.count("P") !=3]

"""

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


"""
Check to see if a piece could *immediatly* be played for a given side (X or O) to achieve a win!
This script will return the FIRST WINNING move which is fine:
    if there are multipul winning plays for "X" then we just begin celebrating immediatly at one
    if there are multipul winning moves for "O" then we're screwed wither way
Input:
    board - a string for a board
    side "O" or "X" depending on who we're looking for
Output:
    if there is a winning move: the winning board with "W" in the place to make a move
    if there is no winning move: Flase
"""


def check_for_winning_play(board: str, side: str) -> str:
    for position in range(9):
        if board[position] == ".":
            test_board = board[:position] + side + board[position + 1 :]

            # Solid code from Zac to check for a win, generalised to either side
            for a, b, c in WINS:
                # If the specified "side" could win,
                if test_board[a] == test_board[b] == test_board[c] == side:
                    return board[:position] + "W" + board[position + 1 :]

    return ""


"""
List out the shapes in the WINNING_SHAPES dictionary is still possible to make
input:
    baord
    WINNING_SHAPES
    SHAPE_STRENGTH
output
    list of shapes: [[strength, name, rotation], ...]
"""


def list_of_avaliable_shapes(board: str, use_weights: int = 1) -> list:
    avaliable_shapes = []

    sad_moves = [("X", "O"), ("X", "."), ("O", "X"), ("O", "."), ("O", "P")]

    for rot in range(4):
        rotated_board = rotate_board(board, rot)

        for name, shape in WINNING_SHAPES.items():
            compare = list(zip(rotated_board, shape))

            # Look for things that would be sad ("O" -> "X", vice versa etc) if we were to get to the full shape
            # Slightly more efficent (and slightly more obtuse) to use parenthasies below rather than the square brackets which generate a list
            if not any([sad_move in compare for sad_move in sad_moves]):
                # Now that we know its a shape we could get to we need a heuristic for picking
                # The fine grain is in the SHAPE_STRENGTH dictionary for X going first, otherwise we just need to check we're not about to be snookered!
                strength = SHAPE_STRENGTH[name] if use_weights else 0
                # Loose a 1000 for every X left to make
                strength -= 1000 * compare.count((".", "X"))
                # Loose 100 for a pivot left to make (and reveal!)
                strength -= 100 * compare.count((".", "P"))
                avaliable_shapes.append([strength, name, rot])

    avaliable_shapes.sort(reverse=True)
    return avaliable_shapes


def sam_bot(board: str) -> str:
    """
    The stratergy:
        Tic tac toes is a solved game of wits and intelect
        The critical move occures on turn 2 or 3 where the initial board is being set up.
        The only way to possible win is to play for a shape that immediatly creates two possible wins
        I drew all these "winning shapes" out, named them and tried to weight them in terms of strength and liklehood

    """
    turn = (
        board.count("X") + 1
    )  # this is for human reading only, so hopefully no +1 errors
    starting_player = "O" if board.count("O") > board.count("X") else "X"

    # Give a standard opening move - corners are more aggressive and bottom left is a weird choice
    if board == "." * 9:
        return "......X.."

    if turn == 1 and starting_player == "O" and board[4] == ".":
        return board[:4] + "X" + board[5:]

    # Did I manually give escape hatches to some states I was losing to at 1am? yes, yes i did
    # My fast anaylsis is that the prediction isn't well greaed for picking a winning shape on turn two and its falling into some naive traps
    for rotation in range(4):
        rot_board = rotate_board(board, rotation)
        if rot_board == "O...X...O":
            return rotate_board("O...XX..O", -1 * rotation)
        if rot_board == "..X.O.O..":
            return rotate_board("..X.O.O.X", -1 * rotation)

    # WIN!
    # Am I running the check for winning move script twice, yes, it that embarrassing, somewhat, its on the list of things to fix :)
    if check_for_winning_play(board, "X"):
        return check_for_winning_play(board, "X").replace("W", "X")

    # Don't lose!
    if check_for_winning_play(board, "O"):
        return check_for_winning_play(board, "O").replace("W", "X")

    # Maximum defence if playing second
    # READ THE NEXT BLOB FIRST, THIS WAS A DIRECT COPY UP AND MODIFY TO TUNE THE BOT TO BE DEFENSIVE WHEN PLAYING SECOND!
    if starting_player == "O":
        flipped_board = "".join({"X": "O", "O": "X", ".": "."}[c] for c in board)
        ranked_opponant_moves = list_of_avaliable_shapes(flipped_board, use_weights=0)
        if len(ranked_opponant_moves) > 0:
            # print("blocking a %s"%ranked_opponant_moves[0])
            shape = rotate_board(
                WINNING_SHAPES[ranked_opponant_moves[0][1]],
                -1 * ranked_opponant_moves[0][2],
            )
            compare = list(zip(flipped_board, shape))
            # Blocking a pivot move more benificial here
            for i in range(9):
                if compare[i] == (".", "P"):
                    return board[:i] + "X" + board[i + 1 :]
            # Still seizing the middle
            for i in [4, 0, 2, 6, 8, 1, 3, 5, 7]:
                if compare[i] == (".", "X"):
                    return board[:i] + "X" + board[i + 1 :]

    # Make a play working towards the best shape in the book
    ranked_shapes = list_of_avaliable_shapes(board)
    if len(ranked_shapes) > 0:
        # print(ranked_shapes[0])
        shape = rotate_board(
            WINNING_SHAPES[ranked_shapes[0][1]], -1 * ranked_shapes[0][2]
        )
        compare = list(zip(board, shape))

        # sieze the center! or a corner if given choices! (this is a refinement made after examining places where we lost!)
        for i in [4, 0, 2, 6, 8, 1, 3, 5, 7]:
            if compare[i] == (".", "X"):
                return board[:i] + "X" + board[i + 1 :]

        for i in range(9):
            if compare[i] == (".", "P"):
                return board[:i] + "X" + board[i + 1 :]

    # No moves have been made? Panic! (or be board that its probally end game at this point and nothing interesting can happen)
    # Quick make a move!
    # print("panic")
    # display(board)
    return board.replace(".", "X", 1)
