import numpy as np

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if the current state of the board is a terminal state
def is_terminal_state(board):
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
    
    # Check for tie
    if all(cell != " " for row in board for cell in row):
        return True
    
    return False

# Function to evaluate the score of the current board state
def evaluate_board(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return 10 if row[0] == "X" else -10
    
    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return 10 if board[0][col] == "X" else -10
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return 10 if board[0][0] == "X" else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return 10 if board[0][2] == "X" else -10
    
    # If no winner
    return 0

# Function to implement Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizer, alpha, beta):
    if is_terminal_state(board):
        return evaluate_board(board)
    
    if is_maximizer:
        max_eval = float("-inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval_score = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval_score)
                    alpha = max(alpha, eval_score)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval_score = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval_score)
                    beta = min(beta, eval_score)
                    if beta <= alpha:
                        break
        return min_eval

# Function to make the AI move using Minimax algorithm with Alpha-Beta Pruning
def make_ai_move(board):
    best_eval = float("-inf")
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                eval_score = minimax(board, 0, False, float("-inf"), float("inf"))
                board[i][j] = " "
                if eval_score > best_eval:
                    best_eval = eval_score
                    best_move = (i, j)
    board[best_move[0]][best_move[1]] = "X"

# Function to play Tic-Tac-Toe
def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You are playing as 'O'.")
    print_board(board)
    
    while not is_terminal_state(board):
        # Human player's move
        while True:
            try:
                row = int(input("Enter row (0, 1, 2): "))
                col = int(input("Enter column (0, 1, 2): "))
                if board[row][col] == " ":
                    board[row][col] = "O"
                    break
                else:
                    print("That cell is already occupied. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid row and column.")

        print_board(board)
        
        # Check if human player wins or if it's a tie
        if is_terminal_state(board):
            break

        # AI player's move
        make_ai_move(board)
        print("AI's move:")
        print_board(board)

        # Check if AI wins or if it's a tie
        if is_terminal_state(board):
            break

    # Game result
    if evaluate_board(board) == 10:
        print("Congratulations! You win!")
    elif evaluate_board(board) == -10:
        print("Sorry, you lose. The AI wins!")
    else:
        print("It's a tie!")

# Start the game
play_tic_tac_toe()