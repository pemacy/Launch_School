import random
from card import Card

class Deck:
    FACE_CARDS = ['Jack', 'Queen', 'King', 'Ace']
    ROYALS = [10] + FACE_CARDS
    RANKS = list(range(2,10)) + ROYALS
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self):
        self.deck = []
        self.draw_number = 0
        self.init_deck()

    def init_deck(self):
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.deck.append(Card(rank, suit))
        self.shuffle_deck()

    def draw(self):
        return self.deck[self.get_draw_number()]

    def random_card(self):
        return random.randint(0, 52)

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def get_draw_number(self):
        num = self.draw_number
        self.draw_number += 1
        if self.draw_number == 52:
            self.shuffle_deck()
            self.draw_number = 0
        return num
