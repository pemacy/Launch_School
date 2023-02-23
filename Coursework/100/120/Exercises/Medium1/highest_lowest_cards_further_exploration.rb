class Card
  attr_reader :rank, :suit
  include Comparable

  FACE_CARDS = {'Ace' => 14, 'Kings' => 13, 'Queen' => 12, 'Jack' => 11}
  SUIT_RANKING = {'Spades' => 4, 'Hearts' => 3, 'Clubs' => 2, 'Diamonds' => 1}

  def initialize(rank, suit)
    @rank = rank
    @suit = suit
  end

  def to_s
    "#{rank} of #{suit}"
  end

  def <=>(card)
    if value != card.value
      value <=> card.value
    else
      suit_value <=> card.suit_value
    end

    #Better Solution:
    [value, suit_value] <=> [card.value, suit_value]
  end

  protected

  def value
    FACE_CARDS.fetch(@rank, @rank)
  end

  def suit_value
    SUIT_RANKING.fetch(@suit)
  end
end

cards = [Card.new(9, 'Clubs'),
         Card.new(8, 'Clubs'),
         Card.new(8, 'Spades'),
         Card.new(8, 'Diamonds')]
puts cards.min
puts cards.max
puts cards.sort
