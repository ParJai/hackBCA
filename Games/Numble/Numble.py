import math
import pygame

class numble:
    def __init__ (self, window, clock):
        userText = ''

        self.window = window
        self.clock = clock
        self.run = True
        self.numbers = []

        while(self.run):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pass
            self.draw()


    def write(self, screen, text, font, text_size, center, color):
        text_font = pygame.font.Font(font, text_size)
        text_to_write = text_font.render(text, True, color)
        text_rect = text_to_write.get_rect()
        text_rect.center = center
        screen.blit(text_to_write, text_rect)

    def draw(self):
        self.window.fill((231, 173, 153))
        pygame.draw.rect(self.window, (255,255,255), (150, 0, 700, 600))
        self.write(self.window, "Numbles", "tahoma.ttf", 36, (505, 25), (255, 0, 0))
        for i in range (12):
            self.write(self.window, str(i + 1) +".", "tahoma.ttf", 16, (160, 128 + i*35), (128, 190, 128))
        pygame.draw.rect(self.window, (128,128,128), (150, 110, 350, 3))
        pygame.draw.rect(self.window, (128, 128, 128), (260, 110, 3, 400))
        #pygame.draw.rect(self.window, (128, 128, 128), (350, 110, 3, 400))
        self.write(self.window, "Guesses", "tahoma.ttf", 20, (200, 90), (82, 173, 228))
        self.write(self.window, "Correct", "tahoma.ttf", 20, (320, 90), (82, 173, 228))
        self.write(self.window, "Wrong Spot", "tahoma.ttf", 20, (440, 90), (82, 173, 228))
        self.write(self.window, "Next Guess: ", "tahoma.ttf", 20, (700, 90), (231, 231, 231))

        pygame.draw.rect(self.window, (231, 231, 231), (375, 530, 200, 50))
        pygame.display.flip()


    

WIDTH = 1000
HEIGHT = 700

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.font.init()


numble(window, clock)
        