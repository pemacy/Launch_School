'''
21 BlackJack
'''

import random
import os
import copy

# ==================
# Constants
# ==================

LOW_CARD_NAMES = [ '2', '3', '4', '5', '6', '7', '8', '9', '10' ]
FACE_CARD_NAMES = [ 'Jack', 'Queen', 'King', 'Ace' ]
CARD_NAMES = LOW_CARD_NAMES + FACE_CARD_NAMES
LOW_CARD_VALUES = list(range(2,11))
FACE_CARD_VALUES = [ 10, 10, 10, 11 ]
CARD_VALUES = LOW_CARD_VALUES + FACE_CARD_VALUES
CARD_VALUE_TABLE = dict(zip(CARD_NAMES, CARD_VALUES))
LOW_RISK_VALUE = 15
MEDIUM_RISK_VALUE = 17
HIGH_RISK_VALUE = 20
BUST_VALUE = 22
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
AI_DELAY = 2
END_ROUND_DELAY = 3
AI_RISK_LEVELS = {
        'low': LOW_RISK_VALUE,
        'medium': MEDIUM_RISK_VALUE,
        'high': HIGH_RISK_VALUE
        }

SUITE_NAMES = [ 'Spades', 'Clubs', 'Hearts', 'Diamonds' ]

def deck_reference():
    '''
    Returns dictionary of dictionaries of cards
    '''
    d = {}
    for suite in SUITE_NAMES:
        for name, value in CARD_VALUE_TABLE.items():
            title = F"{name} of {suite}"
            d[title] = value
    return d

DECK_REFERENCE = deck_reference()
MAX_CARD_NAME_LENGTH = max([ len(title) for title in DECK_REFERENCE ])
CARD_HORIZ = MAX_CARD_NAME_LENGTH + 2
GAME_VALUES = {}

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
    evaluate_winners()
    display_results()

def welcome():
    '''
    Displays welcome screen
    Determines number of players
    Returns None
    '''
    clear_screen()
    print('Welcome to 21 Black Jack!')

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
            input('\n\nPress Return to play your round: ')
            play_user_round(player)
        else:
            play_ai_round(player)
        player['turn_ended'] = True
        clear_screen()
        display_table()
        # display_player(player, True)
        print(F"\n\n{player['name']}'s round has ended")
        input('Press enter to continue: ')

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
        if player_selection not in 'hs':
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
# Evaluation Functions
# ==================

def evaluate_winners():
    '''
    Evaluates the winners of the round
    Updates GAME_VALUES object
    Returns None
    '''
    evaluate_rankings()
    winning_score = sorted(GAME_VALUES['rankings'], reverse = True)[0]
    GAME_VALUES['winning_score'] = winning_score
    if 'Dealer' in GAME_VALUES['rankings'][winning_score]:
        GAME_VALUES['winners'].append(find_player_by_name('Dealer'))
    else:
        for name in GAME_VALUES['rankings'][winning_score]:
            GAME_VALUES['winners'].append(find_player_by_name(name))
        GAME_VALUES['num_winners'] = len(GAME_VALUES['winners'])

def find_player_by_name(name):
    '''
    Returns player dictionary based on name of player
    '''
    result = [ player for player in GAME_VALUES['players']
              if player['name'] == name ]
    return result[0]

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
    print('\nHe decides to Hit!')
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

def is_dealer_winner():
    '''
    Returns True if dealer won
    False otherwise
    '''
    return GAME_VALUES['winners'][0]['name'] == 'Dealer'

def return_score(player):
    '''
    Returns the score of the player passed
    '''
    score = player['score']
    if player['has_busted']:
        score *= -1
    return score

def display_player(player, round_play):
    '''
    Displays a players stats on the table
    Returns None
    '''
    top_bar = '=' * 80
    print(top_bar)
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
    highlight_bar = '=' * 10
    print(F"Hand Value: {player['hand_value']}")
    if player['has_alt_hand_value']:
        print(F"Alternate Ace Hand Value: {player['alt_hand_value']}")
    if player['has_busted']:
        print(highlight_bar, 'Player BUSTS', highlight_bar)

def display_total_score(player):
    '''
    Prints total hand value
    Returns None
    '''
    highlight_bar = '=' * 10
    print(F"Score: {player['score']}")
    if player['has_busted']:
        print(highlight_bar, 'Player BUSTS', highlight_bar)

def display_public_hand_value(player):
    '''
    Prints public hand value (hides first card value)
    Returns None
    '''
    print(F"Public Hand Value: {player['public_hand_value']}")
    if player['has_alt_hand_value']:
        print(F"Alternate Ace Hand Vaue: {player['alt_public_hand_value']}")

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
        card_title = '????'
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
        message = '\nEnter how many players there will be: '
        selection = input(message)
        if selection.isdigit():
            break
        GAME_VALUES['error_messages'].append('Invalid entry please try again')
    GAME_VALUES['num_players'] = int(selection)

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

def shuffle_deck():
    '''
    Shuffles the array of deck cards
    Returns None
    '''
    random.shuffle(GAME_VALUES['deck'])

# ==================
# Utility Functions
# ==================

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

welcome()
while True:
    run()
    selection = input('\n\nWould you like to play again? (y/n): ')
    if selection != 'y':
        break
