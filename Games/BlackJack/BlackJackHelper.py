import random

suits = ['hearts', 'diamonds', 'spades', 'clubs']
ranks = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']


class Deck:
    def __init__(self):
        self.deck = []
        for rank in ranks:
            for suit in suits:
                self.deck.append((rank, suit))

    def shuffle(self):
        random.shuffle(self.deck)

    def display(self):
        for card in self.deck:
            print(card)

    def deal(self):
        if len(self.deck) > 1:
            return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.card_imageNames = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)

        if card[0] == 'ace':

    def calculate(self):
        ranks = [card[0] for card in self.cards]
        aces = [rank for rank in ranks if rank == "ace"]
        notAces = [rank for rank in ranks if rank != "ace"]

        for ace in aces:
            if self.value <= 10:
                self.value += 11 
            else:
                self.value += 1     

        for card in notAces:
            if card == 'jack' or card == 'queen' or card == 'king':
                self.value += 10
            else:
                self.value += int(card)

    def show_cards(self):
        for card in self.cards:
            name = "_of_".join((card[0], card[1]))
            if name not in self.card_imageNames:
                self.card_imageNames.append(name)


class Chips:
    def __init__(self):
        self.total = 100