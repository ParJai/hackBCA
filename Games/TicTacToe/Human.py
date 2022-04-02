from Board import Board

class Human:
    def __init__(self, board : Board, turnNum : int) -> None:
        self.board = board
        self.turnNum = turnNum
        self.turnPiece = "X" if self.turnNum == 0 else "O"
    
    def getMove(self) -> None:
        move = int(input("Possible moves: " + str(self.board.possibleMoves) + "\nEnter your move: "))
        while move not in self.board.possibleMoves:
            move = int(input("Possible moves: " + str(self.board.possibleMoves) + "\nEnter your move: "))
        return move