import pygame
from client import Client
from Games.TicTacToe.tictactoe_gui import TicTacToe
from dashboard import Dashboard

WIDTH = 1400
HEIGHT = 900

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


dashboard = Dashboard(window,clock)
tictactoe = TicTacToe(window,clock)

client = Client()
print('connected')

pygame.display.quit()