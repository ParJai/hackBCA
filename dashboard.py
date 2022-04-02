
import pygame     
import os

pygame.init()

def write(screen, text, font, text_size, center, color):
    text_font = pygame.font.Font(font, text_size)
    text_to_write = text_font.render(text, True, color)
    text_rect = text_to_write.get_rect()
    text_rect.center = center
    screen.blit(text_to_write, text_rect)

class GameLink:
    def __init__(self, window, name, image, x, y, size, game):
        self.window = window

        self.name = name
        self.image = image
        self.x, self.y = x, y
        self.size = size
        self.game = game
    
    def draw(self):
        pygame.draw.rect(self.window, (0, 0, 0), (self.x, self.y, self.size[0], self.size[1]))
        write(self.window, self.name, 'tahoma.ttf', 20, (self.x + self.size[0] / 2, self.y + self.size[0] + (self.size[1] - self.size[0]) / 2), (255, 255, 255))

    def click(self, mx, my):
        if self.x <= mx <= 260 and self.y <= my <= 290:
            return True
        return False
class Dashboard:
    def __init__(self, window, clock):
        self.window = window

        self.clock = clock

        self.run = True

        self.bgColor = (231, 173, 153)
        self.navColor = (40, 0, 3)


        self.gameNames = os.listdir('Games')
        self.images = {}
        self.games = []
        self.gameList = ['agm', 'bts', 'bj', 'c4', 'nim', 'ttt']
        self.dest = ""
        # self.images[self.gameNames[i]]
        for i in range(6):
            x_val = (i if i < 3 else i - 3)
            y_val = (1 if i < 3 else 2)
            self.games.append(GameLink(self.window, self.gameNames[i], 'image', (55*(x_val+1) + 260*x_val), (40*y_val + 290*(y_val-1)), (260, 290), self.gameList[i]))

        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    for i in self.games:
                        if i.click(mx, my):
                            self.dest=i.game
                            self.run = False

            self.draw()

    def draw(self):
        self.window.fill(self.bgColor)
        for game in self.games:
            game.draw()
            if game.x <= pygame.mouse.get_pos()[0] <= game.x + game.size[0] and game.y <= pygame.mouse.get_pos()[1] <= game.y + game.size[1]:
                pygame.draw.rect(self.window, (255, 255, 255), ((game.x - 8), (game.y - 8), game.size[0] + 16, game.size[1] + 16), 8)
        pygame.display.update()
