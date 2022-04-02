import pygame
import threading

pygame.init()

board = [3, 4, 5]

def write(screen, text, font, text_size, center, color):
    text_font = pygame.font.Font(font, text_size)
    text_to_write = text_font.render(text, True, color)
    text_rect = text_to_write.get_rect()
    text_rect.center = center
    screen.blit(text_to_write, text_rect)

class Button:
    def __init__(self, window, x, y, size, text):
        self.window = window
        self. x = x
        self.y = y
        self.size = size
        self.text = text

    def draw(self):
        mx, my = pygame.mouse.get_pos()
        pygame.draw.rect(self.window, (219, 223, 172), (self.x, self.y, self.size[0], self.size[1]), 0, 3)
        write(self.window, self.text, 'tahoma.ttf', 40, ((self.x + (self.size[0] / 2), self.y + (self.size[1] / 2))), (0, 0, 0))
        if self.x <= pygame.mouse.get_pos()[0] <= self.x + self.size[0] and self.y <= pygame.mouse.get_pos()[1] <= self.y + self.size[1]:
            pygame.draw.rect(self.window, (255, 255, 255), ((self.x - 5), (self.y - 5), self.size[0] + 10, self.size[1] + 10), 4)


class Stone:
    def __init__(self, window, row, x, y, size):
        self.window = window
        self.row = row
        self.x, self.y = x, y
        self.size = size

    def draw(self):
        pygame.draw.circle(self.window, (255, 255, 255), (self.x, self.y), self.size)

class Nim:
    def __init__(self, window, clock, client):
        self.window = window
        self.clock = clock
        self.mouse_pos = (0, 0)
        self.client = client

        self.board = board
        self.stones = []
        self.rowSelected = 10
        self.removed = 0
        self.submitTurnButton = Button(self.window, 410, 590, (180, 80), 'SUBMIT')
        self.dashboardButton = Button(self.window, 420, 380, (160, 80), 'DASHBOARD')
        self.run = True
        self.turn = True

        self.bgColor = (74, 111, 165)
        margin = 40

        msg = ""
        sending = threading.Thread(target = self.client.send_message, args = (msg,), daemon = True)
        sending.start()
        recieving = threading.Thread(target = self.client.recieve_message, args = (), daemon = True)
        recieving.start()

        for row in range(len(self.board)):
            self.stones.append([])
            row_size = self.board[row]
            maxim = max(self.board)
            size = ((1000 - (maxim + 1) * margin) / maxim) / 2
            if row == 0:
                y = ((700 - (margin * (len(self.board) - 1) + (size * 2) * len(self.board))) / 2 + size) - (margin / 2)
            else:
                y = (self.stones[-2][-1].y + margin + (size * 2)) - (margin / 2)
            for i in range(row_size):
                if i == 0:
                    x = (1000 - (margin * (row_size - 1) + (size * 2) * row_size)) / 2 + size
                else:
                    x = self.stones[-1][-1].x + margin + (size * 2)
                self.stones[-1].append(Stone(self.window, row + 1, x, y, size))

        while self.run:
            if len(self.client.recievingQueue) != 0:
                self.updateBoard(self.client.recievingQueue[0][1].split(";")[0],self.client.recievingQueue[0][1].split(";")[1] )
                print((self.client.recievingQueue[0][0], self.client.recievingQueue[0][1]))
                del self.client.recievingQueue[0]

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.turn: self.mouse_pos = pygame.mouse.get_pos()
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_pos = ()
            
            self.draw()
            if self.checkSubmitClick(self.submitTurnButton):
                self.client.messageQueue.append(f'{self.rowSelected};{self.removed}')
                self.rowSelected, self.removed = 10, 0
                self.turn = False
            
            self.endScreen()

    def draw(self):
        self.window.fill(self.bgColor)
        for row in self.stones:
            for stone in row:
                stone.draw()
            if self.turn:
                if self.rowSelected == 10:
                    self.checkStoneClick(row)
                else:
                    if self.rowSelected == self.stones.index(row):
                        self.checkStoneClick(row)
        self.submitTurnButton.draw()
        pygame.display.update()

    def checkStoneClick(self, row):
        if self.mouse_pos and (len(row) != 0) and (row[0].x - row[0].size) <= self.mouse_pos[0] <= (row[-1].x + row[0].size) and (row[0].y - row[0].size) <= self.mouse_pos[1] <= (row[-1].y + row[0].size):
            self.removeStone(self.stones, self.stones.index(row))
            self.rowSelected = self.stones.index(row)
            self.mouse_pos = ()
    
    def checkExitClick(self, button):
        if self.mouse_pos and button.x <= self.mouse_pos[0] <= button.x + button.size[0] and button.y <= self.mouse_pos[1] <= button.y + button.size[1]:
            self.mouse_pos = ()
            return True
        return False

    def checkSubmitClick(self, button):
        if self.rowSelected != 10:
            if self.mouse_pos and button.x <= self.mouse_pos[0] <= button.x + button.size[0] and button.y <= self.mouse_pos[1] <= button.y + button.size[1]:
                self.mouse_pos = ()
                return True
        return False

    def removeStone(self, stones, row):
        stones[row].pop(-1)
        self.removed += 1
    
    def updateBoard(self, row, removed):
        row = int(row)
        removed = int(removed)
        for i in range(removed):
            self.stones[row].pop(-1)
        self.turn = True

    def checkWin(self, stones):
        total = 0
        for row in stones:
            total += len(row)
        if total == 0: return 'win'
        elif total == 1: return 'lose'
        return False

    def endScreen(self):
        isWin = self.checkWin(self.stones)
        if isWin == 'win': text = 'WON'; color = (0, 255, 0)
        elif isWin == 'lose': text = 'LOST'; color = (255, 0, 0)
        if isWin:
            self.turn = False
            pygame.draw.rect(self.window, (255, 255, 255), (440, 250, 120, 350))
            write(self.window, f'YOU {text}', 'tahoma.ttf', 40, 500, 300, color)
            self.dashboardButton.draw()
            if self.checkExitClick(self.dashboardButton):
                self.run = False
    
    # def loseScreen(self):
    #     self.turn = False
    #     pygame.draw.rect(self.window, (255, 255, 255), (440, 250, 120, 350))
    #     write(self.window, 'YOU LOST', 'tahoma.ttf', 40, 500, 300, ((255, 0, 0)))
    #     self.dashboardButton.draw()
