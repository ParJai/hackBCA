import pygame

class Dashboard:
    def __init__(self, window, clock):
        self.window = window

        self.clock = clock

        self.run = True

        self.bgColor = (231, 173, 153)
        self.navColor = (40, 0, 3)

        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.draw()

    def draw(self):
        self.window.fill(self.bgColor)
        pygame.draw.rect(self.window, self.navColor, (0, 0, 1400, 100))
        pygame.display.update()
        
    