# X,1 - max, O,0 - min
from functools import lru_cache

from GameLogic import is_draw, is_winner, size
#The Minimax Algo:


#Removed as it offered minimal help and made it in fact longer because of all the additional checks
# def heuristic(current_state, player, move):
#     score = 0
#     if is_winner(result(current_state, move, player), player):
#         score += 10
#     if is_winner(result(current_state, move, (player+1)%2), (player+1)%2): #the move blocks if when it's placed by the opponent he won
#         score += 5
#     return score


def state(current_state):
    if is_winner(current_state,'O'):
        return -1
    if is_winner(current_state, 'X'):
        return 1
    if is_draw(current_state):
        return 0
    return None
def terminal(current_state):
    return is_winner(current_state,'O') or is_winner(current_state,'X') or is_draw(current_state)
def action(current_state, player):
    moves = []
    for i in range(len(current_state)):
        if  current_state[i] == " ":
            moves.append(i)
    #I know I accidentally made the sorted(moves) in ascending rather than descending, I fixed it however
    #it didn't help the fundamental flaw in the heuristic function
    return moves

def result(current_state, player, current_move ):
    new_board = [i for i in current_state]
    new_board[current_move] = "X" if player == 1 else "O"
    return new_board
@lru_cache()
def minimax(current_state, player, alpha, beta):
    current_state = list(current_state)
    if terminal(current_state):
        return state(current_state)
    moves = action(current_state, player)
    if player == 1:
        value = float('-inf')
        for current_move in moves:
            value =  max(value, minimax(tuple(result(current_state, player, current_move)), 0, alpha, beta))
            alpha = max(alpha, value)
            if value >= beta:
                break #Snip
        return value
    if player == 0:
        value = float('inf')
        for current_move in moves:
            value =  min(value, minimax(tuple(result(current_state, player, current_move)), 1, alpha, beta))
            beta = min(beta, value)
            if value <= alpha:
                break #Snip
        return value

def best_move(current_state, player):
    best = 0
    best_move_value = float('-inf')
    for cur_move in action(current_state, player):
        cur_val = minimax(tuple(result(current_state, player, cur_move)), (player+1) %2, float('-inf'), float('inf'))
        if player == 0:
            cur_val *= -1
        if best_move_value < cur_val:
            best = cur_move
            best_move_value = cur_val
    return best+1

def worst_move(current_state, player):
    worst = 0
    worst_move_value = float('inf')
    for cur_move in action(current_state, player):
        cur_val = minimax(tuple(result(current_state, player, cur_move)), (player+1) %2, float('-inf'), float('inf'))
        if player == 0:
            cur_val *= -1
        if worst_move_value > cur_val:
            worst = cur_move
            worst_move_value = cur_val
    return worst+1


