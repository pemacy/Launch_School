class Card
  attr_reader :rank, :suit
  include Comparable

  FACE_CARDS = {'Ace' => 14, 'King' => 13, 'Queen' => 12, 'Jack' => 11}

  def initialize(rank, suit)
    @rank = rank
    @suit = suit
  end

  def to_s
    "#{rank} of #{suit}"
  end

  def <=>(card)
    # rank = self_card_rank
    # other_card = other_card_rank(card.rank)
    #
    # rank <=> other_card
    value <=> card.value
  end

  def value
    FACE_CARDS.fetch(@rank, @rank)
  end

  def convert?(item = @rank)
    item.class == String
  end

  def convert_face_card(item = @rank)
    case item
    when 'Ace' then 14
    when 'King' then 13
    when 'Queen' then 12
    when 'Jack' then 11
    end
  end

  def self_card_rank
    return convert_face_card if convert?
    return @rank unless convert?
  end

  def other_card_rank(item)
    return convert_face_card(item) if convert?(item)
    return item unless convert?(item)
  end
end

# cards = [Card.new(2, 'Hearts'),
#          Card.new(10, 'Diamonds'),
#          Card.new('Ace', 'Clubs')]
# puts cards
# puts cards.min == Card.new(2, 'Hearts')
# puts cards.max == Card.new('Ace', 'Clubs')
#
# cards = [Card.new(5, 'Hearts')]
# puts cards.min == Card.new(5, 'Hearts')
# p cards.max == Card.new(5, 'Hearts')
#
# cards = [Card.new(4, 'Hearts'),
#          Card.new(4, 'Diamonds'),
#          Card.new(10, 'Clubs')]
# puts cards.min.rank == 4
# puts cards.max == Card.new(10, 'Clubs')
#
# cards = [Card.new(7, 'Diamonds'),
#          Card.new('Jack', 'Diamonds'),
#          Card.new('Jack', 'Spades')]
# puts cards.min == Card.new(7, 'Diamonds')
# puts cards.max.rank == 'Jack'
#
# cards = [Card.new(8, 'Diamonds'),
#          Card.new(8, 'Clubs'),
#          Card.new(8, 'Spades')]
# puts cards.min.rank == 8
# puts cards.max.rank == 8

# Output:
#
# 2 of Hearts
# 10 of Diamonds
# Ace of Clubs
# true
# true
# true
# true
# true
# true
# true
# true
# true
# true
