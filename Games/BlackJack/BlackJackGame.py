import pygame as pygame
from BlackJackHelper import *
from BlackJackGameSetup import *
import sys
import time

pygame.init()
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

pygame.display.set_caption('BlackJack')
display.fill(background)
pygame.draw.rect(display, gray, pygame.Rect(0, 0, 250, 700))


#textSetUp functions
def textSetUp(text, font):
    #global cardSize, cardCenter, cardBack, cardBackCenter, suits, ranks, background, gray, black, lightSlate, darkSlate, green, red, normalFont, textfont, endFont, blackJackFont, display, clock 
    surface = font.render(text, True, black)
    return surface, surface.get_rect()

def textSetUpContinued(text, font, color):
    #global cardSize, cardCenter, cardBack, cardBackCenter, suits, ranks, background, gray, black, lightSlate, darkSlate, green, red, normalFont, textfont, endFont, blackJackFont, display, clock 
    surface = font.render(text, True, color)
    return surface, surface.get_rect()


#gameDisplayText functions
def gameDisplayText(text, x, y):
    #global cardSize, cardCenter, cardBack, cardBackCenter, suits, ranks, background, gray, black, lightSlate, darkSlate, green, red, normalFont, textfont, endFont, blackJackFont, display, clock 
    gameSurface, gameRect = textSetUp(text, textFont)

    gameRect.center = (x, y)
    display.blit(gameSurface, gameRect)
    pygame.display.update()

def gameDisplayTextContinued(text, x, y, color):
    #global cardSize, cardCenter, cardBack, cardBackCenter, suits, ranks, background, gray, black, lightSlate, darkSlate, green, red, normalFont, textfont, endFont, blackJackFont, display, clock 
    arr = textSetUpContinued(text, endFont, color)
    gameSurface, gameRect = textSetUpContinued(text, endFont, color)

    gameRect.center = (x, y)
    display.blit(gameSurface, gameRect)
    pygame.display.update()


#button display
def buttonDisplay(message, xCoord, yCoord, width, height, color1, color2, action = None):
    #global cardSize, cardCenter, cardBack, cardBackCenter, suits, ranks, background, gray, black, lightSlate, darkSlate, green, red, normalFont, textfont, endFont, blackJackFont, display, clock 
    position = pygame.mouse.get_pos()
    press = pygame.mouse.get_pressed()

    if (xCoord + width > position[0] and position[0] > xCoord) and (yCoord + height > position[1] and position[1] > yCoord):
        pygame.draw.rect(display, color2, (xCoord, yCoord, width, height))
        if press[0] == 1 != None:
            action()
    else:
        pygame.draw.rect(display, color1, (xCoord, yCoord, width, height))

    TextSurf, TextRect = textSetUp(message, normalFont)

    TextRect.center = ((xCoord + (width/2)), (yCoord + (height/2)))
    display.blit(TextSurf, TextRect)

def blackJackText(text, x, y, color):
    # cardSize, cardCenter, cardBack, cardBackCenter, suits, ranks, background, gray, black, lightSlate, darkSlate, green, red, normalFont, textfont, endFont, blackJackFont, display, clock 
    surface, rectangle = textSetUpContinued(text, blackJackFont, color)
    rectangle.center = (x, y)
    display.blit(surface, rectangle)
    pygame.display.update()

class Game:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Hand()
        self.player = Hand()
        self.deck.shuffle()
        self.playerCardCount = 0
        self.chips = Chips()
    
    def checkBlackJack(self):
        #global cardSize, cardCenter, cardBack, cardBackCenter, suits, ranks, background, gray, black, lightSlate, darkSlate, green, red, normalFont, textfont, endFont, blackJackFont, display, clock 
        self.dealer.calculate()
        self.player.calculate()

        dealerCard = pygame.image.load('PNG-cards-1.3' + chr(92) + self.dealer.card_imageNames[0] + '.png').convert()
        
        if self.player.value == 21 and self.dealer.value == 21:
            display.blit(dealerCard, (550, 200))
            blackJackText("BlackJack! Push!", 500, 250, gray)
            time.sleep(4)
            self.playAgain("T")

        elif self.player.value == 21:
            display.blit(dealerCard, (550, 200))
            blackJackText("You got BlackJack! You win!", 500, 250, green)
            time.sleep(4)
            self.playAgain("W")
        elif self.dealer.value == 21:
            display.blit(dealerCard, (550, 200))
            blackJackText("Dealer has BlackJack! You lose!", 500, 250, red)
            time.sleep(4)
            self.playAgain("L")
            
        self.player.value = 0
        self.dealer.value = 0


    def deal(self):
        #global cardSize, cardCenter, cardBack, cardBackCenter, suits, ranks, background, gray, black, lightSlate, darkSlate, green, red, normalFont, textfont, endFont, blackJackFont, display, clock 
        for i in range(2):
            self.dealer.add_card(self.deck.deal())
            self.player.add_card(self.deck.deal())
        self.dealer.show_cards()
        self.player.show_cards()
        self.playerCardCount = 1

        dealerFirstCard = pygame.image.load('PNG-cards-1.3' + chr(92) + self.dealer.card_imageNames[0] + '.png').convert()
        dealerSecondCard = pygame.image.load('PNG-cards-1.3' + chr(92) + 'back.png').convert()
            
        playerFirstCard = pygame.image.load('PNG-cards-1.3' + chr(92) + self.player.card_imageNames[0] + '.png').convert()
        playerSecondCard = pygame.image.load('PNG-cards-1.3' + chr(92) + self.player.card_imageNames[1] + '.png').convert()


        gameDisplayText("Dealer's hand is:", 500, 150)

        display.blit(dealerFirstCard, (400, 200))
        display.blit(dealerSecondCard, (550, 200))

        gameDisplayText("Your hand is:", 500, 400)
        
        display.blit(playerFirstCard, (300, 450))
        display.blit(playerSecondCard, (410, 450))
        self.checkBlackJack()


    def hit(self):
        self.player.add_card(self.deck.deal())
        self.checkBlackJack()
        self.playerCardCount += 1
        
        if self.playerCardCount == 2:
            self.player.calculate()
            self.player.show_cards()
            playerThirdCard = pygame.image.load('PNG-cards-1.3' + chr(92) + self.player.card_imageNames[2] + '.png').convert()
            display.blit(playerThirdCard, (520, 450))

        if self.playerCardCount == 3:
            self.player.calculate()
            self.player.show_cards()
            playerFourthCard = pygame.image.load('PNG-cards-1.3' + chr(92) + self.player.card_imageNames[3] + '.png').convert()
            display.blit(playerFourthCard, (630, 450))
                
        if self.player.value > 21:
            dealerFirstCard = pygame.image.load('PNG-cards-1.3' + chr(92) + self.dealer.card_imageNames[1] + '.png').convert()
            display.blit(dealerFirstCard, (550, 200))
            gameDisplayTextContinued("You Busted!", 500, 250, red)
            time.sleep(4)
            self.playAgain("L")
            
        self.player.value = 0

        if self.playerCardCount > 4:
            sys.exit()

    def stay(self):
        dealerFirstCard = pygame.image.load('PNG-cards-1.3' + chr(92) + self.dealer.card_imageNames[1] + '.png').convert()
        display.blit(dealerFirstCard, (550, 200))
        self.checkBlackJack()
        self.dealer.calculate()
        self.player.calculate()

        if self.player.value > self.dealer.value:
            gameDisplayTextContinued("You Won!", 500, 250, green)
            time.sleep(4)
            self.playAgain("W")
        elif self.player.value < self.dealer.value:
            gameDisplayTextContinued("Dealer Wins!", 500, 250, red)
            time.sleep(4)
            self.playAgain("L")
        else:
            gameDisplayTextContinued("It's a Tie!", 500, 250, gray)
            time.sleep(4)
            self.playAgain("T")

    def bet(self):
        self.chips.total -= 50
        gameDisplayText(f"\t\t\tChips: {self.chips.total}", 50, 650)
        self.deal()

    def exit(self):
        sys.exit()
    
    def playAgain(self, isWin):
        if isWin == "W":
            self.chips.total += 100
        gameDisplayText(f"\t\t\tChips: {self.chips.total}", 50, 650)

        if self.chips.total == 0:
            exit()

        gameDisplayText("Exit or wait!", 200, 80)
        time.sleep(3)
        self.player.value = 0
        self.dealer.value = 0
        self.deck = Deck()
        self.dealer = Hand()
        self.player = Hand()
        self.deck.shuffle()
        display.fill(background)
        pygame.draw.rect(display, gray, pygame.Rect(0, 0, 250, 700))
        pygame.display.update()


play = Game()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        buttonDisplay("Deal, no bet", 30, 100, 150, 50, lightSlate, darkSlate, play.deal)
        buttonDisplay("Hit", 30, 200, 150, 50, lightSlate, darkSlate, play.hit)
        buttonDisplay("Stay", 30, 300, 150, 50, lightSlate, darkSlate, play.stay)
        buttonDisplay("Bet 50", 30, 400, 150, 50, lightSlate, darkSlate, play.bet)
        buttonDisplay("EXIT", 30, 500, 150, 50, lightSlate, darkSlate, play.exit)
    
    pygame.display.flip()