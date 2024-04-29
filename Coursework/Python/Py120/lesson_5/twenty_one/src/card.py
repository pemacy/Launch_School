# pylint: disable=import-error
from src.constants import BlackjackConstants

class Card:
    def __init__(self, **kwargs):
        self._rank = kwargs['rank']
        self._suite = kwargs['suite']
        self._value = BlackjackConstants.CARD_VALUE_TABLE[self.rank]

    # ==========================
    # Properties
    # ==========================
    @property
    def rank(self):
        return self._rank

    @property
    def suite(self):
        return self._suite

    @property
    def value(self):
        return self._value

    def alt_value(self):
        if self.is_ace():
            return BlackjackConstants.ACE_ALT_VALUE
        return self.value

    # ==========================
    # Predicate Methods
    # ==========================
    def has_alt_value(self):
        return self.value != self.alt_value()

    def is_ace(self):
        return self.rank == 'Ace'

    # ==========================
    # Display Helper Methods
    # ==========================
    def suite_abr(self):
        return self.suite[0]

    def hidden_suite_abr(self):
        return '?'

    def hidden_rank(self):
        return '?????'
