# main.py

import random
from time import sleep

def main():
    deck = []

    for i in range(8):
        for j in range(2, 11):
            deck.append(j)
            deck.append("Jack")
            deck.append("Queen")
            deck.append("King")
            deck.append("Ace")

    first = random.choice(deck)
    second = random.choice(deck)
    hand = [first, second]
    total = 0
    counter = 0

    if "Ace" in hand:
        if "Queen" in hand or "King" in hand or "Jack" in hand or 10 in hand:
            print(f"\nHere is your hand: {hand}")
            print("\nBlackjack! You win!")
            end()

    for element in hand:
        if element == 'Queen' or element == 'Jack' or element == 'King':
            total += 10

        elif element == 'Ace':
            if counter == 0:
                print(f"\nHere is your hand: {hand}")
                sleep(2)
            A = input("You have an Ace! Choose its value (1 or 11): ")
            total += int(A)
            counter += 1

        else:
            total += element

    while True:
        sleep(1)
        print(f"\n\n\nHere is your new hand: {hand}")

        sleep(1.5)
        print(f"Your current value is {total}")

        choice = input("\nType in H to hit or S to stay: ")

        if choice == 'H':
            another = random.choice(deck)
            hand.append(another)

            if another == 'Queen' or another == 'Jack' or another == 'King':
                total += 10

            elif another == 'Ace':
                sleep(2)
                print(f"\nYour new hand is {hand}")
                sleep(1)
                choice_ace = input("\nYou have an Ace! Choose its value (1 or 11): ")
                total += int(choice_ace)

            else:
                total += another

        elif choice == 'S':
            break

        if total > 21:
            sleep(1.5)
            print(f"\nYour new hand is {hand}")
            sleep(1)
            print("\nOh no, you busted! :(")
            end()

    print("\n\nDealer's Turn!")

    deal_first = random.choice(deck)
    deal_second = random.choice(deck)
    deal_hand = [deal_first, deal_second]
    deal_total = 0

    for element in deal_hand:
        if element == 'Queen' or element == 'Jack' or element == 'King':
            deal_total += 10

        elif element == "Ace":
            choosing = [1, 11]
            deal_total += random.choice(choosing)

        else:
            deal_total += element

    while True:
        sleep(1.5)
        print(f"\nHere is the dealer's new hand: {deal_hand}")

        if deal_total == 21 and len(deal_hand) == 2:
            sleep(1)
            print("Blackjack! Dealer wins!")
            end()

        sleep(2)
        print(f"\nThe value of the dealer's cards is {deal_total}")

        if deal_total < 17:
            deal_another = random.choice(deck)
            deal_hand.append(deal_another)

            if deal_another == 'Queen' or deal_another == 'Jack' or deal_another == 'King':
                deal_total += 10

            elif deal_another == 'Ace':
                deal_total += random.choice(choosing)

            else:
                deal_total += deal_another

        elif deal_total > 21:
            sleep(2)
            print("\nThe dealer busted. You win!")
            end()

        else:
            sleep(3)
            print(f"\nThe dealer has finalized their hand.")
            break

    if total > deal_total:
        sleep(2)
        print("\nYou had the better hand. You win! :)")

    elif total == deal_total:
        sleep(2)
        print("\nYou pushed (tied).")

    elif total < deal_total:
        sleep(2)
        print("\nThe dealer had the better hand. You lost :(")

    end()


def end():
    sleep(2.5)
    play_again = input("\n\nPress a key to play again, or press q to quit. ")

    if play_again != 'q':
        main()

    else:
        exit(1)


welcome()







