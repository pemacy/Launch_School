import random

class Player:
    def __init__(self, marker):
        self.marker = marker
        self.squares = set()

    def reset(self):
        self.squares.clear()

    def add_square(self, square):
        self.squares.add(square)

    def square_combo(self):
        return { square.position for square in self.squares }

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker

class Human(Player):
    def __init__(self):
        super().__init__('X')

    def move(self, board):
        position = input('Pick a square: ')
        while not board.mark_square(self, position):
            position = input('Pick a square: ')

    def __str__(self):
        return "Human Player"

class Computer(Player):
    def __init__(self):
        super().__init__('O')

    def move(self, board):
        position = random.choice(board.available_positions)
        board.mark_square(self, position)

    def __str__(self):
        return "Computer Player"

class NonePlayer(Player):
    def __init__(self):
        super().__init__(' ')

    def __str__(self):
        return "No Player"
