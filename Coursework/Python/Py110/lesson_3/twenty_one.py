'''
21 BlackJack
'''

import random
import os
import math
import twenty_one_messages

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
HIGH_ACE_VALUE = 11
LOW_ACE_VALUE = 1

# ==================
# GLOBAL_VARIABLES
# ==================
game_values = {}
round_values = {}
messages = twenty_one_messages.collect_messages()

# ==================
# Game Play
# ==================

def init_new_game():
    'Initiates new game values'
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
    'Initializes game attributes per round'
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
    'Resets pertinent player stats for a new round'
    for player in game_values['players']:
        player['hand'] = []
        player['hand_values'] = []
        player['alt_hand_values'] = []
        player['score'] = 0
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
    'Goes through each player and plays their round'
    for player in game_values['players']:
        clear_screen()
        display_table()
        enter_to_continue()
        play_round(player)
    round_values['round_complete'] = True

def play_round(player):
    'Plays the round of the player passed'
    while not player['turn_ended']:
        clear_screen()
        display_banner(F"{player['name']} Round")
        display_player(player)
        display_error_messages()
        if player['type'] == 'human':
            player_selection = input(messages['hit_stay']).casefold()
            if player_selection not in VALID_ROUND_PLAY_SELECTIONS or \
                    len(player_selection) == 0:
                add_error_message('Invalid selection, please try again')
            elif player_selection == 's':
                player['hit_me'] = False
            else:
                hit(player)
        else:
            if is_risk_level_exceeded(player):
                break
            hit(player)
            display_ai_hit(player)
        evaluate_if_turn_ended(player)
    if player['type'] != 'human':
        display_ai_stay(player)

# ==================
# Initialization Functions
# ==================

def determine_number_of_players():
    'Asks for how many players will play'
    display_banner("Number of Players")
    while True:
        display_error_messages()
        message = "\nHow many computer players (AIs) would like to " \
                  F"play with (1-{MAX_AI_PLAYERS})?: "
        user_input = input(message)
        if user_input.isdigit():
            break
        game_values['error_messages'].append('Invalid entry please try again')
    set_num_of_players(int(user_input))

def set_num_of_players(num):
    'Sets the number of AI Players'
    # forces min to be 1 and max to be 5
    user_players = 1
    ai_players = max(num, 1)
    ai_players = min(ai_players, MAX_AI_PLAYERS)
    game_values['ai_players'] = num
    game_values['num_players'] = ai_players + user_players
    if num > (MAX_AI_PLAYERS) or num < 1:
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
    'Evaluates the winners of the round'
    update_player_scores()
    round_values['winning_score'] = winning_score()
    evaluate_winners()
    save_winners_to_game_values()
    round_values['rankings'] = winning_order()
    update_winner_records()

def evaluate_winners():
    'Evaluates who won the round'
    round_values['winners'].extend([
            player for player in game_values['players']
            if player['score'] == round_values['winning_score']
        ])
    if is_dealer_winner():
        round_values['winners'] = [find_player_by_name('Dealer')]

def winning_order():
    'Returns a list of the winning order of players'
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
    '''Returns the score that won the round
    Returns 'All Busted' if everyone busted'''
    score = max( return_score_for_rankings(player)
                 for player in game_values['players'] )
    if score < 0:
        score = 'All Busted'
    return score

def sorted_players_by_score_descending():
    'Returns the list of players sorted by their score from high to low'
    return sorted(game_values['players'],
                  key = return_score_for_rankings,
                  reverse = True)

def return_score_for_rankings(player):
    '''Returns the score of the player passed'''
    score = player['score']
    if has_busted(player):
        score *= -1
    return score

def evaluate_player_score(p):
    '''Evaluates the player's score
    Returns score value'''
    if not has_alt_hand_value(p):
        return hand_value(p)
    if (hand_value(p) > alt_hand_value(p)) and (hand_value(p) < BUST_VALUE):
        return hand_value(p)
    return alt_hand_value(p)

def evaluate_if_turn_ended(player):
    '''Updates a player's turn_ended flag if their turn is over'''
    player['turn_ended'] =  has_busted(player) or \
                            wants_to_end_turn(player)

def save_winners_to_game_values():
    '''Returns data to be used when displaying winners'''
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
    'Deals initial 2 cards to each player'
    for _ in range(2):
        for player in game_values['players']:
            deal_card_from_deck(player)

def deal_card_from_deck(player):
    'Puts a card from the deck into a players hand'
    card = take_card_from_deck()
    update_player_hand_info(player, card)

def take_card_from_deck():
    'Pops a card from the deck and returns that card'
    return round_values['deck'].pop()

def hit(player):
    'Pops a card from the deck and returns that card'
    deal_card_from_deck(player)

def shuffle_deck():
    'Shuffles the array of deck cards'
    random.shuffle(round_values['deck'])

def find_player_by_name(name):
    'Returns player dictionary based on name of player'
    result = [ player for player in game_values['players']
              if player['name'] == name ]
    return result[0]

def ask_to_play_another_round():
    'Asks if user wants to end the game early or keep playing rounds'
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
    'Returns current round number'
    return game_values['rounds_played']

# ==================
# Player Update Functions
# ==================

def update_player_scores():
    'Updates the player data with their round score'
    for player in game_values['players']:
        player['score'] = evaluate_player_score(player)

def update_winner_records():
    'Updates the winners with winning record data'
    for player in round_values['winners']:
        update_player_wins(player)

def update_player_wins(player):
    ''' Part of evaluate_rankings() function
        Updates a player's winning data if they won a round '''
    player['winning_rounds'].append(current_round())
    player['winning_scores'].append(player['score'])
    player['winning_hands'].append(player['hand'])

def update_rounds_played():
    'Updates rounds played in game_values'
    game_values['rounds_played'] += 1

def update_player_hand_info(player, card):
    ''' Adds card to player's hand
        Updates hand calculated value '''
    player['hand'].append(card)
    player['hand_values'].append(DECK_REFERENCE[card])
    update_alt_hand_values(player)

def update_alt_hand_values(player):
    'Updates best alternate hand score given Aces in hand'
    player['alt_hand_values'] = determine_alt_values(player)

# ==================
# Player Query Functions
# ==================

def public_hand(p):
    'Returns only the face up cards in the hand'
    return p['hand'][1:]

def number_of_cards_in_hand(p):
    'Returns number of cards in hand'
    return len(p['hand'])

def hand_value(p):
    'Returns hand value of player'
    return sum(p['hand_values'])

def public_hand_value(p):
    'Returns public hand value of player'
    return sum(p['hand_values'][1:])

def alt_hand_value(p):
    'Returns alt hand value of player'
    return sum(p['alt_hand_values'])

def alt_public_hand_value(p):
    'Returns public hand value of player'
    return sum(p['alt_hand_values'][1:])

def has_alt_hand_value(p):
    'Returns True if player has an alternate hand value due to aces'
    return hand_value(p) != alt_hand_value(p) and bool(aces_in_hand(p))

def has_alt_public_hand_value(p):
    'Returns True if player has an alternate public hand value due to aces'
    return public_hand_value(p) != alt_public_hand_value(p)

def aces_in_hand(p):
    'Updates the number of aces in a players hand'
    ace_count = 0
    for card in p['hand']:
        if 'Ace' in card:
            ace_count += 1
    return ace_count

# ==================
# Player Alt Hand Values Functions
# ==================

def determine_alt_values(player):
    'Returns a list of alternate valid combinations of Ace Vales, or []'
    if number_of_cards_in_hand(player) < 2:
        return []
    alt_combos = alt_hand_values_combinations(player)
    best_combo_idx = determine_best_valid_alt_combo_idx(alt_combos)
    if best_combo_idx:
        return alt_combos[best_combo_idx[0]]
    return []

def alt_hand_values_combinations(player):
    'Returns all hand values given one or more Aces are in the hand'
    temp_hand = player['hand_values'][:]
    alt_combinations = []
    for idx in ace_indexes(player):
        temp_hand = temp_hand[:]
        temp_hand[idx] = 1
        alt_combinations.append(temp_hand)
    return alt_combinations

def determine_best_valid_alt_combo_idx(alt_combos):
    'Returns the index for the best Ace Score given aces can be 1 or 11'
    scores = [ (sum(combo), i) for i, combo in enumerate(alt_combos) ]
    sorted_filtered_scores = sorted([ (score, i) for score, i
                                     in scores if score < BUST_VALUE ])
    if sorted_filtered_scores:
        best_idx = sorted_filtered_scores[-1][1]
        return [best_idx]
    return []

def determine_best_ace_score_and_combo_idx(ace_combinations):
    'Returns highest public score with Aces in hand <= 21'
    scores = [ (sum(combo[1:]), i) for i, combo
               in enumerate(ace_combinations) ]
    return max( (score, i) for i, score in scores if score < BUST_VALUE )[-1]

def ace_indexes(player):
    'Returns list of indexes of aces in hand'
    indexes = []
    for idx, card in enumerate(player['hand']):
        if is_card_ace(card):
            indexes.append(idx)
    return indexes

def is_card_ace(card):
    'Return True if card is an ace'
    return 'Ace' in card

# ==================
# Display Functions
# ==================

def display_round_results():
    'Displays results of the current round'
    clear_screen()
    display_player_amounts_won()
    display_banner(F"Round {current_round()} Results")
    display_round_winner(current_round())
    display_rankings()

def display_game_results():
    'Displays stats of all rounds played'
    display_banner("Total Game Stats")
    print(F"You played {game_values['rounds_played']} rounds.")
    display_player_amounts_won()
    display_round_winners()

def display_round_winners():
    'Displays winners of each round'
    display_banner("Winner Board")
    for rnd in range(1, game_values['rounds_played'] + 1):
        display_round_winner(rnd)

def display_round_winner(rnd):
    'Displays winner of a particular round'
    winners = game_values['round_winners'][rnd]
    if winners:
        for winner in winners:
            print(F"Round {rnd} Winner: {winner['name']}")
            print(F"\tScore - {winner['score']}")
            print(F"\tHand - {winner['hand']}")
    else:
        print("Everyone busted, no winners this round")

def display_player_amounts_won():
    'Displays how many times each player has won'
    display_banner("Total Wins By Player")
    for player in sorted(game_values['players'],
                         key=sort_amounts_won,
                         reverse=True):
        rounds_won = len(player['winning_rounds'])
        print(F"\t{player['name']} won",
              F"{formatted_rounds_played_text(rounds_won)}")

def sort_amounts_won(player):
    'Returns a tuple of (amount won, player number) for sorting by rounds won'
    return (len(player['winning_rounds']), player['number'] * -1)

def display_banner(banner):
    'Displays title for the results display'
    banner = '  ' + banner + '  '
    print(F"{banner.center(BANNER_LENGTH, BANNER_FILL_CHAR)}\n")

def display_header(header):
    'Displays title for the results display'
    header = header + '  '
    print(F"{header.ljust(BANNER_LENGTH, BANNER_FILL_CHAR)}\n")

def add_error_message(msg):
    'Adds message to error messages list'
    game_values['error_messages'].append(msg)

def display_error_messages():
    'Prints then clears error messages'
    for message in game_values['error_messages']:
        print(message)
    game_values['error_messages'].clear()

def display_ai_hit(player):
    'Displays slow progression of AI play for user experience'
    print(F"{player['name']} is Deciding")
    delay(AI_DELAY)
    print(F"\n{player['name']} decides to Hit!")
    delay(AI_DELAY)
    print(F"\nHe draws a {player['hand'][-1]}")

def display_ai_stay(player):
    'Displays slow progression of AI play for user experience'
    clear_screen()
    display_banner(F"{player['name']} Round")
    display_player(player)
    print(F"{player['name']} is Deciding")
    delay(AI_DELAY)
    print(F"\n{player['name']} will Stay")
    delay(AI_DELAY)

def display_table():
    '''Loops through players
    Displays the players hands on the terminal
    Displays actual scores for player 1, and public scores for other players'''
    display_banner(F"Round {current_round()} BlackJack Table")
    for player in game_values['players']:
        display_player(player)

def display_rankings():
    '''Displays the players hands on the terminal
    Displays actual scores for player 1, and public scores for other players'''
    for player in round_values['rankings']:
        display_player(player)

def display_player(player):
    'Displays a players stats on the table'
    new_line()
    display_header(player['name'])
    determine_card_format(player)
    print(formatted_card_display_string(player))
    display_player_hand_value(player)
    if is_player_turn_ended(player) and not is_round_complete():
        display_turn_status(player)

def display_turn_status(player):
    'Displays if players turn has ended'
    if player['turn_ended']:
        print(F"{player['name']}'s Turn has Ended\n")

def display_player_hand_value(player):
    'Prints Hand Value based on Player number and round play'
    if is_round_in_play():
        if player['type'] == 'human':
            display_total_hand_value(player)
            return
        display_public_hand_value(player)
        return
    display_total_score(player)

def display_total_hand_value(p):
    'Prints total hand value'
    print(F"Hand Value: {hand_value(p)}")
    if has_alt_hand_value(p):
        display_alternate_hand_value(p)
    display_bust_status(p)

def display_total_score(player):
    'Prints total hand score'
    print(F"Score: {player['score']}")
    display_bust_status(player)

def display_alternate_hand_value(p, public = False):
    'Displays alternate hand value'
    if public:
        print(F"Alternate Public Ace Hand Value: {alt_public_hand_value(p)}")
    else:
        print(F"Alternate Ace Hand Value: {alt_hand_value(p)}")

def display_bust_status(p):
    'Displays bust if player busts, or nothing if they didnt bust'
    highlight_bar = '=' * 10
    if has_busted(p):
        print(highlight_bar, F"{p['name']} BUSTS", highlight_bar)

def display_public_hand_value(p):
    'Prints public hand value (hides first card value)'
    print(F"Public Hand Value: {public_hand_value(p)}")
    if has_alt_hand_value(p):
        display_alternate_hand_value(p, public = True)

def display_welcome_message():
    'Displays welcome screen'
    clear_screen()
    display_banner('Welcome to 21 Black Jack!')
    for message in messages['welcome']:
        print(message)

def display_exit_message():
    'Displays exit message'
    new_line()
    display_banner('Game Over')
    print('Thanks for playing!')

# ==================
# Diplay Formatting Functions
# ==================

def formatted_rounds_played_text(num):
    'Returns how singular or plural rounds played text'
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

def generate_card_line(p, text):
    'Returns line of hand for display'
    spacer = '  '
    line = ''
    for _ in range(number_of_cards_in_hand(p) - 1):
        line += text
        line += spacer
    line += text
    line += '\n'
    return line

def generate_card_title_line(p):
    'Returns line of card titles for display'

    spacer = '  '
    hand = format_cards_in_hand(p)
    line = card_line_3(first_card_display(p, hand)) + spacer
    for i in range(1, number_of_cards_in_hand(p) - 1):
        line += card_line_3(hand[i])
        line += spacer
    line += card_line_3(hand[-1])
    line += '\n'
    return line

def format_cards_in_hand(p):
    'Shortens card names in hand'
    if number_of_cards_in_hand(p) > MAX_CARDS_ON_SCREEN:
        return [ F"{card_shorthand(card)}" for card in p['hand']]
    return p['hand']

def card_shorthand(card):
    'Shortens name of card'
    value = card.split()[0]
    suite = card.split()[2]
    if value != '10':
        value = value[0]
    return F"{value}o{suite[0]}"

def first_card_display(player, hand):
    'Returns first card for display'
    if is_round_in_play() and player['type'] != 'human':
        card_title = HIDDEN_CARD
    else:
        card_title = hand[0]
    return card_title

def card_line_1():
    'Returns line 1 of card display'
    return ' ' + ('_' * game_values['card_horiz']) + ' '

def card_line_2():
    'Returns line 2 of card display'
    return '|' + (' ' * game_values['card_horiz']) + '|'

def card_line_3(card_title):
    'Returns line 3 of card display'
    return '| ' +  card_title.center(game_values['card_length']) + ' |'

def card_line_4():
    'Returns bottom of card border'
    return '|' + ('_' * game_values['card_horiz']) + '|'

def determine_card_format(p):
    'Adjusts card length for cards in hand to fit on the screen'
    if number_of_cards_in_hand(p) > MAX_CARDS_ON_SCREEN:
        game_values['card_length'] = SHORT_CARD_NAME_LENGTH
        game_values['card_horiz'] = SHORT_CARD_NAME_LENGTH + 2
    else:
        game_values['card_length'] = MAX_CARD_NAME_LENGTH
        game_values['card_horiz'] = MAX_CARD_NAME_LENGTH + 2

# ==================
# Predicate Functions
# ==================


def is_risk_level_exceeded(player):
    '''Returns True if AI or Dealer exceeded their risk level'''
    if player['type'] == 'ai' and \
            hand_value(player) > RISK_LEVELS[player['risk_level']]:
        return True
    return False

def has_busted(p):
    'Returns True if player busted'
    if hand_value(p) >= BUST_VALUE:
        if alt_hand_value(p) and alt_hand_value(p) < BUST_VALUE:
            return False
        return True
    return False

def wants_to_end_turn(player):
    '''Always False for AI/Dealer
    For User True if they decided to stay'''
    if player['type'] == 'human':
        return not player['hit_me']
    return False

def is_round_in_play():
    '''Returns whether a round is currently in play or not'''
    return not round_values['round_complete']

def is_player_turn_ended(player):
    '''Returns whether a round is currently in play or not'''
    return player['turn_ended']

def is_round_complete():
    'Returns status if round is complete'
    return round_values['round_complete']

def has_everyone_busted():
    '''Returns True if all players busted, False otherwise'''
    return all(has_busted(player) for player in game_values['players'])

def is_dealer_winner():
    '''Returns True if dealer won
    False otherwise'''
    if has_everyone_busted():
        return False
    return round_values['winners'][0]['name'] == 'Dealer'

def is_first_card_an_ace(player):
    '''Returns True if first card is an Ace
    Important for not displaying alternate hand value'''
    return 'Ace' in player['hand'][0]

def has_all_rounds_played():
    '''Returns True if all the planned rounds have been played'''
    return game_values['rounds_played'] == ROUNDS_TO_PLAY

# ==================
# General Utility Functions
# ==================

def enter_to_continue():
    '''Press enter to continue'''
    new_line()
    display_banner('-')
    input('\nPress enter to continue: ')

def clear_screen():
    '''Clears terminal screen'''
    os.system('clear')

def delay(sec):
    '''Pauses for sec number of seconds'''
    os.system(F"sleep {sec}")

def new_line():
    '''Prints a new line to the screen'''
    print('')

def print_separator_bar():
    '''Prints separator bar'''
    print(SEPARATOR_BAR)

# ==================
# Play The Game ...
# ==================

display_welcome_message()
play_game()
display_exit_message()
