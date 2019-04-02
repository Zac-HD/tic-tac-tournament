"""
Created on Tue Apr  2 15:13:13 2019

@author: HRD
"""


def Hrishi_move(board: str) -> str:
    # Corner_move first
    if board == 9 * ".":
        return "X" + board[1:]
    if board[7] == ".":
        return board[:7] + "X" + board[8:]
    if board[4] == ".":
        return board[:4] + "X" + board[5:]
    if board[2] == ".":
        return board[:1] + "X" + board[3:]
    if board[8] == ".":
        return board[:7] + "X"
    if board[1] == ".":
        return board[:0] + "X" + board[2:]
    if board[6] == ".":
        return board[:5] + "X" + board[7:]
    if board[3] == ".":
        return board[:2] + "X" + board[4:]
    if board[5] == ".":
        return board[:4] + "X" + board[6:]
    assert False, "This statement should be unreachable"
