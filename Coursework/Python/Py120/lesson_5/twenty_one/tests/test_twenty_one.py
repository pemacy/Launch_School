# pylint: disable=unused-import
import unittest
from unittest.mock import patch
from io import StringIO
import sys
from twenty_one import TwentyOne

class TestTwentyOne(unittest.TestCase):
    def test_object_creation(self):
        t = TwentyOne()
        assert t.__class__ == TwentyOne

    @patch('sys.stdout', new_callable=StringIO)
    def test_welcome_message(self, mock_stdout):
        t = TwentyOne()
        expected = 'Welcome to 21 BlackJack\n'
        # print(expected, file = sys.stderr)
        t.display_welcome_message()
        assert mock_stdout.getvalue() == expected

    def test_initial_deal_cards(self):
        t = TwentyOne()
        t.initial_deal()
        for player in t.players:
            assert len(player.hand.cards) == 2
