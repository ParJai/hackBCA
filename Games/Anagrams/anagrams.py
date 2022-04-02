import random
import itertools
import pygame
import sys
import Holding
print(sys.path[0])
f = open(sys.path[0] + "\\words.txt", 'r')
WORDLIST = f.read().split()
f2 = open(sys.path[0]+'\\wordsSix.txt', 'r')
SIXLIST = f2.read().split()

class anagrams:
    
    def __init__(self, window, clock):
        self.window = window
        self.clock = clock
        self.run = True
        words = []
        letters = []

        while(self.run):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pass
            self.draw(letters, words)

    def write(self, screen, text, font, text_size, center, color):
        text_font = pygame.font.Font(font, text_size)
        text_to_write = text_font.render(text, True, color)
        text_rect = text_to_write.get_rect()
        text_rect.center = center
        screen.blit(text_to_write, text_rect)
        
    def draw(self, letters, words):
        self.window.fill((231, 173, 153))
        pygame.draw.rect(self.window, (255,255,255), (150, 0, 700, 600))
        self.write(self.window, "ANAGRAMS", "tahoma.ttf", 36, (500, 30), (203, 98, 23))
        for i in range (6):
            #draw each letter
            pass



        pygame.display.flip()
WIDTH = 1000
HEIGHT = 700

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.font.init()


anagrams(window, clock)


    
    # Currently have to input "EXIT CODE" to end, change this to ending the loop once the 60 second timer ends
    # Start 60 second timer once the 6 letters are sent

main()
f.close()