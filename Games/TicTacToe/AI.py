from Board import Board
from copy import deepcopy
from random import choice, randint

class AI:
    def __init__(self, board : Board, turnNum : int) -> None:
        self.board = board
        self.turnNum = turnNum
        self.turnPiece = "X" if turnNum == 0 else "O"

    def isWinningMove(self, row : int, col : int) -> bool: #check if the position is a win move
        tempBoard = deepcopy(self.board)
        tempBoard.addMove(row*self.board.board_size+col, self.turnPiece)
        return tempBoard.checkBoard() == self.turnPiece #check for wins, either return True or False

    def checkForForks(self, row : int, col : int) -> bool: #check if the position is a fork
        tempBoard = deepcopy(self.board) #make a copy of Grid
        tempBoard.addMove(row*self.board.board_size+col, self.turnPiece)
        wins = 0 #keep track of how many win moves there are
        
        for i in self.board.possibleMoves:
                check = self.isWinningMove(i // self.board.board_size, i % self.board.board_size) #check if each position is a potential winning move for temp

                if check == True and self.board.boardArr == 0: #if so, and the position is empty:
                    wins += 1 #mark it as a winning move by adding 1 to wins
        
        return wins >= 2

    def getMove(self) -> int:
        for i in self.board.possibleMoves:
            if self.isWinningMove(i // self.board.board_size, i % self.board.board_size): #if the position is empty, and it is a winning move:
                return i
                
        for k in self.board.possibleMoves:
            if self.isWinningMove(k // self.board.board_size, k % self.board.board_size): #if the position is empty, and it is a winning move:
                return k
        
        for m in self.board.possibleMoves:
            if self.checkForForks(m // self.board.board_size, m % self.board.board_size): #if the position is empty, and it is a fork move:
                return m
                
        for o in self.board.possibleMoves:
            if self.checkForForks(o // self.board.board_size, o % self.board.board_size): #if the position is empty, and it is a winning move:
                return o

        center = self.board.returnCenter()
        if len(center) == 1:
            if 4 in self.board.possibleMoves: #first thing to check afterwards is center
                return 4
        else:
            newAI = AI(center, self.turnNum)
            if 0 in center:
                return newAI.getMove()
        
        corners = [(0, 0), (0, self.board.board_size-1), (self.board.board_size-1, 0), (self.board.board_size-1, self.board.board_size-1)]
        
        randomCorner = choice(corners) #randomly choose a corner
        if randomCorner[0]*self.board.board_size+randomCorner[1] in self.board.possibleMoves:
            return randomCorner[0]*self.board.board_size+randomCorner[1]
        else: #if the center and the corners are already full:
            while True: #just randomly choose a possible item
                row = randint(0, self.board.board_size)
                col = randint(0, self.board.board_size)
            
                if row*self.board.board_size+col in self.board.possibleMoves:
                    return row*self.board.board_size+col