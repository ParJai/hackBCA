
field = [["O" for i in range(8)] for j in range(9)];

def checkWins(col, row):
    global field

    numUp = 0
    numDown = 0
    numLeft = 0
    numRight = 0

    var = field[col][row]

    if var == "B" or var == "O":
        return False

    #up direction
    for i in range(row + 1, 7):
        if field[col][i] == var:
            numUp += 1
        else:
            break

    #down direction
    for i in range(row - 1, 0, -1):
        if field[col][i] == var:
            numDown += 1
        else:
            break

    #check up + down
    if numUp + numDown >= 3:
        if field[col][row] == "R":
            return [True, False]
        else:
            return [True, True]

    #left direction
    for i in range(col - 1, 0, -1):
        if field[i][row] == var:
            numLeft += 1
        else:
            break

    #right direction
    for i in range(col + 1, 8):
        if field[i][row] == var:
            numRight += 1
        else:
            break

    #check left + right
    if numLeft + numRight >= 3:
        if field[col][row] == "R":
            return [True, False]
        else:
            return [True, True]


    diagonal1TopLeft = 0
    diagonal1BottomRight = 0

    tempCol = col - 1
    tempRow = row + 1

    while tempCol > 0 and tempRow < 7:
        if field[tempCol][tempRow] == var:
            diagonal1TopLeft += 1
            tempCol -= 1
            tempRow += 1
        else:
            break

    tempCol = col + 1
    tempRow = row - 1

    while tempCol < 8 and tempRow > 0:
        if field[tempCol][tempRow] == var:
            diagonal1BottomRight += 1
            tempCol += 1
            tempRow -= 1
        else:
            break

    # check diagonal1
    if diagonal1TopLeft + diagonal1BottomRight >= 3:
        if field[col][row] == "R":
            return [True, False]
        else:
            return [True, True]


    diagonal2TopRight = 0
    diagonal2BottomLeft = 0

    tempCol = col + 1
    tempRow = row + 1

    while tempCol < 8 and tempRow < 7:
        if field[tempCol][tempRow] == var:
            diagonal2TopRight += 1
            tempCol += 1
            tempRow += 1
        else:
            break

    tempCol = col - 1
    tempRow = row - 1

    while tempCol > 0 and tempRow > 0:
        if field[tempCol][tempRow] == var:
            diagonal2BottomLeft += 1
            tempCol -= 1
            tempRow -= 1
        else:
            break

    # check diagonal2
    if diagonal2TopRight + diagonal2BottomLeft >= 3:
        if field[col][row] == "R":
            return [True, False]
        else:
            return [True, True]

    return False

for col in range(1, 8):
    for row in range(1, 7):
        field[col][row] = 'B'

field[4][1] = "Y"
field[5][2] = "Y"
field[6][3] = "Y"
field[7][4] = "Y"

print(checkWins(7, 4))















