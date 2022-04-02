import pygame as pygame

width = 1000
height = 700


cardSize = (72, 96)
cardCenter = (42, 56)
cardBack = (72, 96)
cardBackCenter = (42, 56)

suits = ['hearts', 'diamonds', 'spades', 'clubs']
ranks = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']

#colors
background = (10, 110, 110)
gray = (220, 220, 220)
black = (0, 0, 0)
lightSlate = (119, 136, 153)
darkSlate = (47, 79, 79)
green = (0, 220, 0)
red = (255, 0, 0)

#fonts
pygame.init()
normalFont = pygame.font.SysFont("Arial", 20)
textFont = pygame.font.SysFont('Tahoma', 40)
endFont = pygame.font.SysFont('Bahnschrift', 100)
blackJackFont = pygame.font.SysFont('Comic Sans MS', 75)




