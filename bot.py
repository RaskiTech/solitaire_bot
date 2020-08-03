import solitare

# Get the talon card with game.talon[-1]


#  🪄 🪄 🪄 🪄
# pile:
#  0      1       2      3      4      5      6
# ♦1      🃏      🃏      🃏      🃏      🃏      🃏
#        ♦3      🃏      🃏      🃏      🃏      🃏
#               ♦6      🃏      🃏      🃏      🃏
#                      ♦10     🃏      🃏      🃏
#                             ♣2      🃏      🃏
#                                    ♣8      🃏
#                                           ♥2
#
# 🃏 ♥5     - pile 7


#   Commands:
#
#   setup()
#   shuffle(deck)
#   print_board()
#   put_to_foundations(from)
#   put_to_pile(from, to)
#   flip_the_talon()
#   get_from_stock()

def solve():
    game = solitare.Game(False)
    game.setup()
    game.take_from_foundations(1, 4)
    #game.print_board()

    not_done = True
    while not_done:
        not_done = False

        while can_change_pile(game):  # Doesn't need to set not_done since it's the first one
            continue  # and everything can still be done after

        while can_put_to_foundations(game):# if can_put_to_foundations(game):
            not_done = True
            continue

        # If can't move anything anymore, get from the pile
        if not not_done:
            # If can get something from the foundations so the stock card can be placed


            # If can get from the pile
            if game.get_from_stock():
                #game.print_board()
                not_done = True

    #game.print_board()
    # Check if the board is complete
    for i in range(4):
        if game.foundations[i] != 13:
            break
    else:
        return True
    return False


def can_change_pile(game):
    # Check if can move something in the piles
    for i in range(len(game.tableau)):  # +1 for the talon
        for j in range(len(game.tableau)):
            if i == j:
                continue
            if game.put_to_pile(6 - i, 6 - j):
                #game.print_board()
                return True
    for i in range(len(game.tableau)):
        if game.put_to_pile(7, i):
            #game.print_board()
            return True
    return False

  
def can_put_to_foundations(game):
    # Check if something can be put to the foundations
    for i in range(len(game.tableau) + 1):  # +1 for the talon
        if game.put_to_foundations(i):
            #game.print_board()
            return True
    else:
        return False


