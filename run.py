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

# Python program to print colored text and background, code taken from Geeks for Geeks, see README

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))


def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))


def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))


def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))


def print_board(board):

    """
    Creates a board with letters for the columns and numbers for the rows
    """
    print("  A B C D E F G H")
    print("  ---------------")
    row_number = 1
    for row in board:
        print(row_number, "|".join(row))
        row_number += 1

def create_ships(board):

    """
    Creates a random integer between 0 and 7 for ship_row and ship_column
    Checks if "@" is already on the board, if so runs randomint until
    there is an available space
    When there is an available space update with "@"
    """
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == "@":
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = "@"

def computer_guess(board):
    """
    Creates a random integer between 0 and 7 for computer_row and
    computer_column
    Checks if "-" or "X" is already on the board, if so runs randomint until
    there is an available space
    If computer_row and computer_column is "@", prints message to user to say
    their ship has been hit and updates board with "X"
    Else the computer_row and computer_column finds a blank space, prints
    message to the user to say the computer has missed and updates the
    board with "-"
    """
 global computer_score
    computer_row, computer_column = randint(0, 7), randint(0, 7)
    if (USER_BOARD[computer_row][computer_column] == "-" or
            USER_BOARD[computer_row][computer_column] == "X"):
        computer_row = randint(0, 7)
        computer_column = randint(0, 7)
    elif USER_BOARD[computer_row][computer_column] == "@":
        prCyan(f"{username}, your battleship has been hit!")
        prCyan(
            f"The computer guessed row {computer_row +1}"
            f" and column {numbers_to_letters[computer_column]}")
        USER_BOARD[computer_row][computer_column] = "X"
        computer_score += 1
    else:
        prCyan(f"Phew {username}, the computer missed!")
        prCyan(
            f"The computer guessed row {computer_row +1}"
            f" and column {numbers_to_letters[computer_column]}")
        USER_BOARD[computer_row][computer_column] = "-"

def get_ship_location():

    row = input("Please enter a ship row 1-8\n")
    while row not in "12345678" or len(row) > 1 or row == "":
        validate_row(row)
        print("Please enter a valid row")
        row = input("Please enter a ship row 1-8\n")
    column = input("Please enter a ship column A-H\n").upper()
    while column not in "ABCDEFGH" or len(column) > 1 or column == "":
        validate_column(column)
        print("Please enter a valid column")
        column = input("Please enter a ship column A-H\n").upper()
    return int(row) - 1, letters_to_numbers[column]

