# frozen_string_literal: true

require_relative 'ex9.rb'

# In the previous two exercises, you developed a Card class and a Deck class.
# You are now going to use those classes to create and evaluate poker hands.
# Create a class, PokerHand, that takes 5 cards from a Deck of Cards and
# evaluates those cards as a Poker hand. If you've never played poker before,
# you may find this overview of poker hands useful.

# You should build your class using the following code skeleton:

# Include Card and Deck classes from the last two exercises.

class PokerHand
  attr_reader :hand

  def initialize(deck)
    @hand = Array.new(5) { deck.draw }
  end

  def print
    puts hand
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

  # private

  def royal_flush?
    all_same_suit? && royal_sequential?
  end

  def straight_flush?
    all_same_suit? && sequential_rank?
  end

  def four_of_a_kind?
    count_ranks == [1,4]
  end

  def full_house?
    count_ranks == [2,3]
  end

  def flush?
    all_same_suit?
  end

  def straight?
    sequential_rank?
  end

  def three_of_a_kind?
    count_ranks == [1,1,3]
  end

  def two_pair?
    count_ranks == [1,2,2]
  end

  def pair?
    count_ranks == [1,1,1,2]
  end

  def all_same_suit?
    hand.map(&:suit).uniq.size == 1
  end

  def sequential_rank?
    sorted = hand.sort
    first_card = sorted.first
    index_tracker = Card::CARD_RANKING.index(first_card.rank) - 1
    hand.sort.all? do |card|
      index_tracker += 1
      Card::CARD_RANKING.index(card.rank) == index_tracker
    end
  end

  def royal_sequential?
      hand.sort.map(&:rank).map(&:to_s) == %w(10 Jack Queen King Ace)
  end

  def count_ranks
    hand.each_with_object(Hash.new(0)) do |card, hsh|
      hsh[card.rank] += 1
    end.values.sort
  end
end

# Testing your class:

hand = PokerHand.new(Deck.new)
hand.print
puts hand.evaluate

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
  Card.new('Queen', 'Clubs'),
  Card.new('King',  'Diamonds'),
  Card.new(10,      'Clubs'),
  Card.new('Ace',   'Hearts'),
  Card.new('Jack',  'Clubs')
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

# The exact cards and the type of hand will vary with each run.

# Most variants of Poker allow both Ace-high (A, K, Q, J, 10) and Ace-low (A,
# 2, 3, 4, 5) straights. For simplicity, your code only needs to recognize Ace
# -high straights.

# If you are unfamiliar with Poker, please see this description of the various
# hand types. Since we won't actually be playing a game of Poker, it isn't
# necessary to know how to play.
