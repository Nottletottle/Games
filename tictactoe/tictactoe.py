"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    sumx = 0
    for r in board:
        for c in r:
            if c == X or c == O:
                sumx += 1
    if sumx%2 == 0:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == EMPTY:
                actions.add((r,c))
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardcopy = copy.deepcopy(board)
    if action not in actions(board):
        raise NameError("Not a valid Action")
    boardcopy[action[0]][action[1]] = player(board)
    return boardcopy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    n = len(board)
    for index in indices(n):
        if all(board[r][c] == X for r,c in index):
            return X
        elif all(board[r][c]== O for r,c in index):
            return O
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None):
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board) == X:
        value, action = max_value(board,-math.inf,math.inf)
        return action
    else:
        value, action = min_value(board, -math.inf,math.inf)
        return action


def max_value(board,alpha,beta):
    if terminal(board):
        return utility(board), None
    v = -math.inf
    trans = None
    for action in actions(board):
        hlp, act = min_value(result(board,action),alpha,beta)
        if hlp > v:
            v = hlp
            trans = action
        if hlp >= beta:
            return v, trans
        if hlp > alpha:
            alpha = hlp
    return v, trans

def min_value(board,alpha,beta):
    if terminal(board):
        return utility(board), None
    v = math.inf
    trans = None
    for action in actions(board):
        hlp, act = max_value(result(board,action),alpha,beta)
        if hlp < v:
            v = hlp
            trans = action
        if hlp <= alpha:
            return v, trans
        if hlp < beta:
            beta = hlp
    return v, trans

def indices(n):
    #Rows
    for r in range(n):
        yield [(r, c) for c in range(n)]
    # Columns
    for c in range(n):
        yield [(r, c) for r in range(n)]
    # Diagonal top left to bottom right
    yield [(i, i) for i in range(n)]
    # Diagonal top right to bottom left
    yield [(i, n - 1 - i) for i in range(n)]
