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
        letters = self.generateList()
        valid = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        user_text = ''

        
        color_active = pygame.Color('lightskyblue3')
        
        
        
        while(self.run):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
           
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    
                    else:
                        user_text += event.unicode
                        if user_text[-1] not in letters:
                            user_text = user_text[:-1]

            self.draw(letters, words, user_text)

    def shuffle(self, s):
        # Shuffles word randomly
        n = len(s)
        li = list(s)
        for i in range(0,n-1):
            pos = random.randint(i+1,n-1)
            li[pos],li[i] = li[i],li[pos]
        res = ""
        for i in range(n):
            res = res + li[i]
        return res
    def generateList(self):
        # Generates list of 6 random characters
        # Assuming list is valid
        letters = []
        validList = False
        while not validList:
            num = random.randint(0,23033)
            word = SIXLIST[num]
            for i in range(0,6):
                letters.append(word[i])
            if self.isValidList(letters):
                validList = True
            else:
                letters = []
        word = ""
        for i in range (0, 6):
            word += letters[i]
        word = self.shuffle(word)
        letters = []
        for i in range (len(word)):
            letters.append(word[i])
            return letters

    def isValidList(self, aList):
        if self.value(self.finalCombos(aList)) >= 10000:
            return True
        return False

    def value(self, combosList):
        valueSum = 0
        for element in combosList:
            if element.upper() in WORDLIST:
                valueSum += self.wordValue(element)
        return valueSum

    def finalCombos(self, aList):
        combos = []
        finalCombos = []
        permutations = list(itertools.permutations(aList))
        for permutation in permutations:
            word = ""
            for char in permutation:
                word += char
            combos.append(word)
            combos.append(word[:5])
            combos.append(word[:4])
            combos.append(word[:3])
        finalCombos = list(set(combos))
        return finalCombos

    def wordValue(self, guess):
        if len(guess) == 3:
            return 100
        elif len(guess) == 4:
            return 400
        elif len(guess) == 5:
            return 1200
        elif len(guess) == 6:
            return 2000
        else:
            return 0


    def write(self, screen, text, font, text_size, center, color):
        text_font = pygame.font.Font(font, text_size)
        text_to_write = text_font.render(text, True, color)
        text_rect = text_to_write.get_rect()
        text_rect.center = center
        screen.blit(text_to_write, text_rect)
        
    def draw(self, letters, words, user_text):
        self.window.fill((231, 173, 153))
        pygame.draw.rect(self.window, (255,255,255), (150, 0, 700, 600))
        self.write(self.window, "ANAGRAMS", "tahoma.ttf", 36, (500, 30), (203, 98, 23))
        #input rect
        color = pygame.Color('lightskyblue3')
        input_rect = pygame.Rect(200, 200, 140, 32)
        pygame.draw.rect(self.window, color, input_rect)
        self.write(self.window, user_text, "tahoma.ttf", 24, (300, 100), (0, 0, 0))

        for i in range (0, 6):
            window.blit(pygame.image.load(f'anagramsLetters/{letters[i]}.png').convert(), (180 + i * 108, 400))

        self.write(self.window, f"Score: {score}", "tahoma.ttf", 30, (500, 80), (0, 196, 0))

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