import pygame

class Dashboard:
    def __init__(self, window, clock):
        self.window = window

        self.clock = clock

        self.run = True
        
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False