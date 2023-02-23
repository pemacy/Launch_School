require 'pry'

class SumOfMultiples
  attr_accessor :multiples

  def initialize(*args)
    @multiples = args.empty? ? [3,5] : args
  end

  def to(num)
    self.class.to(num, multiples)
  end

  def self.to(num, multiples = [3,5])
    result = (1..num-1).select{|n| is_multiple?(n, multiples)}.reduce(&:+)
    result ? result : 0
  end

  private

  def self.is_multiple?(n, multiples)
    multiples.any?{ |m| n % m == 0}
  end
end

p SumOfMultiples.new.to(7)
p SumOfMultiples.to(4)
