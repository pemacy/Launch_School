import unittest
from unittest.mock import patch
from io import StringIO
import rps

class TestPlayerClass(unittest.TestCase):
    def test_player_class_creation(self):
        p = rps.rps_players.Player()
        self.assertEqual(p.__class__, rps.rps_players.Player)

    def test_selection_initialized_to_none(self):
        p = rps.rps_players.Player()
        self.assertEqual(p.selection, None)

class TestUserClass(unittest.TestCase):
    def test_user_class_creation(self):
        u = rps.rps_players.User()
        self.assertEqual(u.__class__, rps.rps_players.User)

    @patch('builtins.input', side_effect=['r'])
    def test_user_move(self, mocked_input):
        u = rps.rps_players.User()
        u.move()
        self.assertEqual(u.selection, 'rock')

class ComputerUserClass(unittest.TestCase):
    def test_computer_move(self):
        c = rps.rps_players.Computer()
        c.move()
        self.assertIn(c.selection, c.CHOICES)

class TestRpsClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_rps = rps.RPS()

    def test_initialized_players(self):
        self.assertEqual(type(self.test_rps.user), rps.rps_players.User)
        self.assertEqual(   type(self.test_rps.computer),
                            rps.rps_players.Computer)

    def test_initialized_attributes(self):
        test_rps = rps.RPS()
        self.assertEqual(test_rps.winner, None)

    def test_computer_move(self):
        self.test_rps.computer.move()
        self.assertIn(self.test_rps.computer.selection,
                      self.test_rps.computer.CHOICES)

    def test_compare(self):
        self.test_rps.user.selection = 'rock'
        self.test_rps.computer.selection = 'paper'
        self.test_rps.compare()
        self.assertEqual(self.test_rps.winner, self.test_rps.computer)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_results(self, mock_stdout):
        self.test_rps.display_results()
        assert mock_stdout.getvalue() == \
                "Computer chose paper\nUser chose rock\nComputer Wins!\n"

unittest.main()
