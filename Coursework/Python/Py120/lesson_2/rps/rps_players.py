import random

class Player:
    RULES = {
                 'rock': {'beats': 'scissors', 'loses': 'paper'},
                 'paper': {'beats': 'rock', 'loses': 'scissors'},
                 'scissors': {'beats': 'paper', 'loses': 'rock'},
             }
    CHOICES = [ choice for choice in RULES.keys() ]

    def __init__(self):
        self._selection = None

    @property
    def selection(self):
        return self._selection

    @selection.setter
    def selection(self, selection):
        self._selection = selection

    def compatible_compare(self, other):
        return issubclass(self.__class__, Player) and \
               issubclass(other.__class__, Player)

    def __gt__(self, other):
        if self.compatible_compare(other):
            return other.selection == self.RULES[self.selection]['beats']
        return False

    def __eq__(self, other):
        if self.compatible_compare(other):
            return self.selection == other.selection
        return False

    def __lt__(self, other):
        if self.compatible_compare(other):
            return other.selection == self.RULES[self.selection]['loses']
        return False

    def __str__(self):
        return self.__class__.__name__

class User(Player):
    SELECTION_ROSETTA = {   'rock': ['r', 'rock'],
                            'paper': ['p', 'paper'],
                            'scissors': ['s', 'scissor', 'scissors'],
                        }
    VALID_SELECTIONS = [ el for lst in SELECTION_ROSETTA.values()
                            for el in lst ]

    def move(self):
        print('Choose Selection:')
        for obj, selections in self.SELECTION_ROSETTA.items():
            print(F"{selections[0]} - {obj.title()}")
        self.selection = self.validate_move(input('\n>> '))

    def validate_move(self, choice):
        while True:
            if choice.lower() in self.VALID_SELECTIONS:
                for obj, selections in self.SELECTION_ROSETTA.items():
                    if choice in selections:
                        return obj
            print('Invalid selection.')
            self.move()


class Computer(Player):
    def move(self):
        self.selection = random.choice(self.CHOICES)
