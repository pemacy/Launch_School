'21 Backjack Messages'

messages = {}

def welcome_messages():
    messages['welcome'] = [
        'Game Rules:',
        "\n\t• All players are dealt 2 cards.",
        "\t• You can see both your cards, ",
        "\t• but computer player's first card is hidden.",
        "\t• Scores are tallied from the values of the cards in your hand.",
        "\t• You win by getting as close to, or equal to, 21 as you can.",
        "\t• During your round:",
        "\t\t• You can add a card to your hand by choosing to Hit.",
        "\t\t• Or you can end your turn by choosing to Stay.",
        "\t• Going over 21 is a 'bust', resulting in an automatic loss.",
        "\t• The Dealer wins any tie breakers.",
        "\nGood Luck!",
    ]

def hit_stay_message():
    messages['hit_stay'] = '\nWould you like to hit or stay? (h/s): '

def collect_messages():
    welcome_messages()
    hit_stay_message()
    return messages
