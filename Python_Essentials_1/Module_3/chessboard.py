EMPTY = "-"
ROOK = "ROOK"
PAWN = "PAWN"
KING = "KING"
QUEEN = "QUEEN"
KNIGHT = "KNIGHT"
BISHOP = "BISHOP"

board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0], board[0][7], board[7][0], board[7][7] = ROOK, ROOK, ROOK, ROOK
board[0][1], board[0][6], board[7][1], board[7][6] = KNIGHT, KNIGHT, KNIGHT, KNIGHT
board[0][2], board[0][5], board[7][2], board[7][5] = BISHOP, BISHOP, BISHOP, BISHOP
board[0][3], board[7][3] = KING, KING
board[0][4], board[7][4] = QUEEN, QUEEN
board[1][:] = [PAWN for i in range(8)]
board[6][:] = [PAWN for i in range(8)]
  

for row in board:
    print(row)