'''
rock paper scissors
'''

import os
import random

class RPS:
    # Intro message
    # List options and get user input
    # Get random computer selection
    # Determine Win Lose or Tie
    # Display Result and Ask to Play Again

    RPS_OPTIONS = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    NUM_SELECTIONS = len(RPS_OPTIONS) + 1
    WINNING_CONDITIONS = [  ['Rock', 'Scissors'],
                            ['Rock', 'Lizard'],
                            ['Paper', 'Rock'],
                            ['Paper', 'Spock'],
                            ['Scissors', 'Paper'],
                            ['Scissors', 'Lizard'],
                            ['Lizard', 'Spock'],
                            ['Lizard', 'Paper'],
                            ['Spock', 'Scissors'],
                            ['Spock', 'Rock']
                         ]

    def __init__(self):
        self.user_selection = self.computer_selection = self.winner = None
        self.results = {}
        self.game_counter = 1

    def clear_screen(self):
        os.system('clear')

    def computer_input(self):
        return random.choice(self.RPS_OPTIONS)

    def display_welcome_message(self):
        print("Welcome to Rock Paper Scissors App!")

    def selection_choices(self):
        return ("Select Option: \n"
                "1 - Rock\n"
                "2 - Paper\n"
                "3 - Scissors\n"
                "4 - Lizard\n"
                "5 - Spock\n\n>> ")

    def user_input(self):
        while True:
            selection = input(self.selection_choices())
            if self.valid_selection(selection):
                selection = int(selection) - 1
                return self.RPS_OPTIONS[selection]
            print("Invalid Entry. Please try again.\n")

    def valid_selection(self, selection):
        if selection in [str(el) for el in range(1,self.NUM_SELECTIONS)]:
            return True
        return False

    @property
    def result_message(self):
        result = (f"\tYou had {self.user_selection}\n"
                  f"\tComputer had {self.computer_selection}")
        match self.winner:
            case 'User':
                return 'You Won!\n' + result
            case 'Computer':
                return 'Computer Won :(\n' + result
            case _:
                return "It's a Tie :/\n" + result

    def display_result(self):
        print(self.result_message)

    def determine_winner(self):
        if self.user_selection == self.computer_selection:
            self.winner = 'Tie'
        elif ([self.user_selection, self.computer_selection] in
                self.WINNING_CONDITIONS):
            self.winner = 'User'
        else:
            self.winner = 'Computer'

    def store_game(self):
        self.results['Game: ' + str(self.game_counter)] = {
                'Winner': self.winner,
                'User Selection': self.user_selection,
                'Computer Selection': self.computer_selection,
                'Result Message': self.result_message
                }

    def user_wants_to_play_again(self):
        play_again = input("Would you like to play again? ")
        return play_again.lower().startswith('y')

    def __str__(self):
        self.clear_screen()
        s = 'Game Summary:\n\n'
        for game, stats in self.results.items():
            s += f"{game}:\n"
            for stat, desc in stats.items():
                s += f"{stat}: {desc}\n"
            s += "\n\n"
        return s

    def run(self):
        while True:
            self.clear_screen()
            self.display_welcome_message()
            self.user_selection = self.user_input()
            self.computer_selection = self.computer_input()
            self.determine_winner()
            self.store_game()
            self.display_result()
            if not self.user_wants_to_play_again():
                break
            self.game_counter += 1
        print(self)

rps = RPS()
rps.run()
