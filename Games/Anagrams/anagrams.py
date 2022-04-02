import random
import itertools

f = open('words.txt', 'r')
WORDLIST = f.read().split()

def generateList():
    # Generates list of 6 random characters
    # Assuming list is valid
    letters = []
    validList = False
    while not validList:
        for i in range (0,6):
            numASCII = random.randint(65,90)
            letter = chr(numASCII)
            letters.append(letter)
        if isValidList(letters):
            validList = True
        else:
            letters = []
    return letters

def isValidList(aList):
    #print(aList)
    #print(finalCombos(aList))
    #print(value(finalCombos(aList)))
    if value(finalCombos(aList)) >= 10000:
        return True
    return False

def finalCombos(aList):
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

def value(combosList):
    valueSum = 0
    for element in combosList:
        if element.lower() in WORDLIST:
            valueSum += wordValue(element)
    return valueSum

def validGuess(guess):
    if guess in WORDLIST:
        return True
    return False

def wordValue(guess):
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

def main():
    score = 0
    letterList = generateList()
    while True:
        print(letterList)
        guess = input().lower()
        if validGuess(guess):
            score += wordValue(guess)
        print(score)

main()
f.close()