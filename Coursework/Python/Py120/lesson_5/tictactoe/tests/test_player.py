import unittest
from unittest.mock import patch
from io import StringIO
import sys
from src.player import Human
from src.player import Computer
from src.board import Board

class TestPlayerClass(unittest.TestCase):
    def test_new_human_intialization(self):
        h = Human()
        assert isinstance(h, Human)

    def test_new_computer_initialization(self):
        c = Computer()
        assert isinstance(c, Computer)

    def test_human_marker(self):
        h = Human()
        assert h.marker == 'X'

    def test_computer_marker(self):
        c = Computer()
        assert c.marker == 'O'

    @patch('builtins.input', side_effect = ['1'])
    def test_human_move(self, mocked_input):
        h = Human()
        b = Board()
        h.move(b)
        assert len(h.squares) == 1
        assert h.squares.pop().position == '1'

    def test_computer_move(self):
        c = Computer()
        b = Board()
        c.move(b)
        assert len(c.squares) == 1


    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect = ['a', '1'])
    def test_human_move_input_incorrect(self, mocked_input, mock_stdout):
        h = Human()
        b = Board()
        h.move(b)
        # print(mock_stdout.getvalue(), file=sys.stderr)
        expected = 'Square must be a number from 1-9\nPlease try again\n'
        assert mock_stdout.getvalue() == expected

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect = ['1', '2'])
    def test_human_move_input_square_taken(self, mocked_input, mock_stdout):
        h = Human()
        b = Board()
        b.mark_square(h, '1')
        h.move(b)
        # print(mock_stdout.getvalue(), file=sys.stderr)
        expected = 'That square is taken\nPlease try again\n'
        assert mock_stdout.getvalue() == expected
