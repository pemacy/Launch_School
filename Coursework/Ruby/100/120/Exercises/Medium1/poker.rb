require 'pry'
require_relative 'deck_of_cards'

class PokerHand
  def initialize(deck)
    deck.class != Deck ? @hand = deck : new_hand(deck)
  end

  def new_hand(deck)
    @hand = []
    5.times { @hand << deck.draw }
  end

  def print
    puts @hand
  end

  def evaluate
    case
    when royal_flush?     then 'Royal flush'
    when straight_flush?  then 'Straight flush'
    when four_of_a_kind?  then 'Four of a kind'
    when full_house?      then 'Full house'
    when flush?           then 'Flush'
    when straight?        then 'Straight'
    when three_of_a_kind? then 'Three of a kind'
    when two_pair?        then 'Two pair'
    when pair?            then 'Pair'
    else                       'High card'
    end
  end

  private

  def royal_flush?
    same_suit? && hand_by_rank == [10, 'Jack', 'Queen', 'King', 'Ace']
  end

  def straight_flush?
    same_suit? && consecutive_order?
  end

  def four_of_a_kind?
    count_duplicates[0] == 4
  end

  def full_house?
    count_duplicates[0] == 2 && count_duplicates[1] == 3
  end

  def flush?
    same_suit?
  end

  def straight?
    consecutive_order?
  end

  def three_of_a_kind?
    count_duplicates[0] == 3
  end

  def two_pair?
    count_duplicates[0] == 2 && count_duplicates[1] == 2
  end

  def pair?
    count_duplicates[0] == 2
  end

  def count_duplicates
    hand = hand_by_values
    duplicates = Hash.new(0)
    hand.each { |e| duplicates[e] += 1 }
    duplicates.delete_if { |_,num| num == 1}.values.sort
  end

  def same_suit?
    suit = @hand[0].suit
    @hand.all? { |card|  card.suit == suit }
  end

  def consecutive_order?
    hand = hand_by_values
    (hand[0]..(hand[0] + 4)).to_a == hand
  end

  def hand_by_values
    @hand.sort_by! { |c| c.value }.map { |c| c.value }
  end

  def hand_by_rank
    @hand.sort_by! { |c| c.value }.map { |c| c.rank }
  end
end


# Testing your class:

hand = PokerHand.new(Deck.new)
hand.print
# puts hand.evaluate

# Danger danger danger: monkey
# patching for testing purposes.
class Array
  alias_method :draw, :pop
end

# Test that we can identify each PokerHand type.
hand = PokerHand.new([
  Card.new(10,      'Hearts'),
  Card.new('Ace',   'Hearts'),
  Card.new('Queen', 'Hearts'),
  Card.new('King',  'Hearts'),
  Card.new('Jack',  'Hearts')
])
puts hand.evaluate == 'Royal flush'

hand = PokerHand.new([
  Card.new(8,       'Clubs'),
  Card.new(9,       'Clubs'),
  Card.new('Queen', 'Clubs'),
  Card.new(10,      'Clubs'),
  Card.new('Jack',  'Clubs')
])
puts hand.evaluate == 'Straight flush'

hand = PokerHand.new([
  Card.new(3, 'Hearts'),
  Card.new(3, 'Clubs'),
  Card.new(5, 'Diamonds'),
  Card.new(3, 'Spades'),
  Card.new(3, 'Diamonds')
])
puts hand.evaluate == 'Four of a kind'

hand = PokerHand.new([
  Card.new(3, 'Hearts'),
  Card.new(3, 'Clubs'),
  Card.new(5, 'Diamonds'),
  Card.new(3, 'Spades'),
  Card.new(5, 'Hearts')
])
puts hand.evaluate == 'Full house'

hand = PokerHand.new([
  Card.new(10, 'Hearts'),
  Card.new('Ace', 'Hearts'),
  Card.new(2, 'Hearts'),
  Card.new('King', 'Hearts'),
  Card.new(3, 'Hearts')
])
puts hand.evaluate == 'Flush'

hand = PokerHand.new([
  Card.new(8,      'Clubs'),
  Card.new(9,      'Diamonds'),
  Card.new(10,     'Clubs'),
  Card.new(7,      'Hearts'),
  Card.new('Jack', 'Clubs')
])
puts hand.evaluate == 'Straight'

hand = PokerHand.new([
  Card.new(3, 'Hearts'),
  Card.new(3, 'Clubs'),
  Card.new(5, 'Diamonds'),
  Card.new(3, 'Spades'),
  Card.new(6, 'Diamonds')
])
puts hand.evaluate == 'Three of a kind'

hand = PokerHand.new([
  Card.new(9, 'Hearts'),
  Card.new(9, 'Clubs'),
  Card.new(5, 'Diamonds'),
  Card.new(8, 'Spades'),
  Card.new(5, 'Hearts')
])
puts hand.evaluate == 'Two pair'

hand = PokerHand.new([
  Card.new(2, 'Hearts'),
  Card.new(9, 'Clubs'),
  Card.new(5, 'Diamonds'),
  Card.new(9, 'Spades'),
  Card.new(3, 'Diamonds')
])
puts hand.evaluate == 'Pair'

hand = PokerHand.new([
  Card.new(2,      'Hearts'),
  Card.new('King', 'Clubs'),
  Card.new(5,      'Diamonds'),
  Card.new(9,      'Spades'),
  Card.new(3,      'Diamonds')
])
puts hand.evaluate == 'High card'
