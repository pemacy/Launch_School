'''
In the previous exercise, you wrote a number guessing game that determines a secret number between 1 and 100, and gives the user 7 opportunities to guess the number.

Update your solution to accept a low and high value when you create a GuessingGame object, and use those values to compute a secret number for the game. You should also change the number of guesses allowed so the user can always win if she uses a good strategy. You can compute the number of guesses with:
'''

import math
import random

class GuessingGame:
    def __init__(self, start, stop):
        self._start_num = start
        self._stop_num = stop
        self._number_guesses = self.generate_number_of_guesses()
        self._number_to_guess = random.randrange(start,stop)
        self.guesses = []

    def play(self):
        while self._number_guesses > 0:
            print(f"You have {self._number_guesses} guesses remaining.")
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
        self.current_guess = int(input(f"Enter a number between {self._start_num} and {self._stop_num}: "))

    def generate_number_of_guesses(self):
        return int(math.log2(self._stop_num - self._start_num + 1)) + 1

game = GuessingGame(501, 1500)
game.play()
