
import pygame

pygame.init()

board = [3, 4, 5]

def write(screen, text, font, text_size, center, color):
    text_font = pygame.font.Font(font, text_size)
    text_to_write = text_font.render(text, True, color)
    text_rect = text_to_write.get_rect()
    text_rect.center = center
    screen.blit(text_to_write, text_rect)

class Button:
    def __init__(self, window, x, y):
        self.window = window
        self. x = x
        self.y = y
    
    def draw(self):
        pygame.draw.rect(self.window, (219, 223, 172), )

    def onClick(self):
        pass

class Stone:
    def __init__(self, window, row, x, y, size):
        self.window = window
        self.row = row
        self.x, self.y = x, y
        self.size = size
    
    def draw(self):
        pygame.draw.circle(self.window, (255, 255, 255), (self.x, self.y), self.size)
    
class Nim:
    def __init__(self, window, clock):
        self.window = window
        self.clock = clock
        self.mouse_pos = ()

        self.board = board
        self.stones = []
        self.rowSelected = 0
        self.run = True
        
        self.bgColor = (74, 111, 165)
        margin = 40

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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_pos = pygame.mouse.get_pos()
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_pos = ()
            self.draw()
    
    def draw(self):
        self.window.fill(self.bgColor)
        for row in self.stones:
            for stone in row:
                stone.draw()
            if self.rowSelected != 0:
                self.checkStoneClick(row)
            else:
                if self.rowSelected == self.stones.index(row):
                    self.checkStoneClick(row)
        pygame.display.update()

    def checkStoneClick(self, row):
        if self.mouse_pos and (len(row) != 0) and (row[0].x - row[0].size) <= self.mouse_pos[0] <= (row[-1].x + row[0].size) and (row[0].y - row[0].size) <= self.mouse_pos[1] <= (row[-1].y + row[0].size):
            self.removeStone(self.stones, self.stones.index(row))
            self.mouse_pos = ()

    def removeStone(self, stones, row):
        stones[row].pop(-1)
