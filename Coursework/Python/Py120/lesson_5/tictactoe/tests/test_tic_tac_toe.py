import unittest
from unittest.mock import patch
from io import StringIO
import sys
from tic_tac_toe import TicTacToe
from src.player import Human
from src.player import Computer
from src.player import NonePlayer
from src.board import Board
from src.square import Square

class TestTicTacToe(unittest.TestCase):
    def test_class_initialization(self):
        t = TicTacToe()
        assert t.__class__ == TicTacToe

    def test_human_initialization(self):
        t = TicTacToe()
        assert t.human.__class__ == Human

    def test_computer_initialization(self):
        t = TicTacToe()
        assert t.computer.__class__ == Computer

    def test_board_initialization(self):
        t = TicTacToe()
        assert t.board.__class__ == Board

    def test_current_player_initialization(self):
        t = TicTacToe()
        assert t.current_player == t.human

    def test_swap_current_player(self):
        t = TicTacToe()
        t.swap_current_player()
        assert t.current_player == t.computer

    @patch('builtins.input', side_effect = ['1'])
    def test_current_player_move(self, mock_input):
        t = TicTacToe()
        t.current_player_move()
        assert t.board.is_empty() is False
        assert t.board.get_square('1').owner == t.human

    @patch('sys.stdout', new_callable = StringIO)
    def test_display_results_human(self, mock_stdout):
        t = TicTacToe()
        t.board.mark_square(t.human, '1')
        t.board.mark_square(t.human, '2')
        t.board.mark_square(t.human, '3')
        t.display_results()
        # print(mock_stdout.getvalue(), file = sys.stderr)
        assert mock_stdout.getvalue() == 'Human Player Won!\n'

    @patch('sys.stdout', new_callable = StringIO)
    def test_display_results_no_player(self, mock_stdout):
        t = TicTacToe()
        t.display_results()
        # print(mock_stdout.getvalue(), file = sys.stderr)
        assert mock_stdout.getvalue() == 'No Player Won!\n'
