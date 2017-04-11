require 'pry'

class Anagram
  attr_accessor :word

  def initialize(str)
    @word = str.chars.permutation(str.size).to_a.map(&:join)
    @word.delete(str)
  end

  def match(arr)
    arr.select { |s| !([s].map(&:downcase) & word.map(&:downcase)).empty?}
  end

  private

  def validate
    word.class == String
  end
end


# detector = Anagram.new('Orchestra')
# p detector.match %w(cashregister Carthorse radishes)

# detector = Anagram.new('corn')
# p detector.match %w(corn dark Corn rank CORN cron park)
