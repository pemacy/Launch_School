class Octal
  attr_accessor :octal

  def initialize(octal)
    @octal = octal.to_i.to_s.chars.map(&:to_i)
  end

  def to_decimal
    return 0 if is_valid?
    idx = 0
    (octal.size - 1).downto(0) do |n|
      octal[idx] = octal[idx] * (8 ** n)
      idx += 1
    end
    octal.reduce(:+)
  end

  def is_valid?
    if octal.join.to_i != 0 &&
      octal.join.to_i.to_s != octal.join ||
      octal.any? { |n| n > 7 }
      return true
    end
    false
  end
end

p Octal.new('011').to_decimal
