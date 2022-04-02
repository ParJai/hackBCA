import pygame
from client import Client
from Games.Nim.NimGUI import Nim
from dashboard import Dashboard
from tempclient import TempClient
from Games.Nim.NimGUI import Nim
from Games.TicTacToe.tictactoe_gui import *
from Games.Connect_Four.c4GUI import Connect4

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


dashboard = Dashboard(window, clock)
# tictactoe = TicTacToe(window, clock)
#nim = Nim(window, clock)

client = Client(dashboard.dest)
print(dashboard.dest)
print('connected')
tempclient = Connect4(window, clock, client)

pygame.display.quit()
