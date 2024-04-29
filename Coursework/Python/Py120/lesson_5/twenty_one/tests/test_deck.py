import unittest
from src.deck import Deck

class TestDeck(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.deck = Deck()

    def test_initialization(self):
        assert self.deck.__class__ == Deck

    def test_deck_size(self):
        assert len(self.deck.cards) == 52

    def test_cards_2_10(self):
        for i in range(2, 11):
            i_cards = [card for card in self.deck.cards if card.rank == str(i)]
            assert len(i_cards) == 4

    def test_face_cards(self):
        face_cards = ['Jack', 'Queen', 'King', 'Ace']
        for face_card in face_cards:
            i_cards = [card for card in self.deck.cards
                       if card.rank == face_card]
            assert len(i_cards) == 4

    def test_suites(self):
        suites = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        for suite in suites:
            i_cards = [card for card in self.deck.cards
                       if card.suite == suite]
            assert len(i_cards) == 13

class TestDeckDraw(unittest.TestCase):
    def test_draw(self):
        d = Deck()
        d.draw()
        assert len(d.cards) == 51
