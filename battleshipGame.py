# Battleship Game
"""
The objective of the game is to guess the location of a ship
on a 5x5 board. The position of a ship is selected at random.
"""

from random import randint

def build_board():
    """
    Constructing a board consisting of 5x5 squares.
    Returns: a board, a list of lists
    """
    boardSize = 6
    board = []
    row = []
    for i in range(boardSize):
        row.append(str(i))  
    board.append(row)
    for x in range(1, boardSize):
        board.append([str(x)] + ["O"] * (boardSize-1))
        
    return board

def print_board(board):
    """
    Prints the game board.
    """
    for row in board:
        print " ".join(row)
    print

def random_row(board):
    """
    Randomly chooses a row (an int), in which the ship will be anchored.
    Returns: an int
    """
    return randint(1, len(board) - 1)

def random_col(board):
    """
    Randomly chooses a column (an int), in which the ship will be anchored.
    Returns: an int
    """
    return randint(1, len(board[0]) - 1)

def play(board, ship_row, ship_col):
    """
    Shows a 5x5 board and asks the Player to guess, where
    the ship is (row and column). The Player has limited number
    of guesses (turns). After each guess they receive feedback.
    If they miss, their guess is marked upon the board with an "X".
    If they cannot give a valid guess, they still lose a turn.
    If they run out of turns, they lose and the game is over.
    If they guess the location of the ship, they win the game.
    """
    turns = 4
    print "Ahoy! Hands off me booty, ye skirt wearing ballast pig!"
    print "Ye have %d guesses to sink me ship or I'll devour yer parrot!" %(turns)

    # Uncomment to cheat:
    #print "\nHere's a map for ye, ye cargo thievin' sorry sea dog!"
    #print "Ship row: %d" %ship_row
    #print "Ship column: %d" %ship_col

    for turn in range(1, turns+1):
        print "\nTurn: %d" %turn
        print_board(board)
        guess_row = raw_input("Guess Row (1-%d): " %(len(board)-1)) 
        guess_col = raw_input("Guess Column (1-%d): " %(len(board)-1)) 
        try:
            if int(guess_col) == ship_col and int(guess_row) == ship_row:
                board[int(guess_row)][int(guess_col)] = "V"
                print_board(board)
                return "Shiver me timbers! Ye sank me battleship! :("
            else:
                if int(guess_row) >= len(board) or int(guess_col) >= len(board)\
                   or int(guess_row) <= 0 or int(guess_col) <= 0:
                    print "\nBlimey! That's not even in the ocean, ye grog-snarfing monkey!"
                elif board[int(guess_row)][int(guess_col)] == "X":
                    print "\nYou guessed that one already, you scurvy scoundrel!"
                else:
                    print "\nYo Ho Ho and a bottle of rum! Ye missed me battleship!"
                    board[int(guess_row)][int(guess_col)] = "X"
        except ValueError:
            print "\nI accept only stinking rose smelling digits, savvy?"
    print
    print_board(board)
    return "You fight like a cow, matey! Me ship was at %s. Now ye'll walk the plank. :)" \
           %((ship_row, ship_col),)

board = build_board()
ship_row = random_row(board)
ship_col = random_col(board)
print play(board, ship_row, ship_col)
