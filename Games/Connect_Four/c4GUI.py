import pygame
import threading

class circle:
    def __init__(self, x, y, window):
        self.x=x
        self.y=y
        self.window = window
        self.color = (12, 50, 97)

    def draw(self):
        pygame.draw.circle(self.window, self.color, (self.x, self.y), 30)
class Connect4:
    def __init__(self, window, clock, client):
        self.window = window

        self.clock = clock

        self.run = True

        self.client = client
        
        self.circles = []
        self.cir = {}
        self.cols = []

        self.row = 0

        self.prevcol = -1

        self.field = [["O" for i in range(8)] for j in range(9)]
        self.player = self.newGame()

        self.loadCircles()
        
       
        msg = ""
        sending = threading.Thread(target = self.client.send_message, args = (msg,), daemon = True)
        sending.start()
        recieving = threading.Thread(target = self.client.recieve_message, args = (), daemon = True)
        recieving.start()

        while self.run:
            if len(self.client.recievingQueue) != 0:
                self.placePiece(self.client.recievingQueue[0][1])
                self.player = self.nextTurn(self.player, 7-(7-len(self.cols[self.client.recievingQueue[0][1]])), self.client.recievingQueue[0][1])
                print((self.client.recievingQueue[0][0], self.client.recievingQueue[0][1]))
                if self.checkWin(7-(7-len(self.cols[self.client.recievingQueue[0][1]])), self.client.recievingQueue[0][1]):
                    print('Player 1 Won' if self.player == 2 else 'Player 2 Won')
                    self.run = False
                del self.client.recievingQueue[0]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if 200 < mx < 800:
                        if self.cols[(mx-150)//100] != []:
                            print("\n".join([", ".join(i) for i in self.field]))
                            self.placePiece((mx-150)//100)
                            self.client.messageQueue.append(str((mx-200)//100))
                            self.player = self.nextTurn(self.player, (mx-150)//100, len(self.cols[(mx-150)//100]))
                            print(self.checkWin(7-(7-len(self.cols[(mx-150)//100])), (mx-150)//100))
                            if self.checkWin(7-(7-len(self.cols[(mx-150)//100])), (mx-150)//100):
                                print('Player 2 Won' if self.player == False else 'Player 1 Won')
                                self.run = False
            self.draw()
    
    def draw(self):
        mx, my = pygame.mouse.get_pos()
        self.window.fill((231, 173, 153))
        pygame.draw.rect(self.window, (0,0,255), (150, 0, 700, 600))
        for i in self.circles: i.draw()
        if 200 < mx < 800:
            if self.prevcol != (mx-150)//100:
                for i in self.cols[(mx-150)//100]:
                    i.color = (29, 94, 173)
                if self.prevcol != -1:
                    for i in self.cols[self.prevcol]:
                        i.color = (12, 50, 97)
                self.prevcol = (mx-150)//100
        else:
            if self.prevcol != -1:
                for i in self.cols[self.prevcol]:
                    i.color = (12, 50, 97)
                self.prevcol=-1
        pygame.display.update()

    def loadCircles(self):
        col = 0
        row = 0
        for x in range(200, 851, 100):
            tempcol = []
            for y in range(50, 601, 100):
                circ = circle(x, y, self.window)
                self.circles.append(circ)
                self.cir[f'{col},{row}'] = circ
                tempcol.append(circ)
                row += 1
            row = 0
            col += 1
            tempcol.reverse()
            self.cols.append(tempcol)

    def newGame(self):
        for col in range (1, 8):
            for row in range (1, 7):
                self.field[col][row] ='B'
        return (False)

    def nextTurn(self, player, column, row):
        row += 1
        column += 1
        if not player:
            self.field[column][row] = 'R'
        else:
            self.field[column][row] = 'Y'

        return(not player)
    
    def placePiece(self, col):

        self.row = len(self.cols[col])
        if not self.player:
            self.cols[col][0].color = (255,0,0)
        else:
            self.cols[col][0].color = (255, 255, 0)
        del self.cols[col][0]
    
    def checkWin(self, row, col):
        row += 1
        col += 1
        global field

        numUp = 0
        numDown = 0
        numLeft = 0
        numRight = 0

        var = self.field[col][row]

        if var == "B" or var == "O":
            return False

        #up direction
        for i in range(row + 1, 7):
            if self.field[col][i] == var:
               numUp += 1
            else:
                break

        #down direction
        for i in range(row - 1, 0, -1):
            if self.field[col][i] == var:
                numDown += 1
            else:
                break

        #check up + down
        if numUp + numDown >= 3:
            if self.field[col][row] == "R":
                return [True, False]
            else:
                return [True, True]

        #left direction
        for i in range(col - 1, 0, -1):
            if self.field[i][row] == var:
                numLeft += 1
            else:
                break

        #right direction
        for i in range(col + 1, 8):
            if self.field[i][row] == var:
                numRight += 1
            else:
                break

        #check left + right
        if numLeft + numRight >= 3:
            if self.field[col][row] == "R":
                return [True, False]
            else:
                return [True, True]


        diagonal1TopLeft = 0
        diagonal1BottomRight = 0

        tempCol = col - 1
        tempRow = row + 1

        while tempCol > 0 and tempRow < 7:
            if self.field[tempCol][tempRow] == var:
                diagonal1TopLeft += 1
                tempCol -= 1
                tempRow += 1
            else:
                break

        tempCol = col + 1
        tempRow = row - 1

        while tempCol < 8 and tempRow > 0:
            if self.field[tempCol][tempRow] == var:
                diagonal1BottomRight += 1
                tempCol += 1
                tempRow -= 1
            else:
                break

        # check diagonal1
        if diagonal1TopLeft + diagonal1BottomRight >= 3:
            if self.field[col][row] == "R":
                return [True, False]
            else:
                return [True, True]
        diagonal2TopRight = 0
        diagonal2BottomLeft = 0

        tempCol = col + 1
        tempRow = row + 1

        while tempCol < 8 and tempRow < 7:
            if self.field[tempCol][tempRow] == var:
                diagonal2TopRight += 1
                tempCol += 1
                tempRow += 1
            else:
                break

        tempCol = col - 1
        tempRow = row - 1

        while tempCol > 0 and tempRow > 0:
            if self.field[tempCol][tempRow] == var:
                diagonal2BottomLeft += 1
                tempCol -= 1
                tempRow -= 1
            else:
                break

        # check diagonal2
        if diagonal2TopRight + diagonal2BottomLeft >= 3:
            if self.field[col][row] == "R":
                return [True, False]
            else:
                return [True, True]

        return False
        
WIDTH = 1000
HEIGHT = 700

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.font.init()

Connect4(window, clock)