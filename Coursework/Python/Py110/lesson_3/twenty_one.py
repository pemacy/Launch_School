'''
21 BlackJack
'''

import random
import os
import math

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
BANNER_LENGTH = 80
SEPARATOR_BAR = '=' * BANNER_LENGTH
HIDDEN_CARD = '?????'
AI_DELAY = 0
END_ROUND_DELAY = 0

# Gameplay Constants
ROUNDS_TO_PLAY = 5
ROUNDS_NEEDED_TO_WIN = math.ceil(ROUNDS_TO_PLAY / 2)
BUST_VALUE = 22
MAX_AI_PLAYERS = 4

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
    Returns None
    '''
    game_values['num_players'] = None
    game_values['players'] = []
    game_values['error_messages'] = []
    game_values['rounds_played'] = 0
    game_values['round_winners'] = {}
    game_values['winner_tracker'] = {}
    determine_number_of_players()
    initialize_players()

def init_new_round():
    '''
    Initializes game attributes per round
    Returns None
    '''
    round_values['deck'] = list(DECK_REFERENCE.keys())
    round_values['busted_players'] = []
    round_values['winners'] = []
    round_values['num_winners'] = 0
    round_values['rankings'] = None
    round_values['winning_score'] = 0
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
        player['turn_ended'] = False

def play_game():
    '''
    Game play loop
    '''
    init_new_game()
    while True:
        play_round()
        if has_all_rounds_played():
            break
        selection = ask_to_play_another_round()
        if selection != 'y':
            break

def play_round():
    '''
    Runs the game
    Returns None
    '''
    init_new_round()
    deal_cards()
    play_rounds()
    evaluate_results()
    capture_round_stats()
    display_round_results()
    enter_to_continue()

def welcome():
    '''
    Displays welcome screen
    Returns None
    '''
    clear_screen()
    display_banner('Welcome to 21 Black Jack!')
    print_separator_bar()
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

# ==================
# Round Play
# ==================

def play_rounds():
    '''
    Goes through each player and plays their round
    Returns None
    '''
    for player in game_values['players']:
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
        display_banner(F"{player['name']} Round")
        display_player(player, True)
        display_error_messages()
        player_selection = input('\nWould you like to hit or stay? (h/s): ').casefold()
        if player_selection not in 'hs' or len(player_selection) == 0:
            game_values['error_messages'].append('Invalid selection, please try again')
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
        display_banner(F"{player['name']} Round")
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
    Loads that integer into game_values['num_players']
    Returns None
    '''
    print_separator_bar()
    while True:
        display_error_messages()
        message = "\nHow many computer players (AIs) would like to " \
                  F"play with (1-{MAX_AI_PLAYERS})?: "
        user_input = input(message)
        if user_input.isdigit():
            break
        game_values['error_messages'].append('Invalid entry please try again')
    # forces min to be 1 and max to be 5
    user_input = int(user_input)
    ai_players = max(user_input, 1)
    ai_players = min(ai_players, MAX_AI_PLAYERS)
    game_values['num_players'] = ai_players
    if user_input > MAX_AI_PLAYERS or user_input < 1:
        print("You entered a value outside the acceptable range.")
        print(F"Computer players has been set to {ai_players}")
        enter_to_continue()

def initialize_players():
    '''
    Adds a player's information to the game_values['players'] list
    Returns None
    '''
    initialize_user()
    initialize_ai_players()

def initialize_ai_players():
    '''
    Initializes data for AI players
    Returns None
    '''
    for i in range(1, game_values['num_players'] + 1):
        player = {}
        if i == game_values['num_players']:
            initialize_dealer_player_specifics(player)
        else:
            initialize_ai_player_specifics(player, i)
        initialize_ai_player_general(player, i)

def initialize_ai_player_general(player, player_num):
    '''
    Initializes general attribues of an AI player
    Returns none
    '''
    player['player_type'] = 'ai'
    player['player_number'] = player_num + 1
    game_values['players'].append(player)

def initialize_dealer_player_specifics(player):
    '''
    Initializes the dealer player
    Returns none
    '''
    player['name'] = 'Dealer'
    player['risk_level'] = 'low'

def initialize_ai_player_specifics(player, player_num):
    '''
    Initializes an AI player
    Returns none
    '''
    player['name'] = F"AI {player_num}"
    player['risk_level'] = random.choice(list(AI_RISK_LEVELS))

def initialize_user():
    '''
    Initializes data for User player
    Returns None
    '''
    user_info = {}
    user_info['name'] = "Player 1"
    user_info['player_type'] = 'human'
    user_info['player_number'] = 1
    user_info['risk_level'] = 'user'
    game_values['players'].append(user_info)

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
    winning_score = sorted(round_values['rankings'], reverse = True)[0]
    round_values['winning_score'] = winning_score
    if 'Dealer' in round_values['rankings'][winning_score]:
        round_values['winners'].append(find_player_by_name('Dealer'))
    else:
        for name in round_values['rankings'][winning_score]:
            round_values['winners'].append(find_player_by_name(name))
        round_values['num_winners'] = len(round_values['winners'])

def evaluate_busters():
    '''
    If everyone busts, it sets winning score to busted
    Returns None
    '''
    round_values['winning_score'] = 'Everyone Busted!'
    round_values['winners'].append(make_busted_player())

def evaluate_rankings():
    '''
    Evaluates the rankings of the round
    Updates GAME_VALUE object
    Returns None
    '''
    rankings = {}
    for player in game_values['players']:
        score = evaluate_player_score(player)
        player['score'] = score
        if player['has_busted']:
            round_values['busted_players'].append(player)
            continue
        rankings.setdefault(score, [])
        rankings[score].append(player['name'])
    round_values['rankings'] = rankings

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
        for player in game_values['players']:
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
    return round_values['deck'].pop()

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
    random.shuffle(round_values['deck'])

def winning_order():
    '''
    Returns a list of the winning order of players
    '''
    order = []
    if is_dealer_winner():
        order.append(game_values['players'].pop())
    for player in sorted_players_by_score_descending():
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

def sorted_players_by_score_descending():
    '''
    Returns the list of players sorted by their score from high to low
    '''
    return sorted(game_values['players'], key = return_score, reverse = True)

def make_busted_player():
    '''
    In the rare case everyone busts, this player becomes the 'winner'
    Returns busted_player dictionary
    '''
    busted_player = {}
    busted_player['name'] = 'Nobody'
    busted_player['player_number'] = 0
    busted_player['player_type'] = 'ai'
    busted_player['turn_ended'] = True
    return busted_player

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
    display_banner("Play Again?")
    print_separator_bar()
    while True:
        print(F"\nYou have played {formatted_rounds_played_text(current_round())}")
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

def capture_round_stats():
    '''
    Saves round_values in game_values['round_results']
    Returns None
    '''
    capture_round_winners()
    update_winner_tracker()

def update_rounds_played():
    '''
    Updates rounds played in game_values
    '''
    game_values['rounds_played'] += 1

def capture_round_winners():
    '''
    Adds round winners to game_value['round_winners'][round] list
    '''
    game_values['round_winners'][current_round()] = []
    winner_list = game_values['round_winners'][current_round()]
    for winner in round_values['winners']:
        winner_stat = {}
        winner_stat['name'] = winner['name']
        winner_stat['risk_level'] = winner['risk_level']
        winner_stat['cards_in_hand'] = winner['cards_in_hand']
        winner_stat['hand'] = winner['hand']
        winner_stat['score'] = winner['score']
        winner_list.append(winner_stat)

def update_winner_tracker():
    '''
    Updates the tracker of how many rounds each player has won
    '''
    winner_tracker = game_values['winner_tracker']
    for winner in round_values['winners']:
        winner_tracker.setdefault(winner['name'], 0)
        winner_tracker[winner['name']] += 1

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

def display_game_results():
    '''
    Displays stats of all rounds played
    '''
    clear_screen()
    print_separator_bar()
    display_banner("Total Game Stats")
    print(F"You played {game_values['rounds_played']} rounds.")
    print("Winners:")
    for name, rounds_won in game_values['winner_tracker'].items():
        print(F"\t{name}: won {formatted_rounds_played_text(rounds_won)}")
    for rnd, winners in game_values['round_winners'].items():
        print_separator_bar()
        display_banner(F"Round {rnd} Stats")
        for winner in winners:
            print(F"Winner: {winner['name']}")
            print(F"Score: {winner['score']}")
            print(F"Risk Level: {winner['risk_level']}")
            print(F"Hand: {winner['hand']}")
            # print(formatted_card_display_string(winner, False))

def display_round_results():
    '''
    Displays results of the round
    Rreturns None
    '''
    clear_screen()
    display_banner(F"Round {current_round()} BlackJack Table Results")
    winners_names = [ player['name'] for player in round_values['winners'] ]
    print(F"With a score of {round_values['winning_score']}")
    if round_values['num_winners'] > 1:
        print(F"{' and '.join(winners_names)} won the round!")
    else:
        print(F"{''.join(winners_names)} won the round!")
    display_winning_order(False)

def display_banner(title):
    '''
    Displays title for the results display
    '''
    print(F"{title.center(BANNER_LENGTH)}\n")

def display_error_messages():
    '''
    Prints error messages
    Clears error messages
    Returns None
    '''
    for message in game_values['error_messages']:
        print(message)
    game_values['error_messages'].clear()

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
    display_banner(F"{player['name']} Round")
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
    display_banner(F"Round {current_round()} BlackJack Table")
    for player in game_values['players']:
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
    print_separator_bar()
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

def formatted_rounds_played_text(num):
    '''
    Returns how singular or plural rounds played text
    '''
    if num == 1:
        return '1 round'
    return F"{num} rounds"


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
    return all(player['has_busted'] for player in game_values['players'])

def is_dealer_winner():
    '''
    Returns True if dealer won
    False otherwise
    '''
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
    print_separator_bar()
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

def print_separator_bar():
    '''
    Prints separator bar
    '''
    print(SEPARATOR_BAR)

# ==================
# Play The Game ...
# ==================

welcome()
play_game()
display_game_results()
