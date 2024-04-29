# pylint: disable=unused-import, use-implicit-booleaness-not-comparison
import unittest
from unittest.mock import patch
import sys
from io import StringIO
from src.hand import Hand
from src.card import Card

class TestHandInitialization(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.h = Hand()

    def test_init(self):
        assert self.h.__class__ == Hand

    def test_cards_init(self):
        assert self.h.cards == []

class TestHandOneCard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.h = Hand()

    def test_add_card(self):
        c = Card(rank = 'Queen', suite = 'Spades')
        self.h.add_card(c)
        assert self.h.cards[0] is c

    @patch('sys.stdout', new_callable = StringIO)
    def test_display_hand(self, mock_stdout):
        self.h.display()
        l1 = '+-------+\n'
        l2 = '| S     |\n'
        l3 = '|       |\n'
        l4 = '| Queen |\n'
        l5 = '|       |\n'
        l6 = '|     S |\n'
        l7 = '+-------+\n'
        expected = l1 + l2 + l3 + l4 + l5 + l6 + l7
        # print(expected, file = sys.stderr)
        # print(mock_stdout.getvalue(), file = sys.stderr)
        assert mock_stdout.getvalue() == expected

    @patch('sys.stdout', new_callable = StringIO)
    def test_str(self, mock_stdout):
        print(self.h)
        l1 = '+-------+\n'
        l2 = '| S     |\n'
        l3 = '|       |\n'
        l4 = '| Queen |\n'
        l5 = '|       |\n'
        l6 = '|     S |\n'
        l7 = '+-------+\n'
        expected = l1 + l2 + l3 + l4 + l5 + l6 + l7
        # print(expected, file = sys.stderr)
        # print(mock_stdout.getvalue(), file = sys.stderr)
        assert mock_stdout.getvalue() == expected

class TestHandTwoCards(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        c = Card(rank = 'Queen', suite = 'Spades')
        c2 = Card(rank = '10', suite = 'Hearts')
        cls.h = Hand()
        cls.h.add_card(c)
        cls.h.add_card(c2)

    def test_hand_value(self):
        assert self.h.value == 20

    def test_optimized_ace_value(self):
        assert self.h.optimized_ace_value() == 20

    def test_ace_value_combos(self):
        assert self.h.ace_value_combos() == [[]]

    def test_ace_sum_combos(self):
        assert self.h.ace_sum_combos() == [0]

    def test_non_ace_sum(self):
        assert self.h.non_ace_sum() == 20

    def test_is_bust(self):
        assert self.h.is_bust() is False

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_hand(self, mock_stdout):
        self.h.display()
        l1 = '+-------+  +-------+\n'
        l2 = '| S     |  | H     |\n'
        l3 = '|       |  |       |\n'
        l4 = '| Queen |  |   10  |\n'
        l5 = '|       |  |       |\n'
        l6 = '|     S |  |     H |\n'
        l7 = '+-------+  +-------+\n'
        expected = l1 + l2 + l3 + l4 + l5 + l6 + l7
        # print(expected, file = sys.stderr)
        # print(mock_stdout.getvalue(), file = sys.stderr)
        assert mock_stdout.getvalue() == expected

    @patch('sys.stdout', new_callable = StringIO)
    def test_str(self, mock_stdout):
        print(self.h)
        l1 = '+-------+  +-------+\n'
        l2 = '| S     |  | H     |\n'
        l3 = '|       |  |       |\n'
        l4 = '| Queen |  |   10  |\n'
        l5 = '|       |  |       |\n'
        l6 = '|     S |  |     H |\n'
        l7 = '+-------+  +-------+\n'
        expected = l1 + l2 + l3 + l4 + l5 + l6 + l7
        # print(expected, file = sys.stderr)
        # print(mock_stdout.getvalue(), file = sys.stderr)
        assert mock_stdout.getvalue() == expected

class TestHandThreeCardWithAces(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        c1 = Card(rank='10', suite='Spades')
        c2 = Card(rank='Ace', suite='Diamonds')
        c3 = Card(rank='Ace', suite='Hearts')
        cls.h = Hand()
        cls.h.add_card(c1)
        cls.h.add_card(c2)
        cls.h.add_card(c3)

    def test_hand_value(self):
        assert self.h.value == 12

    def test_optimized_ace_value(self):
        assert self.h.optimized_ace_value() == 12

    def test_ace_value_combos(self):
        assert self.h.ace_value_combos() == [[11,11], [1,11], [1,1]]

    def test_ace_sum_combos(self):
        assert self.h.ace_sum_combos() == [22, 12, 2]

    def test_non_ace_sum(self):
        assert self.h.non_ace_sum() == 10

    def test_is_bust(self):
        assert self.h.is_bust() is False

class TestHandBustWithoutAces(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        c1 = Card(rank='10', suite='Spades')
        c2 = Card(rank='6', suite='Diamonds')
        c3 = Card(rank='King', suite='Hearts')
        cls.h = Hand()
        cls.h.add_card(c1)
        cls.h.add_card(c2)
        cls.h.add_card(c3)

    def test_hand_value(self):
        assert self.h.value == 26

    def test_optimized_ace_value(self):
        assert self.h.optimized_ace_value() == 26

    def test_ace_value_combos(self):
        assert self.h.ace_value_combos() == [[]]

    def test_ace_sum_combos(self):
        assert self.h.ace_sum_combos() == [0]

    def test_non_ace_sum(self):
        assert self.h.non_ace_sum() == 26

    def test_is_bust(self):
        assert self.h.is_bust() is True

class TestHandBustWithAces(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        c1 = Card(rank='10', suite='Spades')
        c2 = Card(rank='2', suite='Diamonds')
        c3 = Card(rank='Ace', suite='Hearts')
        c4 = Card(rank='King', suite='Hearts')
        cls.h = Hand()
        cls.h.add_card(c1)
        cls.h.add_card(c2)
        cls.h.add_card(c3)
        cls.h.add_card(c4)

    def test_hand_value(self):
        assert self.h.value == 23

    def test_ace_value_combos(self):
        assert self.h.ace_value_combos() == [[11], [1]]

    def test_ace_sum_combos(self):
        assert self.h.ace_sum_combos() == [11,1]

    def test_non_ace_sum(self):
        assert self.h.non_ace_sum() == 22

    def test_optimized_ace_value(self):
        assert self.h.optimized_ace_value() == 23

    def test_is_bust(self):
        assert self.h.is_bust() is True

class TestClearHand(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        c1 = Card(rank='10', suite='Spades')
        c2 = Card(rank='Ace', suite='Diamonds')
        c3 = Card(rank='Ace', suite='Hearts')
        cls.h = Hand()
        cls.h.add_card(c1)
        cls.h.add_card(c2)
        cls.h.add_card(c3)

    def test_clear_hand(self):
        self.h.clear()
        assert len(self.h.cards) == 0
