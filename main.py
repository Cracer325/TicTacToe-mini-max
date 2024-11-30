# X,1 - max, O,0 - min

#The game:
board = [" " for _ in range(9)]
current_player = "X"


def display_board():
    """Displays the current state of the board."""
    print("\n")
    for i in range(3):
        print(" | ".join(board[i * 3:(i + 1) * 3]))
        if i < 2:
            print("-" * 10)
    print("\n")



def is_winner(current_state, player):
    """Checks if the current player has won."""
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    return any(all(current_state[pos] == player for pos in combo) for combo in win_combinations)

def turn():
    """
    Returns the current player's turn.
    1 for "X" and 0 for "O".
    """
    return 1 if current_player == "X" else 0

def is_draw(current_state):
    """Checks if the game is a draw."""
    return " " not in current_state


def move(position):
    """
    Places the current player's marker on the board.

    Args:
        position (int): The position (1-9) where the player wants to play.
    """
    global current_player
    position -= 1  # Convert to 0-based index
    if position < 0 or position >= 9 or board[position] != " ":
        print("Invalid move! Try again.")
        return
    board[position] = current_player
    display_board()


    # Check for a win or draw
    if is_winner(board, current_player):
        print(f"Player {current_player} wins!")
        exit()
    elif is_draw(board):
        print("It's a draw!")
        exit()

    # Switch player
    current_player = "O" if current_player == "X" else "X"


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

def result(current_state, player, current_move):
    new_board = [i for i in current_state]
    new_board[current_move] = "X" if player == 1 else "O"
    return new_board

def minimax(current_state, player):
    if terminal(current_state):
        return state(current_state)
    moves = action(current_state)
    if player == 1:
        value = float('-inf')
        for current_move in moves:
            value =  max(value, minimax(result(current_state, player, current_move), 0))
        return value
    if player == 0:
        value = float('inf')
        for current_move in moves:
            value =  min(value, minimax(result(current_state, player, current_move), 1))
        return value

def best_move(current_state, player):
    best = 0
    best_move_value = float('-inf')
    for cur_move in action(current_state):
        cur_val = minimax(result(current_state, player, cur_move), (player+1) %2)
        if player == 0:
            cur_val *= -1
        if best_move_value < cur_val:
            best = cur_move
            best_move_value = cur_val
    return best+1



print("Welcome to Tic Tac Toe!")
user_player = int(input("Who do you want to play as? (1 for X, 0 for O): "))
display_board()
while True:
    try:
        if turn() == (user_player+1)%2:
            print("Bot thinking...")
            temp_board = [i for i in board]
            user_input = best_move(temp_board, (user_player+1)%2)
        else:
            user_input = int(input(f"Player {current_player}, enter your move (1-9): "))
        move(user_input)
    except ValueError:
        print("Please enter a valid number.")

