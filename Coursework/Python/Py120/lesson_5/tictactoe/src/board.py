from src.square import Square
from src.player import NonePlayer

class Board:
    WIDTH = 3
    SIZE = WIDTH ** 2
    WINNING_SQUARES = ['123', '456', '789', '147', '258', '369', '159', '357']

    def __init__(self):
        self.reset()

    def reset(self):
        self.positions = { str(i): Square(i) for i in range(1,Board.SIZE + 1) }
        self.squares = self.positions.values()

    def mark_square(self, player, position):
        if self.is_valid_selection(position):
            position = str(position)
            square = self.get_square(position)
            square.owner = player
            player.add_square(square)
            return True
        self.display_position_error(position)
        return False

    def winner(self, player1, player2):
        if self.has_winning_combo(player1):
            return player1
        if self.has_winning_combo(player2):
            return player2
        return NonePlayer()

    # ==================================
    # Display Methods
    # ==================================
    def display(self):
        print('Available Squares:')
        print(*self.display_available(), end='', sep='')
        print('\nBoard State:')
        print(*self.squares, end='', sep='')

    def display_available(self):
        return ''.join( [ F"{square.selection_guide()}"
                          for square in self.squares ] )

    def display_position_error(self, position):
        if not self.is_valid_position(position):
            print('Square must be a number from 1-9')
        elif not self.is_position_empty(position):
            print('That square is taken')
        print('Please try again')

    def board_string(self):
        return ''.join( [ F"{square}" for square in self.squares ] )

    # ==================================
    # Square and Position Queries
    # ==================================
    def get_square(self, position):
        if self.is_correct_position_type(position):
            return self.positions[str(position)]
        raise TypeError('Square position must be int or str')

    def valid_positions(self):
        return [ str(i) for i in range(1, Board.SIZE + 1) ]

    @property
    def available_positions(self):
        return [ square.position for square in self.squares
                                    if square.is_empty() ]

    # ==================================
    # Predicate Methods
    # ==================================
    def is_empty(self):
        return all([ square.is_empty() for square in self.squares ])

    def is_full(self):
        return all([ square.is_taken() for square in self.squares ])

    def is_correct_position_type(self, position):
        return isinstance(position, (int,str))

    def is_position_empty(self, position):
        return self.positions[str(position)].is_empty()

    def is_valid_position(self, position):
        return str(position) in self.valid_positions()

    def is_valid_selection(self, position):
        return  self.is_correct_position_type(position) and \
                self.is_valid_position(position) and \
                self.is_position_empty(position)

    def has_winning_combo(self, player):
        for combo in Board.WINNING_SQUARES:
            if player.square_combo() >= set(combo):
                return True
        return False
