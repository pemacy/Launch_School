import unittest
from src.square import Square
from src.board import Board
from src.player import Human
from src.player import Computer

class TestBoardClass(unittest.TestCase):
    def test_new_board_creation(self):
        b = Board()
        s5 = ' ' * 5
        row = F"{s5}|{s5}|{s5}"
        assert b.board_string() == F"{row}\n{row}\n{row}\n"

    def test_is_empty(self):
        b = Board()
        assert b.is_empty() is True

    def test_is_full(self):
        b = Board()
        h = Human()
        for i in range(1, 10):
            b.mark_square(h, i)
        assert b.is_full() is True

    def test_empty_marker_for_unmarked_square(self):
        b = Board()
        assert b.positions['3'].marker == ' '

    def test_player_marker_for_marked_square(self):
        b = Board()
        h = Human()
        b.mark_square(h, '3')
        assert b.positions['3'].marker == 'X'

    def test_marked_board_display(self):
        b = Board()
        h = Human()
        b.mark_square(h, '3')
        s5 = ' ' * 5
        row1 = F"{s5}|{s5}|  X  "
        row = F"{s5}|{s5}|{s5}"
        assert b.board_string() == F"{row1}\n{row}\n{row}\n"

    def test_false_winning_combo_for_empty_board(self):
        b = Board()
        h = Human()
        assert b.has_winning_combo(h) is False

    def test_false_winning_combo_non_winning_board(self):
        b = Board()
        h = Human()
        b.mark_square(h, '1')
        assert b.has_winning_combo(h) is False

    def test_true_winning_combo_winning_board(self):
        b = Board()
        h = Human()
        b.mark_square(h, '1')
        b.mark_square(h, '2')
        b.mark_square(h, '3')
        assert b.has_winning_combo(h) is True

    def test_reset_board(self):
        b = Board()
        h = Human()
        b.mark_square(h, '1')
        b.mark_square(h, '2')
        b.mark_square(h, '3')
        assert b.is_empty() is False
        b.reset()
        assert b.is_empty() is True

    def test_available_positions_all(self):
        b = Board()
        assert b.available_positions == [ str(i) for i in range(1, 10) ]

    def test_available_positions_all_but_one(self):
        b = Board()
        h = Human()
        b.mark_square(h, '1')
        assert b.available_positions == [ str(i) for i in range(2, 10) ]

    def test_winner_human(self):
        b = Board()
        h = Human()
        c = Computer()
        b.mark_square(h, '1')
        b.mark_square(h, '5')
        b.mark_square(h, '9')
        b.mark_square(c, '2')
        b.mark_square(c, '4')
        b.mark_square(c, '8')
        assert b.winner(h, c) == h

    def test_winner_computer(self):
        b = Board()
        h = Human()
        c = Computer()
        b.mark_square(c, '1')
        b.mark_square(c, '4')
        b.mark_square(c, '7')
        b.mark_square(h, '2')
        b.mark_square(h, '5')
        b.mark_square(h, '9')
        assert b.winner(h, c) == c
