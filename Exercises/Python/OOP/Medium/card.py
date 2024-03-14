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
