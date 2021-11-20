# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# cards_actual_value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# card_points =['A','K','Q','J','2','3','4','5','6','7','8','9','10']
# card_signs =['Heart','CLUB','DIAMOND','SPADE']
# replacement = {'A':11,'a':11, 'Q':10,  'q':10, 'K':10, 'k':10, 'J':10, 'j':10 }
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

from art import logo
import random

card_points = ['A', 'K', 'Q', 'J', '2', '3', '4', '5', '6', '7', '8', '9', '10']
card_signs = ['HEART', 'CLUB', 'DIAMOND', 'SPADE']


def random_value_choosing():
    # its more correct to put it inside the card class, but notice that you dont use '.self'
    # so it doesn't need an object from the class to run it
    return random.choice(card_points)  # you need to 'return| a value so you can assign it


def random_sign_choosing():
    return random.choice(card_signs)  # printing wont let the function give any data to the program


class Card:

    # i was wrong, init overloads arent a thing in python
    def __init__(self, value=None, sign=None):
        if value is None:
            value = random_value_choosing()
        if sign is None:
            sign = random_sign_choosing()

        self.value = value
        self.sign = sign

    # added this function
    def point_value(self):
        if self.value.isdigit():  # what is that function i just used?
            return int(self.value)
        else:
            return -1  # why do i return a negative number here?

    def display(self):
        print(f"You have got {self.value} of {self.sign}")  # GREAT change to the print, love it
        # BUT... if you run the code there's a small problem :P


class Player:
    def __init__(self, player_name='player'):  # using the dealer as the default name
        self.handed = []  # think how you'd like to handle splitting (when you get 2 of the same card)
        self.name = player_name

    def players_name(self, name):
        self.handed = []
        self.name = name
        name = input("Enter your name:\n")  # input AFTER setting the same wont change it (i think)
        # your init sets the name, i dont get why you would need that

    # im a little confused here, what is that?
    def __add__(self, dealer, other):
        isinstance(other, Card)
        self.dealer = self.handed + other

    # removed dealer's value, the next function replaces it:
    def card_value(self):
        current_sum = 0
        last_card = 0
        aces_count = 0
        for card in self.handed:
            last_card = card.point_value()
            if last_card != -1:
                current_sum += last_card
            elif card.value in ('J', 'Q', 'K'):
                current_sum += 10
            elif card.value == 'A':
                current_sum += 11  # why do i ignore the 1?

        while current_sum > 21 and aces_count > 0:
            current_sum -= 10
            aces_count -= 1
        return current_sum

    # i am VERY lazy
    def report_sum(self):
        print(self.name, self.card_value())

    def card_adder(self, card):
        self.handed.append(card)

    # added new overload for random cards
    def card_adder(self):
        self.handed.append(Card())

    def owned_cards(self):
        print(self.name)
        for card in self.handed:
            Card.display(card)
            # telling it explicitly that ot need to display the card
            # notice that the current 'self' is actually the Player, not the card so you need to pass it


class Points:
    def __init__(self, points):
        points_sum = sum('self.value')


def main():
    print(logo)

    card_ran = Card()  # using the empty init to get a random card
    card_ran.display()

    player_1 = Player()  # removed the given name so it'll use the empty init
    player_1.card_adder()
    player_1.card_adder()
    player_1.owned_cards()

    dealer = Player('dealer')
    dealer.card_adder()
    dealer.card_adder()
    dealer.owned_cards()

    player_1.report_sum()
    dealer.report_sum()

    if player_1.card_value() < 21:
        answer = input('Do you want to draw a card? (y)\n')
        while answer == 'y' and player_1.card_value() < 21:
            player_1.card_adder()
            player_1.report_sum()
            answer = input('Do you want to draw a card? (y)\n')

    players_sum = player_1.card_value()
    dealers_sum = dealer.card_value()
    player_1.report_sum()
    dealer.report_sum()

    # if players_sum <= 17:
    #     print(f"Your sum is smaller than 17. (it's {players_sum})")
    #     player_1.card_adder(card_ran)
    #     player_1.owned_cards()
    # elif dealers_sum <= 17:
    #     print(f"The dealers sum is smaller than 17. (it's {dealers_sum})")
    #     dealer.card_adder(card_ran)
    #     dealer.owned_cards()
    # elif players_sum <= 17 or dealers_sum and value == "A":
    #     changed_value = value.replace('A', 1)
    # else:
    #     pass

    if players_sum > 21:  # again, great, clear and short prints
        print("OH no, your sum is bigger than 21 :(.\nYou lost")
    elif dealers_sum > 21:
        print("Your lucky, the dealers sum is bigger than 21 :).\nYou won")
    elif players_sum == dealers_sum:
        print("Its a draw ,play once more to win :)")
    elif players_sum > dealers_sum:
        print("you won! :)")
    elif players_sum < dealers_sum:
        print("OH no :(. You lost \nTry again to win :)")  # writing '\n ' leaves a gap before the next line
    else:
        print("There's a problem")


main()
