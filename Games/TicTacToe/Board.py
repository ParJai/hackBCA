

class Board:
    def __init__(self, board_size: int) -> None:
        self.board_size = board_size
        self.boardArr = [[0 for i in range(self.board_size)] for i in range(self.board_size)]
        self.possibleMoves = [i for i in range(self.board_size ** 2)]

    def printBoard(self) -> None:
        for row in self.boardArr:
            for char in row:
                print(char, end=" ")
            print()
    
    def getRows(self) -> list:
        return self.boardArr
    
    def getColumns(self) -> list:
        columns = [[] for i in range(self.board_size)]
        for i in range(self.board_size):
            for j in range(self.board_size):
                columns[j].append(self.boardArr[i][j])
        return columns
    
    def getDiagonals(self) -> list:
        n_1_inc = self.board_size + 1
        n_2_inc = self.board_size - 1
        n_1 = 0
        n_2 = n_2_inc
        diagonals = [[], []]
        while n_1 < self.board_size ** 2 and n_2 < self.board_size ** 2:
            n_1_x = n_1 // self.board_size
            n_1_y = n_1 % self.board_size
            n_2_x = n_2 // self.board_size
            n_2_y = n_2 % self.board_size
            diagonals[0].append(self.boardArr[n_1_x][n_1_y])
            diagonals[1].append(self.boardArr[n_2_x][n_2_y])
            n_1 += n_1_inc
            n_2 += n_2_inc
        return diagonals
    
    def checkSubset(self, listOfLists: list) -> str | int:
        same = True
        checkChar = ""
        for i in listOfLists:
            if "B" in i:
                continue
            for j in range(len(i)):
                if j == 0:
                    checkChar = i[j]
                elif i[j] != checkChar:
                    same = False
                    break
            if same:
                return checkChar
        
        return 0
    
    def checkBoard(self) -> str | int:
        rowsChar = self.checkSubset(self.getRows())
        columnsChar = self.checkSubset(self.getColumns())
        diagonalsChar = self.checkSubset(self.getDiagonals())
        if rowsChar == "X" or rowsChar == "O":
            return rowsChar
        elif columnsChar == "X" or columnsChar == "O":
            return columnsChar
        elif diagonalsChar == "X" or diagonalsChar == "O":
            return diagonalsChar
        return 0

    def returnCenter(self) -> list:
        center = []
        for i in range(self.board_size):
            for j in range(self.board_size):
                if i != 0 and j != 0 and i != self.board_size-1 and j != self.board_size-1:
                    center.append(self.boardArr[i][j])
        return center
    
    def addMove(self, pos: int, char: str) -> None:
        self.boardArr[pos // self.board_size][pos % self.board_size] = char
        self.possibleMoves.remove(pos)
    
    def getBoardSize(self):
        return self.board_size