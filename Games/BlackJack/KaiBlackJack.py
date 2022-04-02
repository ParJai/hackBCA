import random

dealer_bust = False
player_bust = False
play_again = 'y'
blackjack = False
error = False


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        return rank + ' of ' + suit

    def shuffle(self):
        random.shuffle(self.deck)

    def display(self):
        for card in self.deck:
            print(card)

    def deal(self):
        return self.deck.pop()


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

    def show_hand(self):
        for card in self.cards:
            print(card.__str__())


class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def again():
    global play_again
    global dealer_bust
    global player_bust
    global blackjack
    global error
    dealer_bust = False
    player_bust = False
    play_again = 'y'
    blackjack = False
    error = False
    play_again = input('Would you like to play again? (y/n) ').lower()
    if play_again == 'y' or play_again == 'n':
        pass
    else:
        again()


def play():
    global error
    if not error:
        print('\n' * 100)
    print(f'You have a total of: {player_chips.total} chips')
    player_chips.bet = input('How many chips would you like to bet? ')
    try:
        player_chips.bet = int(player_chips.bet)
    except ValueError:
        error = True
        print('\n' * 100)
        play()
    if player_chips.bet > player_chips.total:
        error = True
        print('\n' * 100)
        print('Sorry, you do not have enough chips to place that bet.')
        play()
    elif player_chips.bet == 0 or player_chips.bet < 0:
        error = True
        print('\n' * 100)
        print('Sorry, you cannot bet 0 chips or less.')
        play()
    else:
        pass

    hit_stand = ''

    # DEALER CARDS #
    print('\n' * 100)
    dealer = Hand()
    print("Dealer's cards:")
    dealer.add_card(deck.deal())
    dealer.show_hand()
    dealer.adjust_for_ace()
    print('???')

    # PLAYER CARDS/PLAY #
    global dealer_bust
    global player_bust
    global blackjack
    player = Hand()
    print('\n' * 2)
    print("Your cards:")
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    player.adjust_for_ace()
    player.show_hand()
    print('\n')
    print(f'The total value of your cards is {player.value}.')
    if player.value == 21:
        blackjack = True
    else:
        while hit_stand != 'hit' and hit_stand != 'stand':
            hit_stand = input('Would you like to hit or stand? ').lower()
            print('\n' * 100)
            if hit_stand == 'hit':
                while hit_stand == 'hit':
                    print("Dealer's cards:")
                    dealer.show_hand()
                    print('???')
                    print('\n' * 2)
                    player.add_card(deck.deal())
                    player.adjust_for_ace()
                    print('Your cards:')
                    player.show_hand()
                    print('\n')
                    print(f'The total value of your cards is {player.value}.')
                    print('\n')
                    if player.value < 21:
                        pass
                    elif player.value == 21:
                        blackjack = True
                        break
                    else:
                        print('\n')
                        print('BUST!')
                        print('Dealer wins.')
                        player_bust = True
                        break
                    hit_stand = input('Would you like to hit or stand? ').lower()
                    print('\n' * 100)
            elif hit_stand == 'stand':
                break

    # IF BLACKJACK #
    if blackjack:
        print("Congratulations, you win!")
        player_chips.win_bet()
        print(f'You now have a total of {player_chips.total} chips.')
        again()
    else:
        # DEALER PLAY #
        if not player_bust:
            while dealer.value < 17:
                print('\n' * 100)
                print("Dealer's cards:")
                dealer.add_card(deck.deal())
                dealer.adjust_for_ace()
                dealer.show_hand()
                print('\n')
                print(f"Dealer's value: {dealer.value}")
                if dealer.value > 21:
                    print('Dealer BUST!')
                    dealer_bust = True
                    break
                else:
                    continue

        # CHECK WHO WINS #
        global play_again
        print('\n')
        if not dealer_bust and not player_bust:
            if player.value > dealer.value:
                print("Congratulations, you win!")
                player_chips.win_bet()
                print(f'You now have a total of {player_chips.total} chips.')
            elif player.value < dealer.value:
                print('Sorry, you lost.')
                player_chips.lose_bet()
                print(f'You now have a total of {player_chips.total} chips.')
            else:
                print('PUSH!')
                print(f'You still have a total of {player_chips.total} chips.')
        elif dealer_bust:
            print("Congratulations, you win!")
            player_chips.win_bet()
            print(f'You now have a total of {player_chips.total} chips.')
        else:
            print('Sorry, you lost.')
            player_chips.lose_bet()
            print(f'You now have a total of {player_chips.total} chips.')
        if player_chips.total == 0:
            print('\n')
            print('It looks like you have run out of chips for the night. Better luck next time!')
            play_again = 'n'
        else:
            again()


'''
PROGRAM
'''


player_chips = Chips()
while play_again == 'y':
    deck = Deck()
    deck.shuffle()

    play()
if player_chips.total != 0:
    print(f'You ended with a total of {player_chips.total} chips.')
    print('Hope you had a fun night at the Casino! Remember to cash out your winnings and come back tomorrow!')