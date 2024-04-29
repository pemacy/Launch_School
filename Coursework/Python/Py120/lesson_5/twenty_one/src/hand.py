# pylint: disable=import-error, use-a-generator
from src.constants import BlackjackConstants

class Hand:
    def __init__(self):
        self._cards = []

    @property
    def cards(self):
        return self._cards

    def clear(self):
        self._cards.clear()

    def add_card(self, card):
        self.cards.append(card)

    @property
    def value(self):
        if self.has_ace():
            return self.optimized_ace_value()
        return sum([card.value for card in self.cards])

    def hidden_value(self):
        return sum([ card.value for card in self.cards[1:] ])

    # =============================
    # Predicate Methods
    # =============================
    def is_bust(self):
        return self.value >= BlackjackConstants.BUST and \
               self.optimized_ace_value() >= BlackjackConstants.BUST

    def has_ace(self):
        return any([ card.is_ace() for card in self.cards ])

    # =============================
    # Determining Value with Aces
    # =============================
    def ace_value_combos(self):
        aces = [11] * self.num_aces()
        combos = []
        combos.append(aces[:])
        for i in range(self.num_aces()):
            aces = aces[:]
            aces[i] = 1
            combos.append(aces)
        return combos

    def ace_sum_combos(self):
        return [ sum(combo) for combo in self.ace_value_combos()]

    def non_ace_sum(self):
        return sum([ card.value for card in self.cards if card.rank != 'Ace' ])

    def optimized_ace_value(self):
        if self.has_ace():
            sums = []
            for ace_sum in self.ace_sum_combos():
                sums.append(ace_sum + self.non_ace_sum())

            valid_sums = [hand_sum for hand_sum in sums
                        if hand_sum < BlackjackConstants.BUST]
            if valid_sums:
                return max(valid_sums)
            return min(sums)
        return self.value


    def num_aces(self):
        return len([1 for card in self.cards if card.rank == 'Ace'])

    # =============================
    # Display
    # =============================
    def __str__(self):
        return '\n'.join([self.line1_str(),
                          self.line2_str(),
                          self.line3_str(),
                          self.line4_str(),
                          self.line5_str(),
                          self.line6_str(),
                          self.line7_str()])

    def hidden(self):
        return '\n'.join([self.line1_str(),
                          self.line2_str(True),
                          self.line3_str(),
                          self.line4_str(True),
                          self.line5_str(),
                          self.line6_str(True),
                          self.line7_str()])

    def display(self):
        print(self)

    def display_hidden(self):
        print(self.hidden())

    def line1_str(self):
        template = '+' + 7 * '-' + '+'
        line = ''
        for _ in range(len(self.cards)):
            line += template
            line += '  '
        line = line.strip()
        return line

    def line2_str(self, hidden=False):
        line = ''
        for i, card in enumerate(self.cards):
            if i == 0 and hidden:
                template = '| ' + card.hidden_suite_abr() + 5 * ' ' + '|'
            else:
                template = '| ' + card.suite_abr() + 5 * ' ' + '|'
            line += template
            line += '  '
        line = line.strip()
        return line

    def line3_str(self):
        template = '|' + 7 * ' ' + '|'
        line = ''
        for _ in range(len(self.cards)):
            line += template
            line += '  '
        line = line.strip()
        return line

    def line4_str(self, hidden=False):
        line = ''
        for i, card in enumerate(self.cards):
            if i == 0 and hidden:
                template = '| ' + card.hidden_rank().center(5) + ' |'
            else:
                template = '| ' + card.rank.center(5) + ' |'
            line += template
            line += '  '
        line = line.strip()
        return line

    def line5_str(self):
        return self.line3_str()

    def line6_str(self, hidden=False):
        line = ''
        for i, card in enumerate(self.cards):
            if i == 0 and hidden:
                template = '|' + 5 * ' '  + card.hidden_suite_abr() + ' |'
            else:
                template = '|' + 5 * ' '  + card.suite_abr() + ' |'
            line += template
            line += '  '
        line = line.strip()
        return line

    def line7_str(self):
        return self.line1_str()
