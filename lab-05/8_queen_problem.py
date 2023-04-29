def check_if_valid(chessboard, row, col):
    # check for row and column
    for i in range(8):
        if chessboard[row][i] == 1 or chessboard[i][col] == 1:
            return False

    # check for digonal
    for i in range(len(chessboard)):
        for j in range(len(chessboard)):
            if (i+j == row+col) or (i-j == row-col):
                if chessboard[i][j] == 1:
                    return False

    return True


def place_queen_onboard(chessboard, col):
    if col >= 8:
        return True

    for row in range(len(chessboard)):
        if check_if_valid(chessboard, row, col):
            chessboard[row][col] = 1

            if place_queen_onboard(chessboard, col+1):
                return True
#  this used for back tracking,if the recursion call is unable to place queen in the next column we need
# to bacl track to previous column and reset the queen in a different row
            chessboard[row][col] = 0
    return False


chessboard = [[0 for i in range(8)] for j in range(8)]

if place_queen_onboard(chessboard, 0):
    for rows in chessboard:
        print(rows)

else:
    print("not able to place queens on board")
