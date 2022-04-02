#input: player, column, row
#Field: 6 by 7, outer rim filled by 'O' - bound square, 'B' - Blank square, 'R' - p1, 'Y' - p2
import client
import threading

field = [[]];

def mPros(message):
    t1 = message.index(";");
    message = message[t1 + 1::]
    t2 = message.index(";");
    return message[t2 + 1::]
def newGame():
    global field
    for col in range (0, 9):
        for row in range (0, 8):
            if (col < 1 or col > 7 or row < 1 or row > 6):
                field[col][row] = 'O'
            else:
                field[col][row] ='B'
    return (False)

#Check , if requested field is blank, proceed, otherwise return error. Main will recieve output from funcs in
#form of [player who's turn it is(0 or 1), error check]
#'R' = 0, 'Y' = 1
def inputCheck(player, column, row):
    if field[column][row] == 'B' and field[column][row - 1] != 'B':
        return True
    else:
        return(False)

def nextTurn(player, column, row):
    global field
    if not player:
        field[column][row] = 'R'
    else:
        field[column][row] = 'Y'

    return(not player)

def checkWins(row, column):
    return False
    #kai will semd

def main():
    player = newGame()
    #field, row, column
    #checkWins
    #false or true, 0/1
    win = False

    while (not win):
        inPlayer, row, col = jack input

        while(not inputCheck(player, row, col) or inPlayer != player):
            if inPlayer != player:
                #send not your turn message
            else:
                #send invalid move message
            #collect new inputs

        player = nextTurn(player, row, col)
        checkWins(row, col)









