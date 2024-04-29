import unittest
from src.card import Card

class TestAceCard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.suite = 'Spades'
        cls.rank = 'Ace'
        cls.c = Card(rank=cls.rank, suite=cls.suite)

    def test_initialization(self):
        assert self.c.__class__ == Card

    def test_rank(self):
        assert self.c.rank == 'Ace'

    def test_suite(self):
        assert self.c.suite == 'Spades'

    def test_value(self):
        assert self.c.value == 11

    def test_alt_value(self):
        assert self.c.alt_value() == 1

    def test_has_alt_value(self):
        assert self.c.has_alt_value() is True

class TestCard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.suite = 'Spades'
        cls.rank = 'King'
        cls.c = Card(rank=cls.rank, suite=cls.suite)

    def test_initialization(self):
        assert self.c.__class__ == Card

    def test_rank(self):
        assert self.c.rank == 'King'

    def test_suite(self):
        assert self.c.suite == 'Spades'

    def test_value(self):
        assert self.c.value == 10

    def test_alt_value(self):
        assert self.c.alt_value() == 10

    def test_has_alt_value(self):
        assert self.c.has_alt_value() is False
