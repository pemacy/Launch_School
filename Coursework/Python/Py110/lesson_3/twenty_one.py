'''
21 BlackJack
'''

import random
import os
import math
import pdb

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
RISK_LEVELS = {
        'low': LOW_RISK_VALUE,
        'medium': MEDIUM_RISK_VALUE,
        'high': HIGH_RISK_VALUE,
        }

# Display Constants
MAX_CARD_NAME_LENGTH = max(len(title) for title in DECK_REFERENCE)
SHORT_CARD_NAME_LENGTH = 10
BANNER_LENGTH = 80
BANNER_FILL_CHAR = '-'
SEPARATOR_BAR = '=' * BANNER_LENGTH
HIDDEN_CARD = '?????'
AI_DELAY = 1
END_ROUND_DELAY = 1
PLAYER_NAME = "Player 1"
MAX_CARDS_ON_SCREEN = 4

# Gameplay Constants
ROUNDS_TO_PLAY = 5
ROUNDS_NEEDED_TO_WIN = math.ceil(ROUNDS_TO_PLAY / 2)
BUST_VALUE = 22
MAX_AI_PLAYERS = 4
VALID_ROUND_PLAY_SELECTIONS = ['hit', 'stay', 'h', 's']

# ==================
# GLOBAL_VARIABLES
# ==================
game_values = {}
round_values = {}

# ==================
# Game Play
# ==================

def init_new_game():
    '''
    Initiates new game values
    '''
    game_values['num_players'] = 0
    game_values['players'] = []
    game_values['error_messages'] = []
    game_values['rounds_played'] = 0
    game_values['round_winners'] = {}
    game_values['card_length'] = MAX_CARD_NAME_LENGTH
    game_values['card_horiz'] = MAX_CARD_NAME_LENGTH + 2
    determine_number_of_players()
    initialize_players()

def init_new_round():
    '''
    Initializes game attributes per round
    '''
    round_values['deck'] = list(DECK_REFERENCE.keys())
    round_values['busted_players'] = []
    round_values['winners'] = []
    round_values['num_winners'] = 0
    round_values['rankings'] = []
    round_values['winning_score'] = 0
    round_values['round_complete'] = False
    update_rounds_played()
    reset_players()
    shuffle_deck()

def reset_players():
    '''
    Resets pertinent player stats for a new round
    '''
    for player in game_values['players']:
        player['hand'] = []
        player['hand_values'] = []
        player['alt_hand_values'] = []
        player['cards_in_hand'] = 0
        player['hand_value'] = 0
        player['alt_hand_value'] = 0
        player['public_hand_value'] = 0
        player['alt_public_hand_value'] = 0
        player['score'] = 0
        player['has_alt_hand_value'] = False
        player['has_busted'] = False
        player['hit_me'] = True
        player['turn_ended'] = False

def play_game():
    'Game play loop'

    init_new_game()
    while True:
        play_new_table()
        if has_all_rounds_played():
            clear_screen()
            display_game_results()
            break
        selection = ask_to_play_another_round()
        if selection != 'y':
            break

def play_new_table():
    'Runs the game'

    init_new_round()
    deal_cards()
    play_rounds()
    evaluate_results()
    display_round_results()
    enter_to_continue()

# ==================
# Round Play
# ==================

def play_rounds():
    '''
    Goes through each player and plays their round
    '''
    for player in game_values['players']:
        clear_screen()
        display_table()
        enter_to_continue()
        play_round(player)
    round_values['round_complete'] = True

def play_round(player):
    '''
    Plays the round of the player passed
    '''
    while not player['turn_ended']:
        clear_screen()
        display_banner(F"{player['name']} Round")
        display_player(player)
        display_error_messages()
        if player['type'] == 'human':
            player_selection = input('\nWould you like to hit or stay? (h/s): ').casefold()
            if player_selection not in VALID_ROUND_PLAY_SELECTIONS or len(player_selection) == 0:
                game_values['error_messages'].append('Invalid selection, please try again')
            elif player_selection == 's':
                player['hit_me'] = False
            else:
                hit(player)
        else:
            hit(player)
            display_ai_hit(player)
        evaluate_if_turn_ended(player)
    if player['type'] != 'human':
        display_ai_stay(player)

# ==================
# Initialization Functions
# ==================

def determine_number_of_players():
    '''
    Asks for how many players will play
    Loads that integer into game_values['num_players']
    '''
    display_banner("Number of Players")
    while True:
        display_error_messages()
        message = "\nHow many computer players (AIs) would like to " \
                  F"play with (1-{MAX_AI_PLAYERS})?: "
        user_input = input(message)
        if user_input.isdigit():
            break
        game_values['error_messages'].append('Invalid entry please try again')
    # forces min to be 1 and max to be 5
    dealer = 1
    user_input = int(user_input) + dealer
    ai_players = max(user_input, 1)
    ai_players = min(ai_players, MAX_AI_PLAYERS + dealer)
    game_values['num_players'] = ai_players
    if user_input > (MAX_AI_PLAYERS + dealer) or user_input < 1:
        print("You entered a value outside the acceptable range.")
        print(F"Computer players has been set to {ai_players}")
        enter_to_continue()

def initialize_players():
    "Adds a player's information to the game_values['players'] list"

    for i in range(0, game_values['num_players']):
        player = {}
        initialize_general_player_data(player, i)
        if i == 0:
            initialize_user_player_specifics(player)
        elif i == game_values['num_players'] - 1:
            initialize_dealer_player_specifics(player)
        else:
            initialize_ai_player_specifics(player, i)
        game_values['players'].append(player)

def initialize_general_player_data(player, player_num):
    'Initializes general attribues of all players'

    player['winning_rounds'] = []
    player['winning_hands'] = []
    player['winning_scores'] = []
    player['number'] = player_num

def initialize_dealer_player_specifics(player):
    'Initializes the dealer player'

    player['name'] = 'Dealer'
    player['type'] = 'ai'
    player['risk_level'] = 'low'

def initialize_ai_player_specifics(player, player_num):
    'Initializes an AI player'

    player['name'] = F"AI {player_num}"
    player['type'] = 'ai'
    player['risk_level'] = random.choice(list(RISK_LEVELS))

def initialize_user_player_specifics(player):
    'Initializes data for User player'

    player['name'] = PLAYER_NAME
    player['type'] = 'human'
    player['risk_level'] = 'user'

# ==================
# Evaluation Functions
# ==================

def evaluate_results():
    '''
    Evaluates the winners of the round
    Updates player and game object
    '''
    update_player_scores()
    round_values['winning_score'] = winning_score()
    evaluate_winners()
    save_winners_to_game_values()
    round_values['rankings'] = winning_order()
    update_winner_records()

def evaluate_winners():
    '''
    Evaluates who won the round
    Appends winner's record to record_values['winners']
    '''
    round_values['winners'].extend([
            player for player in game_values['players']
            if player['score'] == round_values['winning_score']
        ])
    if is_dealer_winner():
        round_values['winners'] = [find_player_by_name('Dealer')]

def winning_order():
    '''
    Returns a list of the winning order of players
    '''
    order = []
    for player in sorted_players_by_score_descending():
        order.append(player)
    if is_dealer_winner():
        dealer = find_player_by_name('Dealer')
        dealer_idx = order.index(dealer)
        order.pop(dealer_idx)
        order.insert(0, dealer)
    return order

def winning_score():
    '''
    Returns the score that won the round
    Returns 'All Busted' if everyone busted
    '''
    score = max( return_score_for_rankings(player) for player in game_values['players'] )
    if score < 0:
        score = 'All Busted'
    return score

def sorted_players_by_score_descending():
    '''
    Returns the list of players sorted by their score from high to low
    '''
    return sorted(game_values['players'], key = return_score_for_rankings, reverse = True)

def return_score_for_rankings(player):
    '''
    Returns the score of the player passed
    '''
    score = player['score']
    if player['has_busted']:
        score *= -1
    return score

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

def evaluate_if_turn_ended(player):
    '''
    Updates a player's turn_ended flag if their turn is over
    '''
    player['turn_ended'] =  is_risk_level_exceeded(player) or \
                            has_busted(player) or \
                            wants_to_end_turn(player)

def save_winners_to_game_values():
    '''
    Returns data to be used when displaying winners
    '''
    game_values['round_winners'].setdefault(current_round(), [])
    if round_values['winners']:
        for player in round_values['winners']:
            game_values['round_winners'][current_round()].append({
                'name': player['name'],
                'score': player['score'],
                'hand': player['hand']
                })
    else:
        game_values['round_winners'][current_round()].append({
            'name': 'All Players Busted',
            'score': 0,
            'hand': []
            })

# ==================
# Game Utility Functions
# ==================

def deal_cards():
    '''
    Deals initial 2 cards to each player
    Calculates
    '''
    for _ in range(2):
        for player in game_values['players']:
            deal_card_from_deck(player)

def deal_card_from_deck(player):
    '''
    Puts a card from the deck into a player's hand
    Updates player's hand information
    '''
    card = take_card_from_deck()
    update_player_hand_info(player, card)

def take_card_from_deck():
    '''
    Pops a card from the deck and returns that card
    '''
    return round_values['deck'].pop()

def hit(player):
    '''
    Pops a card from the deck and returns that card
    '''
    deal_card_from_deck(player)

def shuffle_deck():
    '''
    Shuffles the array of deck cards
    '''
    random.shuffle(round_values['deck'])

def find_player_by_name(name):
    '''
    Returns player dictionary based on name of player
    '''
    result = [ player for player in game_values['players']
              if player['name'] == name ]
    return result[0]

def ask_to_play_another_round():
    '''
    Asks if user wants to end the game early or keep playing rounds
    '''
    clear_screen()
    display_round_winners()
    display_banner("Play Again?")
    while True:
        selection = input('\nWould you like to play another round? (y/n): ')
        if selection in 'yn' and len(selection) != 0:
            break
        print('Invalid input, please try again.')
    return selection

def current_round():
    '''
    Returns current round number
    '''
    return game_values['rounds_played']

# ==================
# Player Update Functions
# ==================

def update_player_scores():
    '''
    Updates the player data with their round score
    '''
    for player in game_values['players']:
        player['score'] = evaluate_player_score(player)

def update_winner_records():
    '''
    Updates the winners with winning record data
    '''
    for player in round_values['winners']:
        update_player_wins(player)

def update_player_wins(player):
    '''
    Part of evaluate_rankings() function
    Updates a player's winning data if they won a round
    '''
    player['winning_rounds'].append(current_round())
    player['winning_scores'].append(player['score'])
    player['winning_hands'].append(player['hand'])

def update_rounds_played():
    '''
    Updates rounds played in game_values
    '''
    game_values['rounds_played'] += 1

def update_player_hand_info(player, card):
    '''
    Adds card to player's hand
    Updates hand calculated value
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
    '''
    player['hand_value'] = sum(player['hand_values'][:])

def update_alt_hand_value(player):
    '''
    Recalculates the sum of alternate values in a player's hand
    '''
    player['alt_hand_value'] = sum(player['alt_hand_values'][:])

def update_public_hand_value(player):
    '''
    Recalculates the sum of publicly displayed values in a player's hand
    '''
    player['public_hand_value'] = sum(player['hand_values'][1:])

def update_alt_public_hand_value(player):
    '''
    Recalculates the sum of alternate publicly displayed
        values in a player's hand
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

def display_round_results():
    '''
    Displays results of the current round
    Rreturns None
    '''
    clear_screen()
    display_player_amounts_won()
    display_banner(F"Round {current_round()} Results")
    display_round_winner(current_round())
    display_rankings()

def display_game_results():
    '''
    Displays stats of all rounds played
    '''
    display_banner("Total Game Stats")
    print(F"You played {game_values['rounds_played']} rounds.")
    display_player_amounts_won()
    display_round_winners()

def display_round_winners():
    '''
    Displays winners of each round
    '''
    display_banner("Winner Board")
    for rnd in range(1, game_values['rounds_played'] + 1):
        display_round_winner(rnd)

def display_round_winner(rnd):
    '''
    Displays winner of a particular round
    '''
    winners = game_values['round_winners'][rnd]
    if winners:
        for winner in winners:
            print(F"Round {rnd} Winner: {winner['name']}")
            print(F"\tScore - {winner['score']}")
            print(F"\tHand - {winner['hand']}")
    else:
        print("Everyone busted, no winners this round")

def display_player_amounts_won():
    '''
    Displays how many times each player has won
    '''
    display_banner("Total Wins By Player")
    for player in game_values['players']:
        rounds_won = len(player['winning_rounds'])
        print(F"\t{player['name']} won {formatted_rounds_played_text(rounds_won)}")


def display_banner(banner):
    '''
    Displays title for the results display
    '''
    banner = '  ' + banner + '  '
    print(F"{banner.center(BANNER_LENGTH, BANNER_FILL_CHAR)}\n")

def display_header(header):
    '''
    Displays title for the results display
    '''
    header = header + '  '
    print(F"{header.ljust(BANNER_LENGTH, BANNER_FILL_CHAR)}\n")

def display_error_messages():
    '''
    Prints error messages
    Clears error messages
    '''
    for message in game_values['error_messages']:
        print(message)
    game_values['error_messages'].clear()

def display_ai_hit(player):
    '''
    Displays slow progression of AI play for user experience
    '''
    print(F"{player['name']} is Deciding")
    delay(AI_DELAY)
    print(F"\n{player['name']} decides to Hit!")
    delay(AI_DELAY)
    print(F"\nHe draws a {player['hand'][-1]}")

def display_ai_stay(player):
    '''
    Displays slow progression of AI play for user experience
    '''
    clear_screen()
    display_banner(F"{player['name']} Round")
    display_player(player)
    print(F"{player['name']} is Deciding")
    delay(AI_DELAY)
    print(F"\n{player['name']} will Stay")
    delay(AI_DELAY)

def display_table():
    '''
    Loops through players
    Displays the players hands on the terminal
    Displays actual scores for player 1, and public scores for other players
    '''
    display_banner(F"Round {current_round()} BlackJack Table")
    for player in game_values['players']:
        display_player(player)

def display_rankings():
    '''
    Loops through players
    Displays the players hands on the terminal
    Displays actual scores for player 1, and public scores for other players
    '''
    for player in round_values['rankings']:
        display_player(player)

def display_player(player):
    '''
    Displays a players stats on the table
    '''
    new_line()
    display_header(player['name'])
    determine_card_format(player)
    print(formatted_card_display_string(player))
    display_player_hand_value(player)
    if is_round_over() and not round_values['round_complete']:
        display_turn_status(player)

def display_turn_status(player):
    '''
    Displays if player's turn has ended
    Return None
    '''
    if player['turn_ended']:
        print(F"{player['name']}'s Turn has Ended\n")

def display_player_hand_value(player):
    '''
    Prints Hand Value based on Player number and round play
    '''
    if is_round_in_play():
        if player['type'] == 'human':
            display_total_hand_value(player)
            return
        display_public_hand_value(player)
        return
    display_total_score(player)

def display_total_hand_value(player):
    '''
    Prints total hand value
    '''
    print(F"Hand Value: {player['hand_value']}")
    if player['has_alt_hand_value']:
        display_alternate_hand_value(player)
    display_bust_status(player)

def display_total_score(player):
    '''
    Prints total hand value
    '''
    print(F"Score: {player['score']}")
    display_bust_status(player)

def display_alternate_hand_value(player, public = False):
    '''
    Displays alternate hand value
    '''
    if public:
        print(F"Alternate Public Ace Hand Value: {player['alt_public_hand_value']}")
    else:
        print(F"Alternate Ace Hand Value: {player['alt_hand_value']}")

def display_bust_status(player):
    '''
    Displays bust if player busts, or nothing if they didn't bust
    '''
    highlight_bar = '=' * 10
    if player['has_busted']:
        print(highlight_bar, F"{player['name']} BUSTS", highlight_bar)

def display_public_hand_value(player):
    '''
    Prints public hand value (hides first card value)
    '''
    print(F"Public Hand Value: {player['public_hand_value']}")
    if player['has_alt_hand_value'] and not is_first_card_an_ace(player):
        display_alternate_hand_value(player, public = True)

def display_welcome_message():
    '''
    Displays welcome screen
    '''
    clear_screen()
    display_banner('Welcome to 21 Black Jack!')
    print('Game Rules:')
    print("\n\t• All players are dealt 2 cards.")
    print("\t• You can see both your cards, but computer player's first card is hidden.")
    print("\t• Scores are tallied from the values of the cards in your hand.")
    print("\t• You win by getting as close to, or equal to, 21 as you can.")
    print("\t• During your round:")
    print("\t\t• You can add a card to your hand by choosing to Hit.")
    print("\t\t• Or you can end your turn with your current hand by choosing to Stay.")
    print("\t• Going over 21 is a 'bust', resulting in an automatic loss.")
    print("\t• The Dealer wins any tie breakers.")
    print("\nGood Luck!")

def display_exit_message():
    '''
    Displays exit message
    '''
    new_line()
    display_banner('Game Over')
    print('Thanks for playing!')

# ==================
# Diplay Formatting Functions
# ==================

def formatted_rounds_played_text(num):
    '''
    Returns how singular or plural rounds played text
    '''
    if num == 1:
        return '1 round'
    return F"{num} rounds"


def formatted_card_display_string(player):
    'Returns formatted string for card display'
    formatted_hand = generate_card_line(player, card_line_1()) + \
                     generate_card_line(player, card_line_2()) + \
                     generate_card_title_line(player) + \
                     generate_card_line(player, card_line_4())
    return formatted_hand

def generate_card_line(player, text):
    'Returns line of hand for display'
    spacer = '  '
    line = ''
    for _ in range(player['cards_in_hand'] - 1):
        line += text
        line += spacer
    line += text
    line += '\n'
    return line

def generate_card_title_line(player):
    'Returns line of card titles for display'

    spacer = '  '
    hand = format_cards_in_hand(player)
    line = card_line_3(first_card_display(player, hand)) + spacer
    for i in range(1, player['cards_in_hand'] - 1):
        line += card_line_3(hand[i])
        line += spacer
    line += card_line_3(hand[-1])
    line += '\n'
    return line

def format_cards_in_hand(player):
    'Shortens card names in hand'
    if player['cards_in_hand'] > MAX_CARDS_ON_SCREEN:
        return [ F"{card_shorthand(card)}" for card in player['hand']]
    return player['hand']

def card_shorthand(card):
    'Shortens name of card'
    value = card.split()[0]
    suite = card.split()[2]
    if value != '10':
        value = value[0]
    return F"{value}o{suite[0]}"

def first_card_display(player, hand):
    '''
    Returns ???? for first card (face down card) for everyone but player 1
    Returns title of first card for player one (will show face up for player 1)
    '''
    if is_round_in_play() and player['type'] != 'human':
        card_title = HIDDEN_CARD
    else:
        card_title = hand[0]
    return card_title

def card_line_1():
    'Returns line 1 of card display'
    return ' ' + ('_' * game_values['card_horiz']) + ' '

def card_line_2():
    '''
    Returns line 2 of card display
    '''
    return '|' + (' ' * game_values['card_horiz']) + '|'

def card_line_3(card_title):
    '''
    Returns line 3 of card display
    '''
    return '| ' +  card_title.center(game_values['card_length']) + ' |'

def card_line_4():
    '''
    Returns bottom of card border
    '''
    return '|' + ('_' * game_values['card_horiz']) + '|'

def determine_card_format(player):
    'Adjusts card length for cards in hand to fit on the screen'
    if player['cards_in_hand'] > MAX_CARDS_ON_SCREEN:
        game_values['card_length'] = SHORT_CARD_NAME_LENGTH
        game_values['card_horiz'] = SHORT_CARD_NAME_LENGTH + 2
    else:
        game_values['card_length'] = MAX_CARD_NAME_LENGTH
        game_values['card_horiz'] = MAX_CARD_NAME_LENGTH + 2

# ==================
# Predicate Functions
# ==================


def is_risk_level_exceeded(player):
    '''
    Returns True if AI or Dealer exceeded their risk level
    '''
    if player['type'] == 'ai' and player['hand_value'] > RISK_LEVELS[player['risk_level']]:
        return True
    return False

def has_busted(player):
    '''
    Returns True or False if the player has busted
    '''
    return player['has_busted']

def wants_to_end_turn(player):
    '''
    Always False for AI/Dealer
    For User True if they decided to stay
    '''
    if player['type'] == 'human':
        return not player['hit_me']
    return False

def is_round_in_play():
    '''
    Returns whether a round is currently in play or not
    '''
    return not round_values['round_complete']

def is_round_over():
    '''
    Returns whether a round is currently in play or not
    '''
    return round_values['round_complete']

def has_everyone_busted():
    '''
    Returns True if all players busted, False otherwise
    '''
    return all(player['has_busted'] for player in game_values['players'])

def is_dealer_winner():
    '''
    Returns True if dealer won
    False otherwise
    '''
    if has_everyone_busted():
        return False
    return round_values['winners'][0]['name'] == 'Dealer'

def is_first_card_an_ace(player):
    '''
    Returns True if first card is an Ace
    Important for not displaying alternate hand value
    '''
    return 'Ace' in player['hand'][0]

def has_all_rounds_played():
    '''
    Returns True if all the planned rounds have been played
    '''
    return game_values['rounds_played'] == ROUNDS_TO_PLAY

# ==================
# General Utility Functions
# ==================

def enter_to_continue():
    '''
    Press enter to continue
    Return None
    '''
    new_line()
    display_banner('-')
    input('\nPress enter to continue: ')

def clear_screen():
    '''
    Clears terminal screen
    '''
    os.system('clear')

def delay(sec):
    '''
    Pauses for sec number of seconds
    '''
    os.system(F"sleep {sec}")

def new_line():
    '''
    Prints a new line to the screen
    '''
    print('')

def print_separator_bar():
    '''
    Prints separator bar
    '''
    print(SEPARATOR_BAR)

# ==================
# Play The Game ...
# ==================

display_welcome_message()
play_game()
display_exit_message()
