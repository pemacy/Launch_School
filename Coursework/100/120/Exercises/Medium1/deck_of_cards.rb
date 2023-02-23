require_relative 'highest_lowest_cards'

class Deck
  attr_reader :deck

  RANKS = (2..10).to_a + %w(Jack Queen King Ace).freeze
  SUITS = %w(Hearts Clubs Diamonds Spades).freeze

  def initialize
    new_deck
  end

  def draw
    new_deck if @deck.empty?
    @deck.pop
  end

  private

  def new_deck
    @deck = RANKS.map { |r| SUITS.map { |s| Card.new(r,s)  }  }.flatten
    @deck.shuffle!
  end
end

# deck = Deck.new
#
# puts deck.deck[0..3]
#
# drawn = []
# 52.times { drawn << deck.draw }
#
# p drawn.count { |card| card.rank == 5 } == 4
# p drawn.count { |card| card.suit == 'Hearts' } == 13
#
# drawn2 = []
# 52.times { drawn2 << deck.draw }
# p drawn != drawn2
