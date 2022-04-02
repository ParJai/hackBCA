import math

class numble:
    def __init__ (self, window, clock):
        self.window = window
        self.clock = clock
        self.run = True
        self.numbers = []

WIDTH = 1000
HEIGHT = 700

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.font.init()
#wadsas

numble(window, clock)
        