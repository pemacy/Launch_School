# pylint: disable=use-a-generator
from src.utility_methods import UtilityMethods
from src.messages import Messages
from src.player import Human
from src.player import Dealer
from src.deck import Deck

class TwentyOne(UtilityMethods, Messages):
    def __init__(self):
        self.deck = Deck()
        self.players = [Human(), Dealer()]
        self.game_play = True
        self.rounds_played = 1
        self.round_winners = {}

    # =============================
    # Game Play Methods
    # =============================
    def play(self):
        self.clear_screen()
        self.display_welcome_message()
        self.display_rules_message()
        self.enter_to_continue()
        while self.game_play:
            self.play_rounds()
            if self.game_play:
                self.ask_play_again()
        self.display_game_results()
        self.display_goodbye_message()

    def play_rounds(self):
        while self.human_player().is_playable():
            self.clear_screen()
            self.display_round_banner()
            self.initial_deal()
            self.display_hands()
            self.enter_to_continue()
            self.play_round()
            self.determine_round_winner()
            self.settle_bets()
            self.display_round_results()
            self.ask_keep_playing()
            if self.game_play:
                self.reset_game()
                self.rounds_played += 1
            else:
                break

    def initial_deal(self):
        for _ in range(2):
            for player in self.players:
                player.hit(self.deck)

    def play_round(self):
        for player in self.players:
            if self.human_player().has_busted():
                self.dealer_player().turn_complete = True
                break
            self.clear_screen()
            player.play_round(self.deck, self)
            print(F"{player.name} round complete")
            self.enter_to_continue()

    def reset_game(self):
        self.deck.reset()
        for player in self.players:
            player.reset()

    # =============================
    # Reference Methods
    # =============================

    def human_player(self):
        return self.players[0]

    def dealer_player(self):
        return self.players[1]

    # =============================
    # End of Round Methods
    # =============================
    def determine_round_winner(self):
        if self.has_all_busted():
            self.round_winners[self.rounds_played] = ['none']
        self.round_winners[self.rounds_played] = self.players_with_max_scores()

    def settle_bets(self):
        if self.human_player() in self.round_winners[self.rounds_played]:
            self.human_player().money += 1
        else:
            self.human_player().money -= 1

    def max_score(self):
        return max([player.score for player in self.players
                    if not player.has_busted()])

    def players_with_max_scores(self):
        return [ player for player in self.players
                 if player.score == self.max_score() ]

    def has_all_busted(self):
        return all([ player.has_busted for player in self.players ])

    # =============================
    # User Input Methods
    # =============================
    def ask_play_again(self):
        self.get_play_status('play again')

    def ask_keep_playing(self):
        self.get_play_status('keep playing')

    def get_play_status(self, msg):
        while True:
            play = input(F'\nWould you like to {msg}? (y/n): ').casefold()
            if play in ('y', 'yes'):
                return
            if play in ('n', 'no'):
                self.game_play = False
                return
            print('Incorrect response, please try again')

    # =============================
    # Display Methods
    # =============================
    def display_welcome_message(self):
        print('Welcome to 21 BlackJack')

    def display_goodbye_message(self):
        print('Thank you for playing, goodbye!')

    def display_rules_message(self):
        print(self.rules())

    def display_game_results(self):
        self.new_line()
        self.display_game_results_banner()
        for rnd, winners in self.round_winners.items():
            print(F"{self.winners_string(winners)} won round {rnd}")
        self.new_line()
        self.human_player().display_gains_losses()

    def winners_string(self, winner_lst):
        player_names = [ player.name for player in winner_lst ]
        return ' and '.join(player_names)

    def display_round_results(self):
        self.clear_screen()
        self.display_round_banner()
        self.display_hands()
        print(self.winners_string(self.round_winners[self.rounds_played]),
              'won the round!')

    def display_round_banner(self):
        title = 'Round ' + str(self.rounds_played)
        print(title.center(UtilityMethods.BANNER_LENGTH))
        self.print_separator_bar()

    def display_game_results_banner(self):
        title = 'Game Results'
        print(title.center(UtilityMethods.BANNER_LENGTH))
        self.print_separator_bar()

    def display_hands(self):
        for player in self.players:
            print(player,'\n')

# t = TwentyOne()
# t.play()
