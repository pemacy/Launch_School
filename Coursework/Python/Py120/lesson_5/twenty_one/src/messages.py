class Messages:
    def rules(self):
        return '\n'.join([
            'Game Rules:',
            "\n\t• All players are dealt 2 cards.",
            "\t• You can see both your cards, ",
            "\t\tbut computer player's first card is hidden.",
            "\t• Scores are tallied from the values of the cards in hand.",
            "\t• You win by getting as close to, or equal to, 21 as you can.",
            "\t• During your round:",
            "\t\t• You can add a card to your hand by choosing to Hit.",
            "\t\t• Or you can end your turn by choosing to Stay.",
            "\t• Going over 21 is a 'bust', resulting in an automatic loss.",
            "\t• The game ends if you decide to quit, or if you lose all your",
            "\t\tmoney, or you reach the max wins, which is a gain of $5",
            "\nGood Luck!",
        ])
