from src.player import NonePlayer

class Square:
    BOARD_COLUMNS = 3

    def __init__(self, position):
        self.position = position
        self.reset()

    def is_empty(self):
        return isinstance(self.owner, NonePlayer)

    def is_taken(self):
        return not self.is_empty()

    def set_player(self, owner):
        self.owner = owner

    def reset(self):
        self.owner = NonePlayer()

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        self._owner = owner

    @property
    def marker(self):
        return self.owner.marker

    @property
    def position(self):
        return self._position

    @property
    def empty_marker(self):
        return ' '

    @position.setter
    def position(self, position):
        if isinstance(position, (int,str)):
            self._position = str(position)
        else:
            raise TypeError('Square must be initialized with int or str')

    def is_end_square(self):
        return int(self.position) % Square.BOARD_COLUMNS == 0

    def selection_guide(self):
        if self.is_end_square():
            suffix = '\n'
        else:
            suffix = '|'
        if isinstance(self.owner, NonePlayer):
            return self.position.center(5) + suffix
        return self.empty_marker.center(5) + suffix

    def __str__(self):
        if self.is_end_square():
            suffix = '\n'
        else:
            suffix = '|'
        return self.owner.marker.center(5) + suffix
