'''
Create an object-oriented number guessing class for numbers in the range 1 to 100, with a limit of 7 guesses per game. The game should play like this:
'''

import random

class GuessingGame:
    def __init__(self):
        self._number_guesses = 7
        self._number_to_guess = random.randrange(1,100)
        self.guesses = []

    def play(self):
        while self._number_guesses > 0:
            print(f"You have {self._number_guesses} remaining.")
            self.make_guess()
            if self.current_guess == self._number_to_guess:
                print("That's the number!\n\nYou won!")
                return
            elif self.current_guess < self._number_to_guess:
                print("Your guess is too low")
            else:
                print("Your guess is too high")

            self._number_guesses -= 1

        print("You have no more guesses, you lost!")

    def make_guess(self):
        self.current_guess = int(input('Enter a number between 1 and 100: '))

game = GuessingGame()
game.play()
