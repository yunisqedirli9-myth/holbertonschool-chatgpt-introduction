#!/usr/bin/env python3

def print_board(board):
    """Display the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    """
    Check if there's a winner on the board.
    Returns True if a winner is found, False otherwise.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def get_valid_input(prompt, valid_values):
    """
    Get valid input from user with error handling.
    
    Args:
        prompt: The message to display to the user
        valid_values: List of valid integer values
        
    Returns:
        A valid integer from valid_values
    """
    while True:
        try:
            value = int(input(prompt))
            if value in valid_values:
                return value
            else:
                print(f"Invalid input! Please enter one of these values: {valid_values}")
        except ValueError:
            print("Invalid input! Please enter a number.")
        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting...")
            exit()


def tic_tac_toe():
    """Main function to run the Tic Tac Toe game."""
    board = [[" "] * 3 for _ in range(3)]
    player = "X"
    moves_made = 0
    
    print("Welcome to Tic Tac Toe!")
    print("Players alternate placing 'X' or 'O' on a 3x3 board.")
    print("Enter row (0, 1, or 2) and column (0, 1, or 2) for your move.")
    print("-" * 50)
    
    while not check_winner(board):
        print_board(board)
        print(f"\nPlayer {player}'s turn")
        
        # Get row input with validation
        row = get_valid_input(
            f"Enter row (0, 1, or 2) for player {player}: ",
            [0, 1, 2]
        )
        
        # Get column input with validation
        col = get_valid_input(
            f"Enter column (0, 1, or 2) for player {player}: ",
            [0, 1, 2]
        )
        
        # Check if spot is already taken
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue
        
        # Place the player's mark
        board[row][col] = player
        moves_made += 1
        
        # Check for winner after move
        if check_winner(board):
            print_board(board)
            print(f"\nPlayer {player} wins!")
            break
        
        # Check for tie (all 9 spots filled)
        if moves_made == 9:
            print_board(board)
            print("\nIt's a tie!")
            break
        
        # Switch players
        if player == "X":
            player = "O"
        else:
            player = "X"


if __name__ == "__main__":
    tic_tac_toe()