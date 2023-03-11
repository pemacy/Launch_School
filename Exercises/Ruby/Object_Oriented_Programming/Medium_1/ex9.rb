# frozen_string_literal: true

# Using the Card class from the previous exercise, create a Deck class that
# contains all of the standard 52 playing cards. Use the following code to
# start your work:

class Card
  CARD_RANKING = %w(0 1 2 3 4 5 6 7 8 9 10 Jack Queen King Ace).freeze

  attr_reader :rank, :suit

  def initialize(rank, suit)
    @rank = rank.to_s
    @suit = suit
  end

  def <=>(card)
    CARD_RANKING.index(rank) <=> CARD_RANKING.index(card.rank)
  end

  def to_s
    "#{rank} of #{suit}"
  end

  def ==(card)
    self.to_s == card.to_s
  end
end

class Deck
  RANKS = ((2..10).to_a + %w(Jack Queen King Ace)).freeze
  SUITS = %w(Hearts Clubs Diamonds Spades).freeze

  attr_reader :deck

  def initialize
    @deck = create_deck
  end

  def draw
    @deck = create_deck if @deck.empty?

    @deck.pop
  end

  def create_deck
    SUITS.each_with_object([]) do |suit, arr|
      RANKS.each do |rank|
        arr << Card.new(rank, suit)
      end
    end.shuffle
  end
end

# The Deck class should provide a #draw method to deal one card. The Deck
# should be shuffled when it is initialized and, if it runs out of cards, it
# should reset itself by generating a new set of 52 shuffled cards.

# deck = Deck.new
# drawn = []
# 52.times { drawn << deck.draw }
# puts drawn.count { |card| card.rank == 5 } == 4
# puts drawn.count { |card| card.suit == 'Hearts' } == 13

# drawn2 = []
# 52.times { drawn2 << deck.draw }
# puts drawn != drawn2 # Almost always.

# Note that the last line should almost always be true; if you shuffle the deck
# 1000 times a second, you will be very, very, very old before you see two
# consecutive shuffles produce the same results. If you get a false result,
# you almost certainly have something wrong.
