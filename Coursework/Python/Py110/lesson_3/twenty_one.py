'''
21 BlackJack
'''

import random
import os
import copy

# ==================
# Constants
# ==================

# Card Names
LOW_CARD_NAMES = [ '2', '3', '4', '5', '6', '7', '8', '9', '10' ]
FACE_CARD_NAMES = [ 'Jack', 'Queen', 'King', 'Ace' ]
CARD_NAMES = LOW_CARD_NAMES + FACE_CARD_NAMES

# Card Values
LOW_CARD_VALUES = list(range(2,11))
FACE_CARD_VALUES = [ 10, 10, 10, 11 ]
CARD_VALUES = LOW_CARD_VALUES + FACE_CARD_VALUES

# Deck Constant
CARD_VALUE_TABLE = dict(zip(CARD_NAMES, CARD_VALUES))
SUITE_NAMES = [ 'Spades', 'Clubs', 'Hearts', 'Diamonds' ]
DECK_REFERENCE = { F"{name} of {suite}": value for suite in SUITE_NAMES
                              for name, value in CARD_VALUE_TABLE.items()}
# AI Risk Levels
LOW_RISK_VALUE = 15
MEDIUM_RISK_VALUE = 17
HIGH_RISK_VALUE = 20
AI_RISK_LEVELS = {
        'low': LOW_RISK_VALUE,
        'medium': MEDIUM_RISK_VALUE,
        'high': HIGH_RISK_VALUE
        }

# Display Constants
MAX_CARD_NAME_LENGTH = max(len(title) for title in DECK_REFERENCE)
CARD_HORIZ = MAX_CARD_NAME_LENGTH + 2
TOP_BAR = '=' * 80
HIDDEN_CARD = '?????'

# Gameplay Constants
AI_DELAY = 1.5
END_ROUND_DELAY = 2
BUST_VALUE = 22
GAME_VALUES = {}
PLAYER_INFO = {'name': None,
               'player_number': None,
               'player_type': None,
               'hand': [],
               'hand_values': [],
               'alt_hand_values': [],
               'cards_in_hand': 0,
               'hand_value': 0,
               'alt_hand_value': 0,
               'public_hand_value': 0,
               'alt_public_hand_value': 0,
               'score': 0,
               'has_alt_hand_value': False,
               'has_busted': False,
               'turn_ended': False,
               # risk_level: ai and dealer players only
               }


# ==================
# Game Play
# ==================

def init_new_game():
    '''
    Initiates new game values
    Returns None
    '''
    GAME_VALUES['deck'] = list(DECK_REFERENCE.keys())
    GAME_VALUES['num_players'] = None
    GAME_VALUES['players'] = []
    GAME_VALUES['busted_players'] = []
    GAME_VALUES['error_messages'] = []
    GAME_VALUES['rankings'] = None
    GAME_VALUES['winners'] = []
    GAME_VALUES['num_winners'] = 0
    GAME_VALUES['winning_score'] = 0
    shuffle_deck()
    determine_number_of_players()
    initialize_players()

def run():
    '''
    Runs the game
    Returns None
    '''
    init_new_game()
    deal_cards()
    play_rounds()
    evaluate_results()
    display_results()
    enter_to_continue()

def welcome():
    '''
    Displays welcome screen
    Returns None
    '''
    clear_screen()
    print('Welcome to 21 Black Jack!')
    print("\n\t• Goal: Get as close to 21 as possible without going over.")
    print("\t• Everyone is dealt 2 cards")
    print("\t• Computer player's first card is hidden")
    print("\t• Options: 'Hit' to add cards, 'Stay' to hold your total.")
    print("\t• Going over 21 is a 'bust', resulting in an automatic loss.")
    print("\t• Dealer wins tie breakers")
    print("\nGood Luck!")

# ==================
# Round Play
# ==================

def play_rounds():
    '''
    Goes through each player and plays their round
    Returns None
    '''
    for player in GAME_VALUES['players']:
        clear_screen()
        display_table()
        if player['player_type'] == 'human':
            enter_to_continue()
            play_user_round(player)
        else:
            play_ai_round(player)
        player['turn_ended'] = True
        clear_screen()
        display_table()
        enter_to_continue()

def play_user_round(player):
    '''
    Takes input from User whether to hit or stay
    Returns None
    '''
    while not player['has_busted']:
        clear_screen()
        display_player(player, True)
        display_error_messages()
        player_selection = input('\nWould you like to hit or stay? (h/s): ').casefold()
        if player_selection not in 'hs' or len(player_selection) == 0:
            GAME_VALUES['error_messages'].append('Invalid selection, please try again')
        elif player_selection == 's':
            break
        else:
            hit(player)

def play_ai_round(player):
    '''
    Plays AI round
    Returns None
    '''
    while (not player['has_busted']) and \
          (player['hand_value'] <= AI_RISK_LEVELS[player['risk_level']]):
        clear_screen()
        display_player(player, True)
        hit(player)
        display_ai_round_play_hit(player)
    display_ai_round_play_stay(player)

# ==================
# Initialization Functions
# ==================

def determine_number_of_players():
    '''
    Asks for how many players will play
    Loads that integer into GAME_VALUES['num_players']
    Returns None
    '''
    while True:
        display_error_messages()
        message = '\nEnter how many computer players you would like to play with (1-5): '
        user_input = input(message)
        if user_input.isdigit():
            break
        GAME_VALUES['error_messages'].append('Invalid entry please try again')
    # forces min to be 1 and max to be 5
    user_input = int(user_input)
    ai_players = max(user_input, 1)
    ai_players = min(ai_players, 5)
    GAME_VALUES['num_players'] = ai_players
    if user_input > 5 or user_input < 1:
        print("You entered a value outside the acceptable range.")
        print(F"Computer players has been set to {ai_players}")
        enter_to_continue()

def initialize_players():
    '''
    Adds a player's information to the GAME_VALUES['players'] list
    Returns None
    '''
    initialize_user()
    initialize_ai_players()

def initialize_ai_players():
    '''
    Initializes data for AI players
    Returns None
    '''
    for i in range(1, GAME_VALUES['num_players'] + 1):
        ai_info = copy.deepcopy(PLAYER_INFO)
        if i == GAME_VALUES['num_players']:
            ai_info['name'] = 'Dealer'
            ai_info['risk_level'] = 'low'
        else:
            ai_info['name'] = F"AI {i}"
            ai_info['risk_level'] = random.choice(list(AI_RISK_LEVELS))
        ai_info['player_type'] = 'ai'
        ai_info['player_number'] = i + 1
        GAME_VALUES['players'].append(ai_info)

def initialize_user():
    '''
    Initializes data for User player
    Returns None
    '''
    user_info = copy.deepcopy(PLAYER_INFO)
    user_info['name'] = "Player 1"
    user_info['player_type'] = 'human'
    user_info['player_number'] = 1
    GAME_VALUES['players'].append(user_info)

# ==================
# Evaluation Functions
# ==================

def evaluate_results():
    '''
    Evaluates the winners of the round
    Updates GAME_VALUES object
    Returns None
    '''
    evaluate_rankings()
    if has_everyone_busted():
        evaluate_busters()
    else:
        evaluate_winners()

def evaluate_winners():
    '''
    Evaluates who won the round
    Returns None
    '''
    winning_score = sorted(GAME_VALUES['rankings'], reverse = True)[0]
    GAME_VALUES['winning_score'] = winning_score
    if 'Dealer' in GAME_VALUES['rankings'][winning_score]:
        GAME_VALUES['winners'].append(find_player_by_name('Dealer'))
    else:
        for name in GAME_VALUES['rankings'][winning_score]:
            GAME_VALUES['winners'].append(find_player_by_name(name))
        GAME_VALUES['num_winners'] = len(GAME_VALUES['winners'])

def evaluate_busters():
    '''
    If everyone busts, it sets winning score to busted
    Returns None
    '''
    GAME_VALUES['winning_score'] = 'Everyone Busted!'
    GAME_VALUES['winners'].append(make_busted_player())

def evaluate_rankings():
    '''
    Evaluates the rankings of the round
    Updates GAME_VALUE object
    Returns None
    '''
    rankings = {}
    for player in GAME_VALUES['players']:
        score = evaluate_player_score(player)
        player['score'] = score
        if player['has_busted']:
            GAME_VALUES['busted_players'].append(player)
            continue
        rankings.setdefault(score, [])
        rankings[score].append(player['name'])
    GAME_VALUES['rankings'] = rankings

def evaluate_player_score(player):
    '''
    Evaluates the player's score
    Returns score value
    '''
    if not player['has_alt_hand_value']:
        return player['hand_value']
    if player['hand_value'] > player['alt_hand_value'] and \
            player['hand_value'] < BUST_VALUE:
        return player['hand_value']
    return player['alt_hand_value']

# ==================
# Game Utility Functions
# ==================

def deal_cards():
    '''
    Deals initial 2 cards to each player
    Calculates
    Returns None
    '''
    for _ in range(2):
        for player in GAME_VALUES['players']:
            deal_card_from_deck(player)

def deal_card_from_deck(player):
    '''
    Puts a card from the deck into a player's hand
    Updates player's hand information
    Returns None
    '''
    card = take_card_from_deck()
    update_player_hand_info(player, card)

def take_card_from_deck():
    '''
    Pops a card from the deck and returns that card
    '''
    return GAME_VALUES['deck'].pop()

def hit(player):
    '''
    Pops a card from the deck and returns that card
    Returns None
    '''
    deal_card_from_deck(player)

def shuffle_deck():
    '''
    Shuffles the array of deck cards
    Returns None
    '''
    random.shuffle(GAME_VALUES['deck'])

def winning_order():
    '''
    Returns a list of the winning order of players
    '''
    order = []
    if is_dealer_winner():
        order.append(GAME_VALUES['players'].pop())
    score_sorted_players = sorted(GAME_VALUES['players'], key = return_score, reverse = True)
    for player in score_sorted_players:
        order.append(player)
    return order

def return_score(player):
    '''
    Returns the score of the player passed
    '''
    score = player['score']
    if player['has_busted']:
        score *= -1
    return score


def make_busted_player():
    '''
    In the rare case everyone busts, this player becomes the 'winner'
    Returns busted_player dictionary
    '''
    busted_player = copy.deepcopy(PLAYER_INFO)
    busted_player['name'] = 'Nobody'
    busted_player['player_number'] = 0
    busted_player['player_type'] = 'ai'
    busted_player['turn_ended'] = True
    return busted_player

def find_player_by_name(name):
    '''
    Returns player dictionary based on name of player
    '''
    result = [ player for player in GAME_VALUES['players']
              if player['name'] == name ]
    return result[0]

# ==================
# Player Update Functions
# ==================

def update_player_hand_info(player, card):
    '''
    Adds card to player's hand
    Updates hand calculated value
    Returns None
    '''
    player['hand'].append(card)
    player['hand_values'].append(DECK_REFERENCE[card])
    update_alt_hand_values_list(player)
    update_hand_value(player)
    update_alt_hand_value(player)
    update_public_hand_value(player)
    update_alt_public_hand_value(player)
    update_has_alt_hand_value(player)
    update_has_busted(player)
    update_cards_in_hand(player)

def update_has_alt_hand_value(player):
    '''
    If the player has an ace in their hand returns True
    If not it returns False
    '''
    if player['has_alt_hand_value']:
        return
    if player['hand_value'] != player['alt_hand_value']:
        player['has_alt_hand_value'] = True

def update_has_busted(player):
    '''
    If the player an alt hand value > 21 returns True
    If not it returns False
    '''
    if player['alt_hand_value'] > 21:
        player['has_busted'] = True

def update_hand_value(player):
    '''
    Recalculates the sum of values in a player's hand
    Returns None
    '''
    player['hand_value'] = sum(player['hand_values'][:])

def update_alt_hand_value(player):
    '''
    Recalculates the sum of alternate values in a player's hand
    Returns None
    '''
    player['alt_hand_value'] = sum(player['alt_hand_values'][:])

def update_public_hand_value(player):
    '''
    Recalculates the sum of publicly displayed values in a player's hand
    Returns None
    '''
    player['public_hand_value'] = sum(player['hand_values'][1:])

def update_alt_public_hand_value(player):
    '''
    Recalculates the sum of alternate publicly displayed
        values in a player's hand
    Returns None
    '''
    player['alt_public_hand_value'] = sum(player['alt_hand_values'][1:])

def update_cards_in_hand(player):
    '''
    Updates the tally of cards in a player's hand
    '''
    player['cards_in_hand'] += 1

def update_alt_hand_values_list(player):
    '''
    Checks for any values of 11 (Ace value) and replaces it with a value of 1
    Stores values in alternate data structure in player's info dictionary
    Returns None
    '''
    try:
        idx = player['hand_values'].index(11)
    except ValueError:
        player['alt_hand_values'] = player['hand_values']
    else:
        player['alt_hand_values'] = player['hand_values'][:]
        player['alt_hand_values'][idx] = 1

# ==================
# Display Functions
# ==================

def display_results():
    '''
    Displays results of the round
    Rreturns None
    '''
    clear_screen()
    winners_names = [ player['name'] for player in GAME_VALUES['winners'] ]
    print(F"With a score of {GAME_VALUES['winning_score']}")
    if GAME_VALUES['num_winners'] > 1:
        print(F"{' and '.join(winners_names)} won the round!")
    else:
        print(F"{''.join(winners_names)} won the round!")
    display_winning_order(False)

def display_error_messages():
    '''
    Prints error messages
    Clears error messages
    Returns None
    '''
    for message in GAME_VALUES['error_messages']:
        print(message)
    GAME_VALUES['error_messages'].clear()

def display_ai_round_play_hit(player):
    '''
    Displays slow progression of AI play for user experience
    Returns None
    '''
    print(F"{player['name']} is Deciding")
    delay(AI_DELAY)
    print(F"\n{player['name']} decides to Hit!")
    delay(AI_DELAY)
    print(F"\nHe draws a {player['hand'][-1]}")

def display_ai_round_play_stay(player):
    '''
    Displays slow progression of AI play for user experience
    Returns None
    '''
    clear_screen()
    display_player(player, True)
    print(F"{player['name']} is Deciding")
    delay(AI_DELAY)
    print(F"\n{player['name']} will Stay")
    delay(AI_DELAY)

def display_table(round_play = True):
    '''
    Loops through players
    Displays the players hands on the terminal
    Displays actual scores for player 1, and public scores for other players
    Returns None
    '''
    for player in GAME_VALUES['players']:
        display_player(player, round_play)

def display_winning_order(round_play):
    '''
    Loops through players
    Displays the players hands on the terminal
    Displays actual scores for player 1, and public scores for other players
    Returns None
    '''
    for player in winning_order():
        display_player(player, round_play)

def display_player(player, round_play):
    '''
    Displays a players stats on the table
    Returns None
    '''
    print(TOP_BAR)
    new_line()
    print(player['name'], ':')
    print(formatted_card_display_string(player, round_play))
    display_player_hand_value(player, round_play)
    if round_play:
        display_turn_status(player)

def display_turn_status(player):
    '''
    Displays if player's turn has ended
    Return None
    '''
    if player['turn_ended']:
        print(F"{player['name']}'s Turn has Ended\n")

def display_player_hand_value(player, round_play):
    '''
    Prints Hand Value based on Player number and round play
    Returns None
    '''
    if round_play:
        if player['player_number'] == 1:
            display_total_hand_value(player)
            return
        display_public_hand_value(player)
        return
    display_total_score(player)

def display_total_hand_value(player):
    '''
    Prints total hand value
    Returns None
    '''
    print(F"Hand Value: {player['hand_value']}")
    if player['has_alt_hand_value']:
        display_alternate_hand_value(player)
    display_bust_status(player)

def display_total_score(player):
    '''
    Prints total hand value
    Returns None
    '''
    print(F"Score: {player['score']}")
    display_bust_status(player)

def display_alternate_hand_value(player, public = False):
    '''
    Displays alternate hand value
    Returns None
    '''
    if public:
        print(F"Alternate Public Ace Hand Value: {player['alt_public_hand_value']}")
    else:
        print(F"Alternate Ace Hand Value: {player['alt_hand_value']}")

def display_bust_status(player):
    '''
    Displays bust if player busts, or nothing if they didn't bust
    Returns None
    '''
    highlight_bar = '=' * 10
    if player['has_busted']:
        print(highlight_bar, F"{player['name']} BUSTS", highlight_bar)

def display_public_hand_value(player):
    '''
    Prints public hand value (hides first card value)
    Returns None
    '''
    print(F"Public Hand Value: {player['public_hand_value']}")
    if player['has_alt_hand_value'] and not is_first_card_an_ace(player):
        display_alternate_hand_value(player, public = True)

# ==================
# Diplay Formatting Functions
# ==================

def formatted_card_display_string(player, round_play):
    '''
    Returns formatted string for card display
    '''
    formatted_hand = generate_card_line(player, card_line_1()) + \
                     generate_card_line(player, card_line_2()) + \
                     generate_card_title_line(player, round_play) + \
                     generate_card_line(player, card_line_4())
    return formatted_hand

def generate_card_line(player, text):
    '''
    Returns line of hand for display
    '''
    spacer = '  '
    line = ''
    for _ in range(player['cards_in_hand'] - 1):
        line += text
        line += spacer
    line += text
    line += '\n'
    return line

def generate_card_title_line(player, round_play):
    '''
    Returns line of card titles for display
    '''
    spacer = '  '
    line = card_line_3(first_card_display(player, round_play)) + spacer
    for i in range(1, player['cards_in_hand'] - 1):
        line += card_line_3(player['hand'][i])
        line += spacer
    line += card_line_3(player['hand'][-1])
    line += '\n'
    return line

def first_card_display(player, round_play):
    '''
    Returns ???? for first card (face down card) for everyone but player 1
    Returns title of first card for player one (will show face up for player 1)
    '''
    if round_play and player['player_number'] != 1:
        card_title = HIDDEN_CARD
    else:
        card_title = player['hand'][0]
    return card_title

def card_line_1():
    '''
    Returns line 1 of card display
    '''
    return ' ' + ('_' * CARD_HORIZ) + ' '

def card_line_2():
    '''
    Returns line 2 of card display
    '''
    return '|' + (' ' * CARD_HORIZ) + '|'

def card_line_3(card_title):
    '''
    Returns line 3 of card display
    '''
    return '| ' +  card_title.center(MAX_CARD_NAME_LENGTH) + ' |'

def card_line_4():
    '''
    Returns bottom of card border
    '''
    return '|' + ('_' * CARD_HORIZ) + '|'

# ==================
# Predicate Functions
# ==================

def has_everyone_busted():
    '''
    Returns True if all players busted, False otherwise
    '''
    return all(player['has_busted'] for player in GAME_VALUES['players'])

def is_dealer_winner():
    '''
    Returns True if dealer won
    False otherwise
    '''
    return GAME_VALUES['winners'][0]['name'] == 'Dealer'

def is_first_card_an_ace(player):
    '''
    Returns True if first card is an Ace
    Important for not displaying alternate hand value
    '''
    return 'Ace' in player['hand'][0]

# ==================
# General Utility Functions
# ==================

def enter_to_continue():
    '''
    Press enter to continue
    Return None
    '''
    input('\nPress enter to continue: ')

def clear_screen():
    '''
    Clears terminal screen
    Returns None
    '''
    os.system('clear')

def delay(sec):
    '''
    Pauses for sec number of seconds
    Returns None
    '''
    os.system(F"sleep {sec}")

def new_line():
    '''
    Prints a new line to the screen
    Returns None
    '''
    print('')

welcome()
while True:
    run()
    clear_screen()
    while True:
        selection = input('\n\nWould you like to play again? (y/n): ')
        if selection in 'yn' and len(selection) != 0:
            break
        print('Invalid input, please try again.')
    if selection != 'y':
        break
