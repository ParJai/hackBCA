#input: player, column, row
#Field: 6 by 7, outer rim filled by 'O' - bound square, 'B' - Blank square, 'R' - p1, 'Y' - p2
import client
import threading
from time import *
import os
import KaiConnect


class ConnectFour:
    field = [["O" for i in range(8)] for j in range(9)]
    def __init__ (player1, player2):
        self.player1 = player1
        self.player2 = player2

    def error(code):
        if code == 0:
            pass
            #INVALID MOVE
        elif code == 1:
            pass
            #IT ISNT YOUR TURN
        else:
            pass
            #ERROR, please try again

    def waitforinp():
        msg = ""
        while(len(msg) < 1):
            try:
                msg = client.recieve_message()
            except:
                sleep(0.05)
        try:
            t1 = msg.index(";")
            msg = msg[t1 + 1::]
            t2 = msg.index(";")
            msg = msg[t2 + 1]
            t3 = msg.index(";")
            arr = msg[t2 + 1 : t3]
            msg = msg[t3 + 1::]
            t4 = msg.index(";")
            arr.append(msg[t3 + 1: t4])
            arr.append(msg[t4 + 1::])
            return arr
        except:
            error(2)
            return waitforinp()
    

    def newGame():
        global field
        for col in range (1, 8):
            for row in range (1, 7):
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

    

    def main():
        player = newGame()
        #field, row, column
        #checkWins
        #false or true, 0/1
        win = False

        while (not win):
            inp = waitforinp()
            inPlayer, row, col = inp[0], inp[1], inp[2]

            while(not inputCheck(player, row, col) or inPlayer != player):
                if inPlayer != player:
                    error(1)
                else:
                    error(0)
                inp = waitforinp()
                inPlayer, row, col = inp[0], inp[1], inp[2]
            player = nextTurn(player, row, col)
            KaiConnect.checkWins(col, row)









