import pygame
from client import Client
from TicTacToe.tictactoe_gui import TicTacToe

window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
pygame.font.init()

with open('nothing.txt') as data: nstring = data.read().strip()

tictactoe = TicTacToe(window,clock)

client = Client()
print('connected')

pygame.display.quit()