
def checkWins(board, row, col):
    numUp = 0
    numDown = 0
    numLeft = 0
    numRight = 0

    var = board[row][col]

    #up direction
    for i in range(row + 1, 7):
        if board[col][i] == var:
            numUp += 1
        else:
            break

    #down direction
    for i in range(row - 1, 0, -1):
        if board[col][i] == var:
            numDown += 1
        else:
            break

    #check up + down
    if numUp + numDown >= 4:
        if board[col][row] == "R":
            return [True, 0]
        else:
            return [True, 1]

    #left direction
    for i in range(col - 1, 0, -1):
        if board[i][row] == var:
            numLeft += 1
        else:
            break

    #right direction
    for i in range(col + 1, 8):
        if board[i][row] == var:
            numRight += 1
        else:
            break

    #check left + right
    if numLeft + numRight >= 4:
        if board[col][row] == "R":
            return [True, 0]
        else:
            return [True, 1]


    diagonal1TopLeft = 0
    diagonal1BottomRight = 0

    tempCol = col - 1
    tempRow = row + 1

    while tempCol > 0 and tempRow < 7:
        if board[tempCol][tempRow] == var:
            diagonal1TopLeft += 1
            tempCol -= 1
            tempRow += 1
        else:
            break

    tempCol = col + 1
    tempRow = row - 1

    while tempCol < 8 and tempRow > 0:
        if board[tempCol][tempRow] == var:
            diagonal1BottomRight += 1
            tempCol += 1
            tempRow -= 1
        else:
            break

    # check diagonal1
    if diagonal1TopLeft + diagonal1BottomRight >= 4:
        if board[col][row] == "R":
            return [True, 0]
        else:
            return [True, 1]


    diagonal2TopRight = 0
    diagonal2BottomLeft = 0

    tempCol = col + 1
    tempRow = row + 1

    while tempCol < 8 and tempRow < 7:
        if board[tempCol][tempRow] == var:
            diagonal2TopRight += 1
            tempCol += 1
            tempRow += 1
        else:
            break

    tempCol = col - 1
    tempRow = row - 1

    while tempCol > 0 and tempRow > 0:
        if board[tempCol][tempRow] == var:
            diagonal2BottomLeft += 1
            tempCol -= 1
            tempRow -= 1
        else:
            break

    # check diagonal2
    if diagonal2TopRight + diagonal2BottomLeft >= 4:
        if board[col][row] == "R":
            return [True, 0]
        else:
            return [True, 1]

    return False















