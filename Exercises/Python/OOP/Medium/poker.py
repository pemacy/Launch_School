'''
In the previous two exercises, you developed a Card class and a Deck class. You are now going to use those classes to create and evaluate poker hands. Create a class, PokerHand, that takes 5 cards from a Deck of Cards and evaluates those cards as a poker hand.

If you are unfamiliar with Poker, please see this description of the various hand types. Since we won't actually be playing a game of Poker, it isn't necessary to know how to play.
'''

from card import Card
from deck import Deck

# Include Card and Deck classes from the last two exercises.

class PokerHand:
    def __init__(self, deck):
        self.deck = deck
        self.hand = []
        self.init_hand()

    def init_hand(self):
        for _ in range(5):
            self.hand.append(self.deck.draw())
        self.ranks_in_hand = [card.rank for card in sorted(self.hand)]
        self.suits_in_hand = [card.suit for card in self.hand]

    def print(self):
        for card in self.hand:
            print(card)

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"

    def _is_royal_flush(self):
        return self._is_royal_straight() and self._is_flush()

    def _is_straight_flush(self):
        return self._is_straight() and self._is_flush()

    def _is_four_of_a_kind(self):
        for rank in set(self.ranks_in_hand):
            if self.ranks_in_hand.count(rank) == 4: return True
        return False

    def _is_full_house(self):
        return self._is_three_of_a_kind() and self._is_pair()

    def _is_flush(self):
        return len(set([card.suit for card in self.hand])) == 1

    def _is_royal_straight(self):
        for royal in Deck.ROYALS:
            if royal not in self.ranks_in_hand: return False
        return True

    def _is_straight(self):
        start_idx = Deck.RANKS.index(self.ranks_in_hand[0])
        return Deck.RANKS[start_idx:start_idx + 5] == self.ranks_in_hand

    def _is_three_of_a_kind(self):
        for rank in set(self.ranks_in_hand):
            if self.ranks_in_hand.count(rank) == 3: return True
        return False

    def _is_two_pair(self):
        pair_marker = 0
        for rank in set(self.ranks_in_hand):
            if self.ranks_in_hand.count(rank) == 2: pair_marker += 1
        return pair_marker == 2

    def _is_pair(self):
        pair_marker = 0
        for rank in set(self.ranks_in_hand):
            if self.ranks_in_hand.count(rank) == 2: pair_marker += 1
        return pair_marker == 1
