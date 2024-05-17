# CODSOFT_TASKNO2

# Tic-Tac-Toe AI Agent

This project implements an AI agent that plays the classic game of Tic-Tac-Toe against a human player. The AI uses the Min-Max algorithm with Alpha-Beta Pruning to make optimal moves, making it unbeatable. This project demonstrates concepts from game theory and basic search algorithms.

## Features

- Human vs AI gameplay.
- AI uses the Min-Max algorithm with Alpha-Beta Pruning to ensure optimal moves.
- Unbeatable AI agent.

## Getting Started

These instructions will help you set up and run the Tic-Tac-Toe AI agent on your local machine.

## Prerequisites

- Python 3.x
- Numpy (optional, but code imports numpy)

## Usage

When you run the script, you will be prompted to enter your move by specifying the row and column numbers. The AI will then make its move. The game continues until there is a winner or the board is full.

Example interaction:

Welcome to Tic-Tac-Toe! You are playing as 'O'.
  |   |  
-----
  |   |  
-----
  |   |  
Enter row (0, 1, 2): 0
Enter column (0, 1, 2): 0
O |   |  
-----
  |   |  
-----
  |   |  
AI's move:
O |   |  
-----
  | X |  
-----
  |   |  
Enter row (0, 1, 2): 


## Code Explanation

The core of the AI agent is implemented using the Min-Max algorithm with Alpha-Beta Pruning to optimize the decision-making process. The AI is designed to always make the optimal move, ensuring it is unbeatable.

## Key Functions:

- print_board(board): Prints the current state of the Tic-Tac-Toe board.
- is_terminal_state(board): Checks if the current board state is a terminal state (win, lose, or tie).
- evaluate_board(board): Evaluates the score of the board. Returns 10 if 'X' wins, -10 if 'O' wins, and 0 for a tie.
- minmax(board, depth, is_maximizer, alpha, beta): Implements the Min-Max algorithm with Alpha-Beta Pruning.
- make_ai_move(board): Determines and makes the optimal move for the AI.
- play_tic_tac_toe(): Manages the game loop, alternating between human and AI moves.

## Customization

You can customize the AI by modifying the evaluation function or by changing the rules for the game. For example, you can adjust the board size or the winning conditions.

## Output
![Screenshot 2024-05-17 172130](https://github.com/omaimajameel11/CODSOFT_TASKNO2/assets/167120544/e7898ba8-e2ba-4e23-bdf4-ac34c939b5f0)

