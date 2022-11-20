from random import randint

# Legend
# "@" for placing ship
# " " for available space
# "X" for hit battleship
# "-" for missed shot

HIDDEN_BOARD = [[" "] * 8 for x in range(8)]
# creates a list of 8 spaces, 8 times
GUESS_BOARD = [[" "] * 8 for x in range(8)]
# creates a list of 8 spaces, 8 times
USER_BOARD = [[" "] * 8 for x in range(8)]
# creates a list of 8 spaces, 8 times

letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4,
                      "F": 5, "G": 6, "H": 7}
# converts letters to numbers

numbers_to_letters = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E",
                      5: "F", 6: "G", 7: "H"}
# converts numbers to letters

user_score = 0
computer_score = 0

continue_playing_options = ["y", "yes", "n", "no"]

