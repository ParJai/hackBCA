import random
import itertools
import pygame
import sys

import time
print(sys.path[0])
f = open(sys.path[0] + "\\Games\\Anagrams\\words.txt", 'r')
WORDLIST = f.read().split()
f2 = open(sys.path[0]+'\\Games\\Anagrams\\wordsSix.txt', 'r')
SIXLIST = f2.read().split()

class anagrams:
    def __init__(self, window, clock):
        self.current = time.time()
        self.window = window
        self.clock = clock
        self.run = True
        words = []
        letters = self.generateList()
        valid = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        user_text = ''
        score = 0
        combos = self.finalCombos(letters)
        
        wordsFound3 = []
        wordsFound4 = []
        wordsFound5 = []
        wordsFound6 = []
        allowed = {}
        appear = {}
        
        for i in letters:
            if i in allowed:
                allowed[i] += 1
            else:
                allowed[i] = 1
        
        
        
        while(self.run):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
           
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        appear[user_text[-1]] -= 1
                        user_text = user_text[:-1]
                    
                    else:
                        prev = len(user_text)
                        user_text += event.unicode
                        next = len(user_text)
                        if (next > 6):
                            user_text = user_text[:-1]
                    
                        if (prev != next):
                            if user_text[-1] in valid:
                                if user_text[-1].upper() not in letters:
                                    user_text = user_text[:-1]
                                else:
                                    user_text = user_text[:-1] + user_text[-1].upper()
                                    a = user_text[-1]
                                    if a in appear:
                                        appear[a] += 1
                                    else:
                                        appear[a] = 1
                                    if (appear[a] > allowed[a]):
                                        user_text = user_text[:-1]
                                    
                                    
                                
                            else:
                                user_text = user_text[:-1]
                        if event.key == pygame.K_RETURN:
                            
                            guess = user_text
                            if (self.validGuess(guess, letters) and guess in combos):
                                combos.remove(user_text)
                                score += self.wordValue(user_text)
                                
                                if len(guess) == 3:
                                    wordsFound3.append(guess)
                                elif len(guess) == 4:
                                    wordsFound4.append(guess)
                                elif len(guess) == 5:
                                    wordsFound5.append(guess)
                                elif len(guess) == 6:
                                    wordsFound6.append(guess)
                                user_text = ''
                                appear = {}
                            else:
                                self.write(self.window,  "Word Already Entered", "tahoma.ttf", 50, (500, 250), (255, 0, 0))
                                
                                user_text = ''
                                appear = {}
            if 60 - (int(time.time() - self.current)) == 0:
                break
    
            self.draw(letters, words, user_text, score)
        while(self.run):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.drawEnd(score, wordsFound3, wordsFound4, wordsFound5, wordsFound6)

    def validGuess(self, guess, aList):
        if guess in WORDLIST and guess in self.finalCombos(aList):
            return True
        return False


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
    def drawEnd(self, score, wordsFound3, wordsFound4, wordsFound5, wordsFound6):
        self.window.fill((231, 173, 153))
        pygame.draw.rect(self.window, (255,255,255), (150, 0, 700, 600))
        self.write(self.window, "ANAGRAMS", "tahoma.ttf", 36, (500, 30), (203, 98, 23))
        self.write(self.window, "RESULTS", "tahoma.ttf", 36, (500, 60), (203, 98, 23))

        wordsFound3.sort()
        wordsFound4.sort()
        wordsFound5.sort()
        wordsFound6.sort()

        if len(wordsFound6) != 0:
            self.write(self.window, f"6 letter words:", "tahoma.ttf", 30, (500, 100), (0, 196, 0))
            self.write(self.window, f"{wordsFound6}", "tahoma.ttf", 30, (500, 150), (0, 196, 0))

        if len(wordsFound5) != 0:
            self.write(self.window, f"5 letter words:", "tahoma.ttf", 30, (500, 200), (0, 196, 0))
            self.write(self.window, f"{wordsFound5}", "tahoma.ttf", 30, (500, 250), (0, 196, 0))

        if len(wordsFound4) != 0:
            self.write(self.window, f"4 letter words:", "tahoma.ttf", 30, (500, 300), (0, 196, 0))
            self.write(self.window, f"{wordsFound4}", "tahoma.ttf", 30, (500, 350), (0, 196, 0))

        if len(wordsFound3) != 0:
            self.write(self.window, f"3 letter words:", "tahoma.ttf", 30, (500, 400), (0, 196, 0))
            self.write(self.window, f"{wordsFound3}", "tahoma.ttf", 30, (500, 450), (0, 196, 0))

        self.write(self.window, f"Final Score: {score}", "tahoma.ttf", 30, (500, 650), (0, 196, 0))
        pygame.display.update()

    

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
    def isValidList(self, aList):
        if self.value(self.finalCombos(aList)) >= 10000:
            return True
        return False
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
        
    def draw(self, letters, words, user_text, score):
        self.window.fill((231, 173, 153))
        pygame.draw.rect(self.window, (255,255,255), (150, 0, 700, 600))
        self.write(self.window, "ANAGRAMS", "tahoma.ttf", 36, (500, 30), (203, 98, 23))
        #input rect
        color = pygame.Color('lightskyblue3')
        input_rect = pygame.Rect(175, 300, 650, 96)
        pygame.draw.rect(self.window, color, input_rect)
        self.write(self.window, user_text, "tahoma.ttf", 50, (500, 350), (0, 0, 0))
        self.write(self.window, f"Time: {60 - (int(time.time() - self.current))}", "tahoma.ttf", 30, (500, 650), (0, 0, 255))
        for i in range (0, 6):
            self.window.blit(pygame.image.load(f'Games/Anagrams/anagramsLetters/{letters[i]}.png').convert(), (180 + i * 108, 400))

        self.write(self.window, f"Score: {score}", "tahoma.ttf", 30, (500, 80), (0, 196, 0))

        pygame.display.update()