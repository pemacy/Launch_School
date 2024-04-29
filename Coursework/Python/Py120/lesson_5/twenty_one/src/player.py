# pylint: disable=import-error
import random
from src.utility_methods import UtilityMethods
from src.hand import Hand
from src.constants import BlackjackConstants

class Player(UtilityMethods):
    def __init__(self, name='Player', risk_level='low'):
        self._hand = Hand()
        self.name = name
        self.turn_complete = False
        self.money = 5
        self.risk_value = BlackjackConstants.RISK_LEVELS[risk_level]

    # ==========================
    # GamePlay Methods
    # ==========================
    def reset(self):
        self.hand.clear()
        self.turn_complete = False

    def play_round(self, deck, gameplay):
        while True:
            gameplay.display_hands()
            self.assess_hand()
            print(F"{self.name} Turn:")
            if self.turn_complete:
                print(F"{self.name} decided to stand")
                break
            self.hit(deck)
            print(F"{self.name} decides to hit!")
            self.delay(1)
            self.clear_screen()

    def assess_hand(self):
        if self.has_busted() or self.is_hand_above_risk_level():
            self.end_turn()

    def hit(self, deck):
        self.hand.add_card(deck.draw())

    def end_turn(self):
        self.turn_complete = True

    # ==========================
    # Properties
    # ==========================
    @property
    def hand(self):
        return self._hand

    @property
    def score(self):
        return self.hand.value

    # ==========================
    # Magic Methods
    # ==========================
    def __str__(self):
        if self.is_human():
            s = self.human_str()
        else:
            s = self.computer_str()
        if self.has_busted() and not self.should_hide_first_card():
            return '\n'.join([s, F"{self.name} has busted"])
        return s

    # ==========================
    # __str__ Helper Methods
    # ==========================
    def human_str(self):
        money = 'Money: $' + str(self.money)
        return '\n'.join([ self.name,
                            money,
                            str(self.hand),
                            F"Score: {str(self.hand.value) }"])

    def computer_str(self):
        hand, value = self.computer_str_values()
        return '\n'.join([ self.name,
                            str(hand),
                            F"Score: {str(value)}" ])

    def computer_str_values(self):
        if not self.turn_complete:
            return(self.hand.hidden(), self.hand.hidden_value())
        return(self.hand, self.hand.value)

    # ==========================
    # Predicate Methods
    # ==========================
    def should_hide_first_card(self):
        return not self.turn_complete and not self.is_human()

    def is_human(self):
        return self.__class__ == Human

    def has_busted(self):
        return self.hand.is_bust()

    def is_hand_above_risk_level(self):
        return self.hand.value > self.risk_value


class Human(Player):
    def __init__(self):
        self._risk_level = 'max'
        super().__init__('Player 1', self._risk_level)

    # ==========================
    # GamePlay Methods
    # ==========================
    def play_round(self, deck, gameplay):
        while True:
            self.clear_screen()
            gameplay.display_round_banner()
            gameplay.display_hands()
            self.assess_hand()
            if not self.turn_complete:
                self.hit_or_stand()
            if self.turn_complete:
                break
            self.hit(deck)

    def hit_or_stand(self):
        while True:
            print(F"{self.name} Turn:")
            play = input('Hit or stand? (h/s): ').lower()
            if play in ('s', 'stand'):
                self.end_turn()
                break
            if play in ('h', 'hit'):
                break
            print('Incorrect input, please try again.')

    # ==========================
    #  Predicate Methods
    # ==========================
    def is_playable(self):
        return self.money > 0 and self.money <= 10

    # ==========================
    #  Display Methods
    # ==========================
    def display_gains_losses(self):
        if self.money > 5:
            print(F"You gained ${self.money - 5}!")
        elif self.money < 5:
            print(F"You lost ${5 - self.money}!")
        else:
            print("You didn't gain or lose any money.")


class Computer(Player):
    pass


class Dealer(Computer):
    def __init__(self):
        self._risk_level = 'medium'
        super().__init__('Dealer', self._risk_level)

# ==========================
#  Future Development
# ==========================
class AI(Computer):
    AI_NUM = 1
    def __init__(self):
        name = F"AI {self.__class__.AI_NUM}"
        self._risk_level = random.choice(['low', 'medium', 'high'])
        super().__init__(name, self._risk_level)
        self.__class__.AI_NUM += 1
