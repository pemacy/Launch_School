'''
Using the Card class from the previous exercise, create a Deck class that contains all of the standard 52 playing cards. Use the following code to start your work:
'''

import random

class Card:
    CARD_RANKING = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __eq__(self, other):
        return self.rank_value() == other.rank_value()

    def __ne__(self, other):
        return self.rank_value() != other.rank_value()

    def __lt__(self, other):
        return self.rank_value() < other.rank_value()

    def __le__(self, other):
        return self.rank_value() <= other.rank_value()

    def __gt__(self, other):
        return self.rank_value() > other.rank_value()

    def __ge__(self, other):
        return self.rank_value() >= other.rank_value()

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def rank_value(self):
        return self.CARD_RANKING.index(self.rank)

class Deck:
    RANKS = list(range(2,11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self):
        self.deck = []
        self.draw_number = 0
        self.init_deck()

    def init_deck(self):
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.deck.append(Card(rank, suit))

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


deck = Deck()
drawn = []
for _ in range(52):
    drawn.append(deck.draw())

count_rank_5 = sum([1 for card in drawn if card.rank == 5])
count_hearts = sum([1 for card in drawn if card.suit == 'Hearts'])

print(count_rank_5 == 4)      # True
print(count_hearts == 13)     # True

drawn2 = []
for _ in range(52):
    drawn2.append(deck.draw())

print(drawn != drawn2)        # True (Almost always).
