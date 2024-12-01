from GameLogic import display_board, turn, board, move, current_player, size
from MiniMax import best_move, worst_move
print("Welcome to Tic Tac Toe!")
user_player = int(input("Who do you want to play as? (1 for X, 0 for O): "))
display_board()
while True:
    try:
        if turn() == (user_player+1)%2:
            temp_board = [i for i in board]
            user_input = best_move(temp_board, (user_player+1)%2)
        else:
            user_input = int(input(f"Player {current_player}, enter your move (1-{size*size}): "))

        move(user_input)
    except ValueError:
        print("Please enter a valid number.")