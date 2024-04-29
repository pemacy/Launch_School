# pylint: disable=import-error
import random
from src.card import Card
from src.constants import BlackjackConstants

class Deck:
    def __init__(self):
        self.cards = []
        self.reset()

    def reset(self):
        self.cards.clear()
        for suite in BlackjackConstants.SUITES:
            for rank in BlackjackConstants.CARD_RANKS:
                card = Card(rank = rank, suite = suite)
                self.cards.append(card)
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()
