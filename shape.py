import pygame

class Rectangle:
    def __init__(self, x, y, width, height, color, window):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.window = window
    
    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))
