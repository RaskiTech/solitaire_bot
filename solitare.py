import random

# Suits: diamond♦, club♣, heart♥, spade♠
SUITS = ("♦", "♣", "♥", "♠")


def can_put_to_top(bottom_card, top_card):
    if are_colors_different(bottom_card, top_card):
        return True if bottom_card.number + 1 == top_card.number else False
    return False


def are_colors_different(card_1, card_2):
    if card_1.suit_index == 0 or card_1.suit_index == 2:
        if card_2.suit_index == 1 or card_2.suit_index == 3:
            return True
    elif card_1.suit_index == 1 or card_1.suit_index == 3:
        if card_2.suit_index == 0 or card_2.suit_index == 2:
            return True
    return False


class Game:

    def __init__(self, see_all):
        self.SEE_ALL = see_all
        self.flip_amount = 4
        self.foundations = [0, 0, 0, 0]
        self.stock = [] # The stock pile
        self.talon = [] # The talon pile
        for i in range(4):
            for j in range(1, 14):
                self.stock.append(Card(j, i, False))
        self.tableau = [[], [], [], [], [], [], []]

    # Shuffles the given deck
    def shuffle(self, deck):
        random.shuffle(deck)

    # Does the setup for the game
    def setup(self):
        self.shuffle(self.stock)
        # build the tableau
        for i in range(7):
            self.tableau[i] = []
            for j in range(i):
                self.tableau[i].append(self.stock[0])
                self.stock.pop(0)
            self.stock[0].face_up = True
            self.tableau[i].append(self.stock[0])
            self.stock.pop(0)

    def get_from_stock(self):
        if len(self.stock) != 0:
            num = 3 if self.flip_amount != 1 else 1
            for i in range(num):
                if len(self.stock) != 0:
                    self.stock[0].face_up = True
                    self.talon.append(self.stock[0])
                    self.stock.pop(0)
            #print(f"\nuusi kortti ({num})")
            return True
        # Flip the talon over
        else:
            return self.flip_the_talon()

    def flip_the_talon(self):
        if len(self.stock) == 0 and len(self.talon) != 0 and self.flip_amount > 1:
            for i in range(len(self.talon)):
                self.talon[i].face_up = False
            self.stock = list(self.talon)
            self.talon.clear()
            self.flip_amount -= 1
            #print("\npakan kääntö")
            return True
        else:
            # print("flipped the talon without meeting requirements")
            return False

    def put_to_foundations(self, row_index):
        if row_index >= 7:
            if len(self.talon) == 0:
                return False
            card = self.talon[-1]
        else:
            if len(self.tableau[row_index]) == 0:
                return False
            card = self.tableau[row_index][-1]

        # If can be put
        if self.foundations[card.suit_index] == card.number - 1:
            self.foundations[card.suit_index] += 1
            if row_index < 7:
                self.tableau[row_index].pop()
                # Open the card below
                if len(self.tableau[row_index]) != 0:
                    self.tableau[row_index][-1].face_up = True
            else:
                self.talon.pop()
            #print("\nkortti ässiin")
            return True
        else:
            return False

    def take_from_foundations(self, suit_index, row_index):
        if row_index >= 7:
            return False
        if len(self.tableau[row_index]) == 0:
            return False
        tab_card = self.tableau[row_index][-1]
        fou_card = Card(self.foundations[suit_index], suit_index, True)
        if not can_put_to_top(tab_card, fou_card):
            return False

        # The card can be placed
        self.foundations[suit_index] -= 1
        self.tableau[row_index].append(fou_card)
        #print("\nkortti ässistä")
        return True

    def put_to_pile(self, original_row, new_row):
        if original_row < 7:
            if len(self.tableau[original_row]) == 0:
                return False
            elif self.tableau[original_row][0].number == 13 and self.tableau[original_row][0].face_up:
                return False  # This so the program doesn't change king pos infinitely

            # What position to move from
            for i in range(len(self.tableau[original_row])):
                original_card = self.tableau[original_row][i]
                if original_card.face_up:
                    pop_point = i  # Where to start moving the cards
                    break
            else:
                print(f"The pile {original_row} doesn't have any cards face up")
                pop_point = len(self.tableau[original_row]) - 1
                original_card.face_up = True
            # Only kings can move to a new place
            if len(self.tableau[new_row]) == 0 and original_card.number != 13:
                return False  # Can't move random cards at the start
        else:
            if len(self.talon) == 0:
                return
            elif len(self.tableau[new_row]) == 0 and self.talon[-1].number != 13:
                return
            # Get from the talon
            original_card = self.talon[-1]
        if len(self.tableau[new_row]) != 0:
            new_card = self.tableau[new_row][-1]
            cont = False
        else:
            cont = True

        # Check if can be put
        if not cont:
            cont = can_put_to_top(original_card, new_card)

        if cont:
            # Put to the pile
            if original_row < 7:
                move_amount = len(self.tableau[original_row]) - pop_point
                # Move and pop the cards
                for i in range(move_amount):
                    self.tableau[new_row].append(self.tableau[original_row][pop_point])
                    self.tableau[original_row].pop(pop_point)
                # Unlock the back-card
                if pop_point != 0:
                    self.tableau[original_row][pop_point - 1].face_up = True
            else:
                self.tableau[new_row].append(original_card)
                self.talon.pop()
            #print("\nkortin siirto")
            return True
        else:
            return False

    def print_board(self):
        # Foundations
        string = ""
        for i in range(len(self.foundations)):
            string += f"{SUITS[i]}{self.foundations[i]} " if self.foundations[i] != 0 else "🪄 "
        print(string + "\n")

        # The tableau
        do_loop = True
        i = -1 # -1 Because it gets bigger right away
        while do_loop:
            i += 1
            string = ""
            for j in range(7):
                if i >= len(self.tableau[j]):
                    string += "       "
                else:
                    # () if the card is upside down
                    if self.tableau[j][i].face_up:
                        string += f" {SUITS[self.tableau[j][i].suit_index]}{self.tableau[j][i].number}   "
                    else:
                        if self.SEE_ALL:
                            string += f"({SUITS[self.tableau[j][i].suit_index]}{self.tableau[j][i].number})  "
                        else:
                            string += "  🃏    "
                        #            "i       i"
                    # extra space is number is <10 because it takes less space
                    if self.tableau[j][i].number < 10 and (self.tableau[j][i].face_up or self.SEE_ALL):
                        string += " "
            print(string)
            if string.isspace():
                do_loop = False

        # The stock and the talon
        string = " " if len(self.stock) == 0 else "🃏"
        if len(self.talon) != 0:
            string += f" {SUITS[self.talon[-1].suit_index]}{self.talon[-1].number}"
        string += "\n"
        print(string)


class Card:
    def __init__(self, number, suit_index, face_up):
        self.number = number
        self.suit_index = suit_index
        self.face_up = face_up
