import unittest
from unittest.mock import patch
from io import StringIO
# import sys
from src.player import Human
from src.player import Dealer
from src.player import AI
from src.deck import Deck
from src.card import Card

class TestPlayerInitialization(unittest.TestCase):
    def test_instance_from_human_class(self):
        p = Human()
        assert p.__class__ == Human

    def test_instance_from_dealer_class(self):
        p = Dealer()
        assert p.__class__ == Dealer

    def test_instance_from_ai_class(self):
        p = AI()
        assert p.__class__ == AI

    def test_human_hand_empty(self):
        p = Human()
        assert len(p.hand.cards) == 0

    def test_dealer_hand_empty(self):
        p = Dealer()
        assert len(p.hand.cards) == 0

    def test_ai_hand_empty(self):
        p = AI()
        assert len(p.hand.cards) == 0

    def test_turn_complete(self):
        h = Human()
        assert h.turn_complete is False

class TestAddingCardsToHand(unittest.TestCase):
    def test_adding_card_to_player_hand(self):
        h = Human()
        d = Deck()
        assert len(h.hand.cards) == 0
        assert len(d.cards) == 52
        h.hit(d)
        assert len(h.hand.cards) == 1
        assert len(d.cards) == 51

class TestDisplayPlayer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p = Human()
        cls.c1 = Card(rank='Queen', suite='Spades')
        cls.c2 = Card(rank='10', suite='Hearts')
        cls.c3 = Card(rank='5', suite='Hearts')

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_player(self, mock_stdout):
        self.p.reset()
        self.p.hand.add_card(self.c1)
        self.p.hand.add_card(self.c2)
        l0 = f'{self.p.name}\n'
        l01 = f'Money: ${self.p.money}\n'
        l1 = '+-------+  +-------+\n'
        l2 = '| S     |  | H     |\n'
        l3 = '|       |  |       |\n'
        l4 = '| Queen |  |   10  |\n'
        l5 = '|       |  |       |\n'
        l6 = '|     S |  |     H |\n'
        l7 = '+-------+  +-------+\n'
        l8 = F"Score: {self.p.hand.value}\n"
        expected = l0 + l01 + l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8
        print(self.p)
        assert mock_stdout.getvalue() == expected

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_player_busts(self, mock_stdout):
        self.p.reset()
        self.p.hand.add_card(self.c1)
        self.p.hand.add_card(self.c2)
        self.p.hand.add_card(self.c3)
        l0 = f'{self.p.name}\n'
        l01 = f'Money: ${self.p.money}\n'
        l1 = '+-------+  +-------+  +-------+\n'
        l2 = '| S     |  | H     |  | H     |\n'
        l3 = '|       |  |       |  |       |\n'
        l4 = '| Queen |  |   10  |  |   5   |\n'
        l5 = '|       |  |       |  |       |\n'
        l6 = '|     S |  |     H |  |     H |\n'
        l7 = '+-------+  +-------+  +-------+\n'
        l8 = F"Score: {self.p.hand.value}\n"
        l9 = F"{self.p.name} has busted\n"
        expected = l0 + l01 + l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9
        print(self.p)
        assert mock_stdout.getvalue() == expected

# class TestComputerRoundPlay(unittest.TestCase):
#     def test_computer_round_play(self):
#         d = Deck()
#         c = AI()
#         c.play_round(d)
#         assert c.turn_complete is True
#         assert len(c.hand.cards) > 0

# pylint: disable=unused-argument
# class TestHumanRoundPlay(unittest.TestCase):
#     @patch('builtins.input', side_effect=['h', 'h', 's'])
#     @patch('sys.stdout', new_callable=StringIO)
#     def test_human_round_play(self, mock_input, mock_stdout):
#         d = Deck()
#         h = Human()
#         h.play_round(d)
#         print(h, file=sys.stderr)
#         assert h.turn_complete is True
#         assert len(h.hand.cards) == 2

#     @patch('builtins.input', side_effect=['h', 'h', 'h', 'h', 'h', 'h', 's'])
#     @patch('sys.stdout', new_callable=StringIO)
#     def test_human_round_play_bust(self, mock_input, mock_stdout):
#         d = Deck()
#         h = Human()
#         h.play_round(d)
#         print(h, file=sys.stderr)
#         assert h.has_busted() is True
