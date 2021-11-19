# SUDOKU VALIDATION

# Sudoku is a number-placing puzzle played on a 9x9 board.
# The player has to fill the board in a very specific way:
# - Each row of the board must contain all digits from 0 to
# 9 (the order doesn't matter).
# - Each column of the board must contain all digits from 0 to
# 9 (again, the order doesn't matter).
# - Each of the nine 3x3 "tiles" (or "sub-squares") of the table
# must contain all digits from 0 to 9.

# Task. Write a program which:
# - Reads 9 rows of the Sudoku, each containing 9 digits (check
# carefully if the data entered are valid).
# - Outputs Yes if the Sudoku is valid, and No otherwise.

# Test
test_data = [
"""
295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672
""",
"""
195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671
"""
]

expected_output = ["Yes", "No"]


def check_numbers_in_row(board_sample: list):
    number_of_row = 9
    for n in range(number_of_row):
        row = board_sample[n]
        if str(n + 1) in row:
            continue
        else:
            is_valid = "No"
            return is_valid
    else:
        is_valid = "Yes"
        return is_valid


def check_numbers_in_col(board_sample: list):
    number_of_col = 9
    for n in range(number_of_col):
        col = [number for number in [board_sample[row][n] for row in range(number_of_col)]]
        if str(n + 1) in col:
            continue
        else:
            is_valid = "No"
            return is_valid
    else:
        is_valid = "Yes"
        return is_valid


def check_numbers_in_tile(tile: list):
    numbers_in_tile = ""
    for row in tile:
        for number in row:
            numbers_in_tile += str(number)
    for n in range(9):
        if str(n + 1) in numbers_in_tile:
            continue
        else:
            is_valid = "No"
            return is_valid
    else:
        is_valid = "Yes"
        return is_valid


def valid_sudoku(board):
    # Cleaning string board input
    board = board.strip()
    board_rows = board.split("\n")

    # Preparing board in list format
    board_list = []
    for row in board_rows:
        if row.isdigit():
            board_list.append([number for number in row])
        else:
            print("No. The sudoku board must contain only digits.")
            return

    # Checking 9 rows
    is_valid = check_numbers_in_row(board_list)
    if is_valid == "No":
        print(is_valid)
        return

    # Checking 9 columns
    is_valid = check_numbers_in_col(board_list)
    if is_valid == "No":
        print(is_valid)
        return

    # Generating tiles 3x3
    for row in range(3):
        for col in range(0, 9, 3):
            tile = [board_list[3*row][col : col + 3],
                    board_list[3*row + 1][col : col + 3],
                    board_list[3*row + 2][col : col + 3],
            ]

            # Checking tiles
            is_valid = check_numbers_in_tile(tile)
            if is_valid == "No":
                print(is_valid)
                return

    # Board passes all tests
    else:
        print("Yes")
        return


if __name__ == "__main__":
    for board in test_data:
        print(board)
        result = valid_sudoku(board)