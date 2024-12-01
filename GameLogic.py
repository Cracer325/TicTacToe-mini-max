size = int(input("Enter size (size 3 recommended): "))
board = [" " for _ in range(size*size)]
current_player = "X"


def display_board():
    """Displays the current state of the board."""
    print("\n")
    for i in range(size):
        print(" | ".join(board[i * size:(i + 1) * size]))
        if i < size-1:
            print("-" * (size*4))
    print("\n")



def is_winner(current_state, player):
    """Checks if the current player has won."""
    # Check rows
    for r in range(size):
        if all(current_state[r * size + c] == player for c in range(size)):
            return True

    # Check columns
    for c in range(size):
        if all(current_state[r * size + c] == player for r in range(size)):
            return True

    # Check diagonals
    if all(current_state[i * (size + 1)] == player for i in range(size)):
        return True

    if all(current_state[(i + 1) * (size - 1)] == player for i in range(size) if (i + 1) * (size - 1) < len(current_state)):
        return True

    return False

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
    if position < 0 or position >= size*size or board[position] != " ":
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

