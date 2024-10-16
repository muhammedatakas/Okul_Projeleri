"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None

second_player_turn = False


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
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    if x_count == o_count:
        return X
    elif x_count == o_count + 1:
        return O
    else:
        return None


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                actions_set.add((i, j))

    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] is not None:
        raise ValueError("Invalid action: Cell is already occupied.")

    copy_board = deepcopy(board)
    current_player = player(board)
    copy_board[action[0]][action[1]] = current_player

    return copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2] != EMPTY:
        return board[2][0]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for sublist in board:
        if None in sublist:
            return False
    return True


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
    Returns the best move for the AI.
    """
    current_player = player(board)
    if current_player == X:
        best_score = float('-inf')
        best_move = None
        for action in actions(board):
            new_board = result(board, action)
            score = min_value(new_board, float('-inf'), float('inf'))
            if score > best_score:
                best_score = score
                best_move = action
        return best_move
    else:
        best_score = float('inf')
        best_move = None
        for action in actions(board):
            new_board = result(board, action)
            score = max_value(new_board, float('-inf'), float('inf'))
            if score < best_score:
                best_score = score
                best_move = action
        return best_move


def max_value(board, alpha, beta):
    if terminal(board):
        return utility(board)
    value = float('-inf')
    for action in actions(board):
        value = max(value, min_value(result(board, action), alpha, beta))
        alpha = max(alpha, value)
        if alpha >= beta:
            break
    return value


def min_value(board, alpha, beta):
    if terminal(board):
        return utility(board)
    value = float('inf')
    for action in actions(board):
        value = min(value, max_value(result(board, action), alpha, beta))
        beta = min(beta, value)
        if beta <= alpha:
            break
    return value