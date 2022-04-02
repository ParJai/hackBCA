import pygame
from client import Client
from Games.TicTacToe.tictactoe_gui import TicTacToe
from Games.Nim.NimGUI import Nim
#from dashboard import Dashboard

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


<<<<<<< HEAD
# dashboard = Dashboard(window, clock)
# tictactoe = TicTacToe(window, clock)
nim = Nim(window, clock)
=======
dashboard = Dashboard(window,clock)
>>>>>>> 81c7dea1dae13e48962adf9dee27dcb2b0a3756d

client = Client(dashboard.dest)
print(dashboard.dest)


print('connected')

pygame.display.quit()
