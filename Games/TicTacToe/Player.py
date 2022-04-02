from Board import Board
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, turnNum: int) -> None:
        self.turnPiece = "X" if turnNum == 0 else "O"
    
    @abstractmethod
    def getMove(self):
        pass

    @abstractmethod
    def makeMove(self):
        pass