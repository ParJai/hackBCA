def shuffle(s):
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

def generateList():
    # Generates list of 6 random characters
    # Assuming list is valid
    letters = []
    validList = False
    while not validList:
        num = random.randint(0,23033)
        word = SIXLIST[num]
        for i in range(0,6):
            letters.append(word[i])
        if isValidList(letters):
            validList = True
        else:
            letters = []
    word = ""
    for i in range (0, 6):
        word += letters[i]
    word = shuffle(word)
    letters = []
    for i in range (len(word)):
        letters.append(word[i])
    return letters

def isValidList(aList):
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
        if element.upper() in WORDLIST:
            valueSum += wordValue(element)
    return valueSum

def validGuess(guess, aList):
    if guess in WORDLIST and guess in finalCombos(aList):
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
    wordsFound3 = []
    wordsFound4 = []
    wordsFound5 = []
    wordsFound6 = []
    letterList = generateList()
    remaining = finalCombos(letterList)
    guess = ""
    while guess != "EXIT CODE":
        print(letterList)
        guess = input().upper()
        if validGuess(guess, letterList) and guess in remaining:
            score += wordValue(guess)
            remaining.remove(guess)
            if len(guess) == 3:
                wordsFound3.append(guess)
            elif len(guess) == 4:
                wordsFound4.append(guess)
            elif len(guess) == 5:
                wordsFound5.append(guess)
            elif len(guess) == 6:
                wordsFound6.append(guess)
            print(guess.upper(), "+" + str(wordValue(guess)))
        elif not validGuess(guess, letterList):
            print(guess.upper(), "(Invalid)")
        elif guess not in remaining:
            print(guess.upper(), "(Already used)")
        print("Score:", score)

    wordsFound3.sort()
    wordsFound4.sort()
    wordsFound5.sort()
    wordsFound6.sort()
    
    if len(wordsFound6) != 0:
        print("6 letter words: ")
        if len(wordsFound6) == 1:
            print(wordsFound6[0])
        elif len(wordsFound6) == 2:
            print(wordsFound6[0] + ", " + wordsFound6[1])
        elif len(wordsFound6) >= 3:
            for i in range (len(wordsFound6) - 1):
                print(wordsFound6[i], end=", ")
            print(wordsFound6[len(wordsFound6) - 1])

    if len(wordsFound5) != 0:
        print("5 letter words: ")
        if len(wordsFound5) == 1:
            print(wordsFound5[0])
        elif len(wordsFound5) == 2:
            print(wordsFound5[0] + ", " + wordsFound5[1])
        elif len(wordsFound5) >= 3:
            for i in range (len(wordsFound5) - 1):
                print(wordsFound5[i], end=", ")
            print(wordsFound5[len(wordsFound5) - 1])

    if len(wordsFound4) != 0:
        print("4 letter words: ")
        if len(wordsFound4) == 1:
            print(wordsFound4[0])
        elif len(wordsFound4) == 2:
            print(wordsFound4[0] + ", " + wordsFound4[1])
        elif len(wordsFound4) >= 4:
            for i in range (len(wordsFound4) - 1):
                print(wordsFound4[i], end=", ")
            print(wordsFound4[len(wordsFound4) - 1])

    if len(wordsFound3) != 0:
        print("3 letter words: ")
        if len(wordsFound3) == 1:
            print(wordsFound3[0])
        elif len(wordsFound3) == 2:
            print(wordsFound3[0] + ", " + wordsFound3[1])
        elif len(wordsFound3) >= 3:
            for i in range (len(wordsFound3) - 1):
                print(wordsFound3[i], end=", ")
            print(wordsFound3[len(wordsFound3) - 1])
    
    print("Your final score:", score)