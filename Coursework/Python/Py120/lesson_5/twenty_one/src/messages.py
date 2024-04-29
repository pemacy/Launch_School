class Messages:
    def rules(self):
        return '\n'.join([
            'Game Rules:',
            "\n\t• All players are dealt 2 cards.",
            "\t• You will see both your cards and your score.",
            "\t• The Dealer's first card is hidden, only the face up card " +\
                "score is shown during round play.",
            "\t• Scores are tallied from the values of the cards in hand.",
            "\t• You win a round by getting the highest score without going "+\
                "over 21.",
            "\t• If both players get the same score, both win that round.",
            "\t• During your round:",
            "\t\t• You can add a card to your hand by choosing to Hit.",
            "\t\t• Or you can end your turn by choosing to Stay.",
            "\t• Going over 21 is a 'bust', resulting in an automatic loss.",
            "\t• The game ends if you decide to quit, or if you lose all" +\
                " your money, or your money reaches $10.",
            "\nGood Luck!",
        ])
