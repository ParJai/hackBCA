import pygame

class box:
    def __init__(self, x,y, col, row):
        self.x = x
        self.y = y
        self.col = col
        self.row = row


    def checkBox(self, mx, my):
        if self.x <= mx <= self.x+71 and self.y <= my <= self.y+71:
            return True
        return False
class Battleship:

    def __init__(self, window, clock):
        self.window = window
        self.clock = clock

        self.run = True

        self.drawables = []

        self.pieces = [2, 2, 3, 4, 5]

        self.buttons = {}
        while self.run:
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    print('exit')
                    self.run = False
            self.draw()

    def draw(self):
        self.window.fill((231, 173, 153))
        pygame.draw.rect(self.window, (71, 230, 199), (50, 50, 600, 600))
        for i in range(100, 600, 71):
            self.drawables.append(pygame.draw.rect(self.window, (148, 231, 215), (i, 50, 10, 600)))
        for i in range(100, 600, 71):
            self.drawables.append(pygame.draw.rect(self.window, (148, 231, 215), (50, i, 600, 10)))
        
        if self.pieces != []:
            mx, my = pygame.mouse.get_pos()

        pygame.display.update()

    

WIDTH = 1000
HEIGHT = 700

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.font.init()

Battleship(window, clock)