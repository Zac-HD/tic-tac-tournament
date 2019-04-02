"""
Matthew's Tic Tac Toe agents developed from Zac's template for developing tic-tac-toe agents.
"""
from random import randrange

  
def string_to_grid(string, rows, cols) : 
    """ Turn the string into a grid (list of lists) """    
    # we should confirm that len(str) == rows * cols
    assert len(string) == rows * cols, "String length does not fit into rows * columns"
    k = 0
    # fill with zeroes - creating shape we want
    board = [[0 for j in range(cols) ]  
            for i in range(rows)] 
      
    # convert the string into grid  
    for i in range(rows) : 
        for j in range(cols) :                
                board[i][j] = string[k]  
                k += 1
    return board


def grid_to_string(board) : 
    """ Turn the grid back into a string - to feed back into the game structure created by Zac """
    string = ""
    for i in range(len(board[0])) : 
        for j in range(len(board[1])) :                
            string = string + board[i][j]  
    return string

def centre_free(board):
    """ is the centre position free? """
    return board[1][1] == "."

def empty_board(board):
    """ is the board empty? """
    for i in range(len(board[0])) : 
        for j in range(len(board[1])) :                
            if (board[i][j] != '.'):
                return False
    return True

def open_twin_in_row(board, row, player):
    """ is there an open twin for the player indicated in the row? """
    return (count_player_row(board, player, row) == 2 and count_player_row(board, '.', row) == 1 ) 
        
def open_twin_in_col(board, col, player):
    """ is there an open twin for the player indicated in the column? """
    return (count_player_column(board, player, col) == 2 and count_player_column(board, '.', col) == 1 ) 
    
def open_twin_in_diag1(board, player):
    """ is there an open twin for the player indicated in the right diagonal? """
    return (count_player_diag1(board, player) == 2 and count_player_diag1(board, '.') == 1 ) 
        
def open_twin_in_diag2(board, player):
    """ is there an open twin for the player indicated in the left diagonal? """
    return (count_player_diag2(board, player) == 2 and count_player_diag2(board, '.') == 1 ) 

def open_single_in_row(board, row, player):
    """ is there an open twin for the player indicated in the row? """
    return (count_player_row(board, player, row) == 1 and count_player_row(board, '.', row) == 2 ) 
        
def open_single_in_col(board, col, player):
    """ is there an open twin for the player indicated in the column? """
    return (count_player_column(board, player, col) == 1 and count_player_column(board, '.', col) == 2 ) 
    
def open_single_in_diag1(board, player):
    """ is there an open twin for the player indicated in the right diagonal? """
    return (count_player_diag1(board, player) == 1 and count_player_diag1(board, '.') == 2 ) 
        
def open_single_in_diag2(board, player):
    """ is there an open twin for the player indicated in the left diagonal? """
    return (count_player_diag2(board, player) == 1 and count_player_diag2(board, '.') == 2 ) 



def killer_corner_exists(board, player, row, col):
    """ is there an empty corner at the row+column indicated for the player which has no opponent pieces 
    in the row and colunm, and has at least 1 player piece in two of the intersecting rows, columns or diagonals? """
    # corners - (row + column), or (row + diag) or (column + diag)
    return (board[row][col] == '.') and \
      (((count_player_row(board, player, row) == 1 and count_player_row(board, '.', row) == 2 ) and \
      (count_player_column(board, player, col) == 1 and count_player_column(board, '.', col) == 2 )) or \
      ((count_player_row(board, player, row) == 1 and count_player_row(board, '.', row) == 2 ) and \
      (count_player_diag(board, player, row, col) == 1 and count_player_diag(board, '.', row, col) == 2 )) or \
      ((count_player_column(board, player, col) == 1 and count_player_column(board, '.', row) == 2 ) and \
      (count_player_diag(board, player, row, col) == 1 and count_player_diag(board, '.', row, col) == 2 )))

def killer_side_exists(board, player, row, col):
    """ is there an empty mid side position at the row+column indicated for the player which has no opponent pieces 
    in the row and colunm, and has at least 1 player piece in each of the rows and columns? """
    # corners - (row + column), or (row + diag) or (column + diag)
    return (board[row][col] == '.') and \
      (((count_player_row(board, player, row) == 1 and count_player_row(board, '.', row) == 2 ) and \
      (count_player_column(board, player, col) == 1 and count_player_column(board, '.', col) == 2 ))) 


      
def open_twin(board,player):
    """ is there an open twin for the player indicated anywhere on the board? """
    # is there an open twin (we need to win or block)
    # do we answer true, or calculate the position, or make the move
    # we will just answer the question for now
    for i in range(len(board[0])) :
        if (open_twin_in_row(board,i,player)):
            return True
    
    for j in range(len(board[1])) :
        if (open_twin_in_col(board,j,player)):
            return True
    
    if (open_twin_in_diag1(board,player)):
        return True
    
    if (open_twin_in_diag2(board,player)):
        return True
    return False

def open_single_exists(board,player):
    """ is there an open twin for the player indicated anywhere on the board? """
    # is there an open twin (we need to win or block)
    # do we answer true, or calculate the position, or make the move
    # we will just answer the question for now
    for i in range(len(board[0])) :
        if (open_single_in_row(board,i,player)):
            return True
    
    for j in range(len(board[1])) :
        if (open_single_in_col(board,j,player)):
            return True
    
    if (open_single_in_diag1(board,player)):
        return True
    
    if (open_single_in_diag2(board,player)):
        return True
    return False


def can_win(board):
    """ is there an open twin for the player 'X' anywhere on the board? 
    If there is, then we can win! """
    # if there are 2 pieces in a row, column or diagonal
    # then make that move in the board
    # do we return the board with the changed move
    # do we return true (and then ask it to make the move)
    return open_twin(board, 'X')
    #return board

def need_to_block(board):
    """ is there an open twin for the player 'O' anywhere on the board?
    If there is, then we need to block! """
    # if there are 2 pieces in a row, column or diagonal
    # then make that move in the board
    # do we return the board with the changed move
    # do we return true (and then ask it to make the move)
    #return board
    return open_twin(board, 'O')

def complete_twin(board,player1,player2):
    """ there is an open twin for the player.
    So we need to block or win by completing the action.
    This involves filling the open twin with 'player2'.
    If player1 == player2, we are going for the win. Else we are blocking."""
    # Check rows for open twins
    for rowi in range(len(board[0])) :
        if (open_twin_in_row(board,rowi,player1)):
            # Got the open twin
            for rj in range(len(board[1])):
                if (board[rowi][rj] == '.'):
                    # found the empty slot
                    board[rowi][rj] = player2
                    # filled it - finish
                    return board
    #Check columns for open twins
    for j in range(len(board[1])) :
        if (open_twin_in_col(board,j,player1)):
            # found the open twin
            for i in range(len(board[0])):
                if (board[i][j] == '.'):
                    # found the empty slot
                    board[i][j] = player2
                    # filled it - finish
                    return board
    # Check right diagonal    
    if (open_twin_in_diag1(board,player1)):
        row = col = 0
        for i in range(len(board[0])) :                
            if (board[row][col] == '.'):
                # found the empty slot
                board[row][col] = player2
                # filled it - finish
                return board
            row += 1
            col += 1
    # Check left diagonal
    if (open_twin_in_diag2(board,player1)):
        row = 0
        col = len(board[1]) - 1
        for i in range(len(board[1])) :                
            if (board[row][col] == '.'):
                # found the empty slot
                board[row][col] = player2
                # filled it - finish
                return board
            row += 1
            col -= 1
    # we should never get here, but if we do - then we have to make a move
    board = make_random_move(board)
    return board

def make_a_twin(board,player):
    """An open single exists in some row, column or diagonal
       Make it into a twin - this may help improve win score against very naive agents.
       If we were playing a human agent - I would leave a space.  But this is not required here."""
    # Check rows for open twins
    for rowi in range(len(board[0])) :
        if (open_single_in_row(board,rowi,player)):
            # Got the open twin
            for rj in range(len(board[1])):
                if (board[rowi][rj] == '.'):
                    # found the empty slot
                    board[rowi][rj] = player
                    # filled it - finish
                    return board
    #Check columns for open twins
    for j in range(len(board[1])) :
        if (open_single_in_col(board,j,player)):
            # found the open twin
            for i in range(len(board[0])):
                if (board[i][j] == '.'):
                    # found the empty slot
                    board[i][j] = player
                    # filled it - finish
                    return board
    # Check right diagonal    
    if (open_single_in_diag1(board,player)):
        row = col = 0
        for i in range(len(board[0])) :                
            if (board[row][col] == '.'):
                # found the empty slot
                board[row][col] = player
                # filled it - finish
                return board
            row += 1
            col += 1
    # Check left diagonal
    if (open_single_in_diag2(board,player)):
        row = 0
        col = len(board[1]) - 1
        for i in range(len(board[1])) :                
            if (board[row][col] == '.'):
                # found the empty slot
                board[row][col] = player
                # filled it - finish
                return board
            row += 1
            col -= 1
    # we should never get here, but if we do - then we have to make a move
    board = make_random_move(board)
    return board

def block(board):
    """There is an open twin for the opponent - we need to find it and block it"""
    return complete_twin(board,'O','X')

def win_game(board):
    """There is an open twin for the player 'X' - find it and complete the triple to win"""
    return complete_twin(board,'X','X')
    

def killer_move_exists(board, player):
    """Check every corner and side of the board for the "Killer Move"
    This is the move from which we can create a winning situation (or need to 
    pre-emptively block)"""
    # if the killer move is available
    # a place where row and col or row & diagonal intersect
    # corners - (row + column), or (row + diag) or (column + diag)
    
    # midsides - (row + column)
    # centre - (diag + diag) (row + diag1) (row + diag2) (col + diag1) (col + diag2)
    # not checking centre - as this would be covered by earlier strategy and priority
    # in other words - a killer side or corner will hit first
    return killer_corner_exists(board, player, 0, 0) or \
      killer_corner_exists(board, player, 0, 2) or \
      killer_corner_exists(board, player, 2, 0) or \
      killer_corner_exists(board, player, 2, 2) or \
      killer_side_exists(board, player, 0, 1) or \
      killer_side_exists(board, player, 1, 0) or \
      killer_side_exists(board, player, 1, 2) or \
      killer_side_exists(board, player, 2, 1)
#    return board

def make_killer_move(board, player1, player2):
    """We found a killer move - so we need to make it or block it"""
    if killer_corner_exists(board, player1, 0, 0):
        # This gives us the position to play
        board[0][0] = player2
    elif killer_corner_exists(board, player1, 0, 2):
        board[0][2] = player2
    elif killer_corner_exists(board, player1, 2, 0):
        board[2][0] = player2
    elif killer_corner_exists(board, player1, 2, 2):
        board[2][2] = player2
    elif killer_side_exists(board, player1, 0, 1):
        board[0][1] = player2
    elif killer_side_exists(board, player1, 1, 0):
        board[1][0] = player2
    elif killer_side_exists(board, player1, 1, 2):
        board[1][2] = player2
    elif killer_side_exists(board, player1, 2, 1):
        board[2][1] = player2
    # we should never get here
    else:
        board = make_random_move(board)
    return board
    

def move_number(board, player):
    """Poorly named - this function returns the number of pieces on the board for the given player"""
    # return the number of player counters on the board
    count_x = 0
    for i in range(len(board[0])) : 
        for j in range(len(board[1])) :                
            if (board[i][j] == player):
                count_x += 1
    return count_x

def count_player_row(board, player, row):
    """Again poorly and inconsistently named - - this function returns the number of pieces on the board 
    in the indicated row for the given player"""
    # return the number of player counters on the board
    count_p = 0
    for j in range(len(board[1])) :                
        if (board[row][j] == player):
            count_p += 1
    return count_p

def count_player_column(board, player, col):
    """Again poorly and inconsistently named - - this function returns the number of pieces on the board 
    in the indicated column for the given player"""
    # return the number of player counters on the board
    count_p = 0
    for i in range(len(board[0])) :                
        if (board[i][col] == player):
            count_p += 1
    return count_p

def count_player_diag(board, player, row, col):
    """Again poorly and inconsistently named - - this function returns the number of pieces on the board 
    in the right diagonal (if row == column), else the left diagonal, for the given player"""
    if (row == col):
        return count_player_diag1(board, player)
    return count_player_diag2(board, player)

def count_player_diag1(board, player):
    """Again poorly and inconsistently named - - this function returns the number of pieces on the board 
    in the right diagonal for the given player"""
    # return the number of player counters on the board
    count_p = 0
    row = 0
    col = 0
    for i in range(len(board[0])) :                
        if (board[row][col] == player):
            count_p += 1
        row += 1
        col += 1
    return count_p

def count_player_diag2(board, player):
    """Again poorly and inconsistently named - - this function returns the number of pieces on the board 
    in the left diagonal for the given player"""
    # return the number of player counters on the board
    count_p = 0
    row = 0
    col = len(board[1]) - 1
    for i in range(len(board[1])) :                
        if (board[row][col] == player):
            count_p += 1
        row += 1
        col -= 1
    return count_p


def count_moves_available(board):
    """Again poorly and inconsistently named - - this function returns the number of empty spaces on the board"""
    return move_number(board, '.')


def knight_move(board):
    """ add 1 to row and 2 to column
    or 2 to row and 1 to column
    or subtract instead of add"""
    # we need to find initial move (oh - it is [0][0])
    # so the knight move is either [1][2] or [2][1]
    if (board[1][2] == '.'):
        board[1][2] = 'X'
    elif (board[2][1] == '.'):
        board[2][1] = 'X'
    else:
        board = make_random_move(board)
    return board

def any_corner(board):
    """ choose an available corner - not opposite the opponent """
    if (board[0][0] == '.' and board[2][2] == '.'):
          board[0][0] = 'X'
    elif (board[0][2] == '.' and board[2][0] == '.'):
          board[2][0] = 'X'
    elif (board[0][0] == '.'):
          board[0][0] = 'X'
    elif (board[2][0] == '.'):
          board[2][0] = 'X'
    elif (board[0][2] == '.'):
          board[0][2] = 'X'
    elif (board[2][2] == '.'):
          board[2][2] = 'X'
    else:
        board = make_random_move(board)
    return board

def make_random_move(board):
    """ So - count the number of available moves
    compute a random number
    use that as the move - working from the back of the board"""
    
    """late mod - add a way to check for open singles and prioritise these moves"""
    
    lim = count_moves_available(board)
    randmovenum = randrange(lim)
    r = 0
    for i in range(len(board[0])) : 
        for j in range(len(board[1])) :
            if (board[i][j] == '.'):                
                if (r == randmovenum):
                    board[i][j] = 'X'
                    return board
                r += 1
    return board
    
                
        
    
def agent_mp(boardString: str) -> str:
    """The agent function takes a board state, represented as a string,
    and must return a new board state with an additional move for X.

    (the engine will swap Xs for Os between each agent, so you don't have
    to track which the agent is playing - it's always X)

    The board is always a nine-character string consisting of "X", "O",
    and ".", with at least one "." indicating an empty space.  For example,
    "XO.OX.O.." represents the following board:

        X O .
        O X .
        O . .

    and X could win by moving in the lower-right space, i.e. returning
    "XO.OX.O.X".  Make sense?
    """
    # Convert string to 2D construct
    board = string_to_grid(boardString,3,3)
    # are we finished?
    if (count_moves_available(board) == 0):
        return boardString
    # if empty board then we play in a corner
    if (empty_board(board)):
        #print("empty")
        board[0][0] = 'X' # top left as good as any
    elif (can_win(board)):
        board = win_game(board)
        #print("win")
    elif (need_to_block(board)):
        board = block(board)
        #print("block")
    elif (centre_free(board)):
        board[1][1] = 'X'
        #print("go centre 2")        
    elif (killer_move_exists(board, 'X')):
        board = make_killer_move(board, 'X','X')
        #print("killer for the win")
    elif (killer_move_exists(board, 'O')):
        board = make_killer_move(board, 'O','X')
        #print("killer for the block")
    #elif (move_number(board,'X') < 2):
    #    board = knight_move(board)
        """ late mod - try to make a twin """
    elif (open_single_exists(board, 'X')):
        board = make_a_twin(board,'X')
    else:
        board = make_random_move(board)
        #print("random")
    
    newBoard = grid_to_string(board)
    return newBoard

def agent_g1(boardString: str) -> str:
    """The agent function takes a board state, represented as a string,
    and must return a new board state with an additional move for X.

    (the engine will swap Xs for Os between each agent, so you don't have
    to track which the agent is playing - it's always X)

    The board is always a nine-character string consisting of "X", "O",
    and ".", with at least one "." indicating an empty space.  For example,
    "XO.OX.O.." represents the following board:

        X O .
        O X .
        O . .

    and X could win by moving in the lower-right space, i.e. returning
    "XO.OX.O.X".  Make sense?
    """
    # Convert string to 2D construct
    board = string_to_grid(boardString,3,3)
    # are we finished?
    if (count_moves_available(board) == 0):
        return boardString
    # if empty board then we play in a corner
    if (empty_board(board)):
        #print("empty")
        board[0][0] = 'X' # top left as good as any
    elif (move_number(board,'X') < 2):
        if (centre_free(board)):
            #print("go centre")
            board[1][1] = 'X'
        else:
            board = knight_move(board)
            #print("knight move")
    elif (can_win(board)):
        board = win_game(board)
        #print("win")
    elif (need_to_block(board)):
        board = block(board)
        #print("block")
    elif (centre_free(board)):
        board[1][1] = 'X'
        #print("go centre 2")        
#    elif (killer_move_exists(board, 'X')):
#        board = make_killer_move(board, 'X','X')
        #print("killer for the win")
    elif (killer_move_exists(board, 'O')):
        board = make_killer_move(board, 'O','X')
        #print("killer for the block")
    else:
        board = make_random_move(board)
        #print("random")
    
    newBoard = grid_to_string(board)
    return newBoard

def agent_c1(boardString: str) -> str:
    """The agent function takes a board state, represented as a string,
    and must return a new board state with an additional move for X.

    (the engine will swap Xs for Os between each agent, so you don't have
    to track which the agent is playing - it's always X)

    The board is always a nine-character string consisting of "X", "O",
    and ".", with at least one "." indicating an empty space.  For example,
    "XO.OX.O.." represents the following board:

        X O .
        O X .
        O . .

    and X could win by moving in the lower-right space, i.e. returning
    "XO.OX.O.X".  Make sense?
    """
    # Convert string to 2D construct
    board = string_to_grid(boardString,3,3)
    # are we finished?
    if (count_moves_available(board) == 0):
        return boardString
    # if empty board then we play in a corner
    if (empty_board(board)):
        #print("go centre first")
        board[1][1] = 'X'
    elif (centre_free(board)):
        #print("go centre")
        board[1][1] = 'X'
    elif (move_number(board,'X') < 2):
        #choose a corner
        board = any_corner(board)
    elif (can_win(board)):
        board = win_game(board)
        #print("win")
    elif (need_to_block(board)):
        board = block(board)
        #print("block")
    elif (centre_free(board)):
        board[1][1] = 'X'
        #print("go centre 2")        
    elif (killer_move_exists(board, 'X')):
        board = make_killer_move(board, 'X','X')
        #print("killer for the win")
    elif (killer_move_exists(board, 'O')):
        board = make_killer_move(board, 'O','X')
        #print("killer for the block")
        """ late mod - try to make a twin """
    elif (open_single_exists(board, 'X')):
        board = make_a_twin(board,'X')
    else:
        board = make_random_move(board)
        #print("random")

    
    newBoard = grid_to_string(board)
    return newBoard