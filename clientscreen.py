import pygame
from client import Client
from Games.Nim.NimGUI import Nim
from dashboard import Dashboard
from tempclient import TempClient
from Games.Nim.NimGUI import Nim
from Games.TicTacToe.tictactoe_gui import *
from Games.Anagrams.anagrams import anagrams
from Games.Connect_Four.c4GUI import Connect4

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

dashboard = Dashboard(window, clock)
while dashboard.dest != "":
    client = Client(dashboard.dest)
    if dashboard.dest == 'agm':
        tempclient = anagrams(window, clock)
    elif dashboard.dest == 'ttt':
        tempclient = TicTacToe(window, clock, client)
    elif dashboard.dest == 'bj':
        tempclient = TicTacToe(window, clock, client)
    elif dashboard.dest == 'nim':
        tempclient = Nim(window, clock, client)
    elif dashboard.dest == 'c4':
        tempclient = Connect4(window, clock, client)
    dashboard = Dashboard(window, clock)

pygame.display.quit()
