# SCENARIO
# Your task is to write a simple program which
# pretends to play tic-tac-toe with the user.

# Assumptions:
# 1. The computer play the game using "X".
# 2. The user play the game using "O".
# 3. First move belong to the computer. It always
# puts its first X in the middle of the board.
# 4. All the square are numbered starting with 1.
# 5. The user inputs their move entering the number
# of the square (from 1 to 9). It cannot point to a
# field which is already occupied.
# 6. The program checks if the game is over.

# Requeriments:
# The board should be stored as a three-element list.
# The squares are accessed using: board[roe][column]

from random import randrange


board = [
    [str(3*i + j) for j in range(1, 4)] for i in range(3)
    ]


board_drawing = """
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   5   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
"""

game_continue = True


def display_board(board_drawing):
    """The function accepts one parameter containing the 
    board's current status and prints it out to the console."""
    print(board_drawing)


def make_list_of_free_fields(board):
    """The function browses the board and builds a list of all the
    free squares; the list consists of tuples, while each tuple is
    a pair of row and column numbers."""
    free_squares = [
        (i, j) for i, row in enumerate(board) 
        for j, digit in enumerate(row)
        if (digit != "X") and (digit != "O") 
        ]
    return free_squares


def enter_move(board):
    """The function accepts the board's current status, 
    asks the user about their move, checks the input, and updates
    the board according to the user's decision."""
    global board_drawing
    is_valid_move = False

    while is_valid_move != True:
        try:
            user_move = int(input("Enter your move: "))
        except:
            print("Hey! You must enter a number between 0 and 9.")
            continue
        if (user_move <= 0) or (user_move > 9):
            print("Your move must be between 1 and 9.")
        else:
            free_squares = make_list_of_free_fields(board)
            for square in free_squares:
                i, j = square
                if board[i][j] != str(user_move):
                    continue
                else:
                    board[i][j] = "O"
                    board_drawing = board_drawing.replace(str(user_move), "O")
                    display_board(board_drawing)
                    is_valid_move = True


def draw_move(board):
    """The function draws the computer's move and updates the board."""
    global board_drawing
    is_valid_move = False

    while is_valid_move != True:
        computer_move = randrange(1, 10)
        free_squares = make_list_of_free_fields(board)
        for square in free_squares:
                i, j = square
                if board[i][j] != str(computer_move):
                    continue
                else:
                    board[i][j] = "X"
                    board_drawing = board_drawing.replace(str(computer_move), "X")
                    display_board(board_drawing)
                    is_valid_move = True


def victory_for(board, sign):
    """The function analyzes the board's status in order to check if 
    the player using 'O's or 'X's has won the game."""
    global game_continue

    free_squares = make_list_of_free_fields(board)
    if free_squares == []:
        print("It's a tie!")
        game_continue = False
        return

    winner = [sign, sign, sign]
    for num in range(3):
        row = board[num]
        col = [board[0][num], board[1][num], board[2][num]]
        if (row == winner) or (col == winner):
            if sign == "O":
                print("You won!")
            elif sign == "X":
                print("You lose!")
            game_continue = False
            return
        else:
            continue

    
print("THE TIC-TAC-TOE GAME")
display_board(board_drawing)
print("Let's begin. I make the first move.")
board_drawing = board_drawing.replace("5", "X")
board[1][1] = "X"
display_board(board_drawing)


while game_continue == True:
    enter_move(board)
    victory_for(board, "O")
    if not game_continue:
        break
    draw_move(board)
    victory_for(board, "X")