Solitaire_bot is a bot that solves solitaires for you, so you dont have to do it

This project contains a file named "solitaire.py" whitch is the custom library for this project.
It has these functions:
  #   __init__
    When you create an instance of this library, you can choose wether you want to see the cards that are face down or not

  #   setup()
    Does the setup for the game; Suffles the deck and puts down the cards

  #   shuffle(deck)
    Shuffles the given deck

  #   print_board()
    Prints the board as it's usually played to the console

  #   put_to_foundations(from)
    Tries to put the fist card from the deck in ithe given index into the foundations.
    Returns bool whether is was successful or not
    
  #   get_from_foundations(from, to)
    Tries to put the top card from the founration at that index into the pile at the given index.
    Returns bool whether is was successful or not

  #   put_to_pile(from, to)
    Tries to put the first open card in the pile in the first index into the top of the pile at the given index
    Returns bool whether is was successful or not
    
  #   get_from_stock()
    Tries to get the correct amount of cards from the stock to the talon.
    If there is no stock left, flip the talon.
    Returns false if it wasn't able to do nether if those, and true if it was
    
  #   flip_the_talon()
    Takes all the cards from the talon and flips them to the stock if there are flips aveilable
    Returns bool whether is was successful or not
  
Note: The talon pile is usually referd to as the index 7


The bot file is a bot that solves one game of solitaire.
The runner constantly makes bot solve the game and prints out how many percent of games it has won
  
