class BlackjackConstants:
    # Card Ranks
    LOW_CARD_RANKS = [ '2', '3', '4', '5', '6', '7', '8', '9', '10' ]
    FACE_CARD_RANKS = [ 'Jack', 'Queen', 'King', 'Ace' ]
    CARD_RANKS = LOW_CARD_RANKS + FACE_CARD_RANKS

    # Deck Constant
    SUITES = [ 'Spades', 'Clubs', 'Hearts', 'Diamonds' ]

    # Card Values
    LOW_CARD_VALUES = list(range(2,11))
    FACE_CARD_VALUES = [ 10, 10, 10, 11 ]
    CARD_VALUES = LOW_CARD_VALUES + FACE_CARD_VALUES

    CARD_VALUE_TABLE = dict(zip(CARD_RANKS, CARD_VALUES))

    ACE_ALT_VALUE = 1

    BUST = 22

    # AI Risk Levels
    LOW_RISK_VALUE = 15
    MEDIUM_RISK_VALUE = 17
    HIGH_RISK_VALUE = 20
    MAX_RISK_VALUE = 21
    RISK_LEVELS = {
            'low': LOW_RISK_VALUE,
            'medium': MEDIUM_RISK_VALUE,
            'high': HIGH_RISK_VALUE,
            'max': MAX_RISK_VALUE,
            }

    ROUNDS_TO_PLAY = 2
