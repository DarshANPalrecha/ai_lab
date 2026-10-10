
# Tic-Tac-Toe Game in Python

def print_board(board):
    print()
    for i in range(3):
        print(" | ".join(board[i * 3:(i + 1) * 3]))
        if i < 2:
            print("--+---+--")
    print()


def check_winner(board, player):
    win_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]

    for a, b, c in win_positions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def play_game():
    board = [" "] * 9
    player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print("Enter positions from 1 to 9.")

    while True:
        print_board(board)

        try:
            position = int(input(f"Player {player}, enter position (1-9): "))
        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        if position < 1 or position > 9:
            print("Choose a position between 1 and 9.")
            continue

        index = position - 1

        if board[index] != " ":
            print("Position already occupied! Try again.")
            continue

        board[index] = player

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if " " not in board:
            print_board(board)
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"


play_game()
