# X,1 - max, O,0 - min
from GameLogic import is_draw, is_winner
#The Minimax Algo:
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
def action(current_state):
    moves = []
    for i in range(len(current_state)):
        if  current_state[i] == " ":
            moves.append(i)

    return moves

def result(current_state, player, current_move ):
    new_board = [i for i in current_state]
    new_board[current_move] = "X" if player == 1 else "O"
    return new_board

def minimax(current_state, player, alpha, beta):
    if terminal(current_state):
        return state(current_state)
    moves = action(current_state)
    if player == 1:
        value = float('-inf')
        for current_move in moves:
            value =  max(value, minimax(result(current_state, player, current_move), 0, alpha, beta))
            alpha = max(alpha, value)
            if value >= beta:
                break #Snip
        return value
    if player == 0:
        value = float('inf')
        for current_move in moves:
            value =  min(value, minimax(result(current_state, player, current_move), 1, alpha, beta))
            beta = min(beta, value)
            if value <= alpha:
                break #Snip
        return value

def best_move(current_state, player):
    best = 0
    best_move_value = float('-inf')
    for cur_move in action(current_state):
        cur_val = minimax(result(current_state, player, cur_move), (player+1) %2, float('-inf'), float('inf'))
        if player == 0:
            cur_val *= -1
        if best_move_value < cur_val:
            best = cur_move
            best_move_value = cur_val
    return best+1

def worst_move(current_state, player):
    worst = 0
    worst_move_value = float('inf')
    for cur_move in action(current_state):
        cur_val = minimax(result(current_state, player, cur_move), (player+1) %2, float('-inf'), float('inf'))
        if player == 0:
            cur_val *= -1
        if worst_move_value > cur_val:
            worst = cur_move
            worst_move_value = cur_val
    return worst+1


