'''
Tic Tac Toe Game
'''

import random
import os

# ==========================
# Game Variable Setup
# ==========================

BOARD_DELIMITER = ' | '
VALID_SELECTION_OPTIONS = '123456789'
NUMBER_OF_BOARD_SQUARES = 9
ROW_LENGTH = 3
BOARD_START_SQUARE = 0
DEFAULT_USER_SYMBOL = 'X'
DEFAULT_COMPUTER_SYMBOL = 'O'
SQUARES_AVAILABLE_TITLE = '\n\n=== SQUARES AVAILABLE ===\n'
GAME_BOARD_TITLE = '\n\n=== CURRENT GAME BOARD ===\n'
board = { '1': '_',
          '2': '_',
          '3': '_',
          '4': '_',
          '5': '_',
          '6': '_',
          '7': '_',
          '8': '_',
          '9': '_',
        }
BOARD_VALUES = board.values()
GAME_VALUES = {}

# ==========================
# Game Running Functions
# ==========================

def init():
    '''
    Reset initial conditions of game
    Return None
    '''
    GAME_VALUES['user_turn_count'] = 0
    GAME_VALUES['computer_turn_count'] = 0
    GAME_VALUES['user_moves'] = set()
    GAME_VALUES['computer_moves'] = set()
    GAME_VALUES['whose_turn'] = 'user'
    GAME_VALUES['winning_condition'] = False
    GAME_VALUES['winner'] = None
    GAME_VALUES['error_messages'] = []
    GAME_VALUES.setdefault('user_symbol', DEFAULT_USER_SYMBOL)
    GAME_VALUES.setdefault('computer_symbol', DEFAULT_COMPUTER_SYMBOL)
    GAME_VALUES.setdefault('winning_combos', winning_combos())
    GAME_VALUES.setdefault('winning_combo_sets', winning_combo_sets())
    GAME_VALUES.setdefault('defensive_combos', defensive_combos())
    GAME_VALUES.setdefault('defensive_combo_sets', defensive_combo_sets())
    GAME_VALUES['simple_ai_moves'] = simple_ai_moves()
    for key in board:
        board[key] = '_'

def run():
    '''
    Runs Program
    '''
    select_first_player()
    while True:
        print_status_for_selection()
        play_turn()
        assess_winning_condition()
        if is_game_over():
            break
        update_ai_moves()
        change_turns()
    clear_screen()
    print_board()
    print_end_game_message()

# ==========================
# Game Play Functions
# ==========================

def welcome():
    '''
    Clears screen
    Welcomes user
    Asks what symbol to use
    Displays board
    Returns None
    '''
    clear_screen()
    print('Welcome to Tic Tac Toe!')
    update_symbols_used()


def play_turn():
    '''
    Plays the current turn
    '''
    if is_user_turn():
        user_move()
    else:
        computer_move()

def change_turns():
    '''
    Swaps turn of players
    '''
    if is_user_turn():
        GAME_VALUES['whose_turn'] = 'computer'
    else:
        GAME_VALUES['whose_turn'] = 'user'

def user_move():
    '''
    Takes user input for selection
    Validates selection
    Updates board with valid selection
    Returns None
    '''
    while True:
        user_selection = input('\nSelect Square: ')
        if not is_valid_user_selection(user_selection):
            print_error_messages()
        else:
            board[user_selection] = GAME_VALUES['user_symbol']
            GAME_VALUES['user_moves'].add(user_selection)
            GAME_VALUES['user_turn_count'] += 1
            break

def computer_move():
    '''
    Generates computer selection from available squares
    Updates board with computer selection
    Returns None
    '''
    clear_screen()
    ai_move = check_for_ai_move()
    print('Computer is selecting ...')
    half_second_pause()
    if ai_move:
        computer_selection = ai_move
    else:
        computer_selection = random.choice(available_squares())
    GAME_VALUES['computer_moves'].add(computer_selection)
    board[computer_selection] = GAME_VALUES['computer_symbol']
    GAME_VALUES['computer_turn_count'] += 1
    print(F"Computer Selected Square {computer_selection}")
    one_second_pause()

# ==========================
# Game Board Stats
# ==========================

def assess_winning_condition():
    '''
    Updates winning conditions in GAME_VALUES if there is a winner
    '''
    if is_user_turn():
        if has_winning_combo(user_squares()):
            GAME_VALUES['winning_condition'] = True
            GAME_VALUES['winner'] = 'user'
    else:
        if has_winning_combo(computer_squares()):
            GAME_VALUES['winning_condition'] = True
            GAME_VALUES['winner'] = 'computer'

def user_squares():
    '''
    Returns all squares user has selected
    '''
    return sorted([ square for square, value in board.items()
                    if value == GAME_VALUES['user_symbol']])

def computer_squares():
    '''
    Returns all squares computer has selected
    '''
    return sorted([ square for square, value in board.items()
                    if value == GAME_VALUES['computer_symbol']])

def available_squares():
    '''
    Returns squares that have not been selected
    '''
    return [ k for k, v in board.items() if v == '_' ]

def square_numbers_available():
    '''
    Returns an array of numbers or spaces if the square is available to select
    or not
    '''
    return [ square_num if value == '_' else ' '
                        for square_num, value in board.items() ]

def square_numbers_not_available():
    '''
    Returns squares that have been selected
    '''
    return [ k for k, v in board.items() if v != '_' ]

# ==========================
# GAME_VALUES updates
# ==========================

def update_symbols_used():
    '''
    Asks user if they would like to use 'X' or 'O' for their symbol
    Updates user_symbol and computer_symbol as necessary
    Returns None
    '''
    while True:
        message = [F"Your board symbol is {GAME_VALUES['user_symbol']}",
                   F"Would you like {GAME_VALUES['computer_symbol']} instead? (y/n): "
                  ]
        selection = input('\n'.join(message)).casefold()
        if selection in 'yn':
            break
        clear_screen()
        print('Invalid selection, please try again')
    if selection == 'y':
        GAME_VALUES['user_symbol'] = 'O'
        GAME_VALUES['computer_symbol'] = 'X'

def select_first_player():
    '''
    Changes who goes first at the start of the game
    '''
    clear_screen()
    print('Press 1 for User\nPress 2 for Computer')
    while True:
        selection = input('Select who goes first: ')
        if selection in '12':
            break
        print('Invalid selection, please try again')
    if selection == '2':
        change_turns()

# =========================
# AI
# =========================

def check_for_ai_move():
    '''
    Returns a smart move if there is one available
    Checks for Offensive moves first
    Then Defensive
    Returns False if no good move available
    '''
    offensive_move = check_for_offensive_move()
    if offensive_move:
        return offensive_move
    return check_for_defensive_move()

def check_for_defensive_move():
    '''
    Returns square for best offense or defense move
    Returns False if none available
    '''
    if len(GAME_VALUES['user_moves']) < 2:
        return False
    for move_set, square in GAME_VALUES['simple_ai_moves'].items():
        if len(move_set - GAME_VALUES['user_moves']) == 0:
            return square
    return False

def check_for_offensive_move():
    '''
    Returns square for best offense move
    Returns False if none available
    '''
    if len(GAME_VALUES['computer_moves']) < 2:
        if is_square_5_open():
            return '5'
        return False
    for move_set, square in GAME_VALUES['simple_ai_moves'].items():
        if len(move_set - GAME_VALUES['computer_moves']) == 0:
            return square
    return False

def update_ai_moves():
    '''
    Mutates GAME_VALUES['simple_ai_moves'] dictionary and removes items where the
    square has been seleted
    Returns None
    '''
    keys_to_remove = []
    used_squares = square_numbers_not_available()
    for key, square in GAME_VALUES['simple_ai_moves'].items():
        if square in used_squares:
            keys_to_remove.append(key)
    for key in keys_to_remove:
        del GAME_VALUES['simple_ai_moves'][key]

def winning_combos():
    '''
    Returns list of winning combo strings
    '''
    return ['123', '456', '789', '147', '258', '369', '159', '357']

def winning_combo_sets():
    '''
    Returns set versions of winning combos
    '''
    return [ set(s) for s in GAME_VALUES['winning_combos'] ]

def defensive_combos():
    '''
    Returns:
    [['12', '13', '23'], ['45', '46', '56'], ['78', '79', '89'],
    ['14', '17', '47'], ['25', '28', '58'], ['36', '39', '69'],
    ['15', '19', '59'], ['35', '37', '57']]
    '''
    return [ [s[0]+s[1], s[0]+s[2], s[1]+s[2]]
                    for s in GAME_VALUES['winning_combos'] ]

def defensive_combo_sets():
    '''
    Returns
    [{'2', '1'}, {'1', '3'}, {'2', '3'}, {'4', '5'}, {'4', '6'}, {'6', '5'},
     {'8', '7'}, {'7', '9'}, {'8', '9'}, {'1', '4'}, {'7', '1'}, {'7', '4'},
     {'2', '5'}, {'2', '8'}, {'8', '5'}, {'6', '3'}, {'9', '3'}, {'9', '6'},
     {'1', '5'}, {'1', '9'}, {'9', '5'}, {'5', '3'}, {'7', '3'}, {'7', '5'}]
    '''
    return [ frozenset(pair) for row_combo in GAME_VALUES['defensive_combos']
                             for pair in row_combo ]

def simple_ai_moves():
    '''
    Returns dictionary of all combos where one more move wins
    { { squares_taken }: winning_square }
    ex: { {'1', '2'}: '3' }
    '''
    d = {}
    for winning_combo in GAME_VALUES['winning_combo_sets']:
        for def_combo in GAME_VALUES['defensive_combo_sets']:
            diff = winning_combo - def_combo
            if len(diff) == 1:
                d.setdefault(def_combo, diff.pop())

    return d

# Returns
#   {frozenset({'1', '2'}): '3', frozenset({'1', '3'}): '2',
#    frozenset({'3', '2'}): '1', frozenset({'4', '5'}): '6',
#    frozenset({'4', '6'}): '5', frozenset({'5', '6'}): '4',
#    frozenset({'7', '8'}): '9', frozenset({'7', '9'}): '8',
#    frozenset({'9', '8'}): '7', frozenset({'4', '1'}): '7',
#    frozenset({'7', '1'}): '4', frozenset({'4', '7'}): '1',
#    frozenset({'5', '2'}): '8', frozenset({'8', '2'}): '5',
#    frozenset({'5', '8'}): '2', frozenset({'3', '6'}): '9',
#    frozenset({'9', '3'}): '6', frozenset({'9', '6'}): '3',
#    frozenset({'1', '5'}): '9', frozenset({'1', '9'}): '5',
#    frozenset({'9', '5'}): '1', frozenset({'5', '3'}): '7',
#    frozenset({'7', '3'}): '5', frozenset({'7', '5'}): '3'}

# ==========================
# Predicate Functions
# ==========================

def is_user_winner():
    '''
    Returns true if user won
    '''
    return GAME_VALUES['winner'] == 'user'

def is_game_over():
    '''
    Returns True or False if game over
    '''
    return is_winning_condition_achieved() or has_no_more_squares_left()

def is_winning_condition_achieved():
    '''
    Returns True or False if there is a winning condition present
    '''
    return GAME_VALUES['winning_condition'] is True

def has_no_more_squares_left():
    '''
    Returns True if there aren't any empty squares left
    '''
    return len([ value for value in BOARD_VALUES if value == '_' ]) == 0

def has_winning_combo(squares_selected):
    '''
    Determines if squares selected are winning squares
    Returns True if yes, False otherwise
    '''
    for winning_set in GAME_VALUES['winning_combo_sets']:
        if len(winning_set - set(squares_selected)) == 0:
            return True
    return False

def is_user_turn():
    '''
    Returns True or False if it is the user's turn
    '''
    return GAME_VALUES['whose_turn'] == 'user'

def is_computer_turn():
    '''
    Returns True or False if it is the computer's turn
    '''
    return GAME_VALUES['whose_turn'] == 'computer'

def has_no_winning_condition():
    '''
    Returns True or False if there is NOT a winning condition present
    '''
    return GAME_VALUES['winning_condition'] is False

def is_valid_user_selection(user_selection):
    '''
    Tests if user input is valid
    Sets an error message if the input is invalid
    Returns True if selection is valid, or False otherwise
    '''
    if user_selection not in VALID_SELECTION_OPTIONS or \
            len(user_selection) == 0:
        set_error_message('That is not a valid input')
        return False
    if board[user_selection] != '_':
        set_error_message('That square is already taken')
        return False
    return True

def is_square_5_open():
    '''
    Returns True if square 5 is open, False otherwise
    '''
    return '5' in square_numbers_available()

# ==========================
# PRINTING FUNCTIONS
# ==========================

def print_end_game_message():
    '''
    Prints if there is a winner or cats game
    '''
    if is_winning_condition_achieved():
        print_winner_message()
    else:
        print("Cat's Game!")

def print_winner_message():
    '''
    Prints appropriate message for who won
    Returns None
    '''
    if is_user_winner():
        print("Congrats you beat the computer!")
        print(F"You won in {GAME_VALUES['user_turn_count']} moves!")
    else:
        print(F"Computer won this time in {GAME_VALUES['computer_turn_count']} moves")
        print("Better luck next time")

def print_status_for_selection():
    '''
    Function to administer printing board for selection and
    current board status
    Prints squares available for selection
    Prints current status of board
    Returns None
    '''
    clear_screen()
    print_squares_available()
    print_board()

def print_board():
    '''
    prints board by rows
    Returns None
    '''
    print_board_title()
    for i in range(BOARD_START_SQUARE, NUMBER_OF_BOARD_SQUARES, ROW_LENGTH):
        row = BOARD_DELIMITER.join(list(BOARD_VALUES)[i:i+3])
        print(row.center(25))

def print_squares_available():
    '''
    Prints square numbers available for selection
    Returns None
    '''
    squares_available = square_numbers_available()
    print_squares_available_title()
    for i in range(BOARD_START_SQUARE, NUMBER_OF_BOARD_SQUARES, ROW_LENGTH):
        row = BOARD_DELIMITER.join(squares_available[i:i+3])
        print(row.center(25))

def print_board_title():
    '''
    Prints title when displaying board
    Returns None
    '''
    print(GAME_BOARD_TITLE)

def print_squares_available_title():
    '''
    Prints title when displaying board
    Returns None
    '''
    print(SQUARES_AVAILABLE_TITLE)

# ==========================
# Utility Functions
# ==========================

def clear_screen():
    '''
    Clears terminal screen
    Returns None
    '''
    os.system('clear')

def half_second_pause():
    '''
    Half second pause to add to game feel with computer
    Returns None
    '''
    os.system('sleep 0.5')

def one_second_pause():
    '''
    One second pause to add to game feel with computer
    Returns None
    '''
    os.system('sleep 1')

# ==========================
# Error Message Handling
# ==========================

def set_error_message(message):
    '''
    Clears error messages
    Appends message to GAME_VALUES['error_messages'] list
    '''
    clear_error_messages()
    GAME_VALUES['error_messages'].append(message)


def clear_error_messages():
    '''
    Clears error messages list
    '''
    GAME_VALUES['error_messages'].clear()

def print_error_messages():
    '''
    Prints all messages from error messages list
    '''
    for message in GAME_VALUES['error_messages']:
        print(message)

# ==========================
#       Start the game
# ==========================

init()
welcome()
while True:
    run()
    again = input('Play Again?: ')
    if again not in 'yY':
        break
    init()
