from Board import Board
from Human import Human
from AI import AI
from random import randint

class Game:
    def coinFlip(self): #Flip a coin
        return randint(0,1)

    def __init__(self, boardSize : int, p1Human : bool, p2Human : bool) -> None:
        self.board = Board(boardSize)
        p1Turn = self.coinFlip()
        self.p1 = Human(self.board, p1Turn) if p1Human else AI(self.board, p1Turn)
        self.p2 = Human(self.board, 1 ^ p1Turn) if p2Human else AI(self.board, 1 ^ p1Turn)
        self.turn = 0
    
    def start_game_loop(self) -> str:
        boardCheck = 0
        while len(self.board.possibleMoves) > 0 and boardCheck == 0:
            move = self.p1.getMove() if self.p1.turnNum == self.turn else self.p2.getMove()
            char = self.p1.turnPiece if self.p1.turnNum == self.turn else self.p2.turnPiece
            if move not in self.board.possibleMoves:
                print("Invalid move.")
                continue
            self.board.addMove(move, char)
            self.turn ^= 1
            self.board.printBoard()
            print()
            boardCheck = self.board.checkBoard()

        if len(self.board.possibleMoves) == 0:
            return "Tie"
        elif boardCheck == self.p1.turnPiece:
            return "Win"
        else:
            return "Loss"