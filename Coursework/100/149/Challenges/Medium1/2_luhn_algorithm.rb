class Luhn
  attr_accessor :input

  def initialize (num)
    @input = num.to_s.chars.map(&:to_i)
  end

  def addends
    @input.reverse.map.with_index { |n,i| i.even? ? n : add(n) }.reverse
  end

  def checksum
    addends.reduce(&:+)
  end

  def valid?
    checksum % 10 == 0
  end

  def find_check_sum(num)
    return num if Luhn.new(num).valid?
    find_check_sum(num += 1)
  end

  def self.create(num)
    luhn = new(num)
    luhn.find_check_sum(num * 10)
  end

  private

  def add(n)
    ((n * 2) > 10) ? ((n * 2) - 9) : (n * 2)
  end
end
