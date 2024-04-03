module Roman
  DEC_TO_ROM = {1000=>"M", 900=>"CM", 500=>"D", 400=>"CD", 100=>"C",
                    90=>"XC", 50=>"L", 40=>"XL", 10=>"X", 9=>"IX",
                    5=>"V", 4=>"IV", 1=>"I"}

  def to_roman
    p to_roman_by_subtraction
    p to_roman_by_addition
    p reverse_digits
  end

  def to_roman_by_subtraction
    num = self
    DEC_TO_ROM.each_with_object '' do |(decimal_value,roman_numeral), storage|
      until num < decimal_value do
        storage << roman_numeral
        num -= decimal_value
      end
    end
  end

  def to_roman_by_addition
    val = 0
    stor = ''
    loop do
      stor, val = add_to_num(stor, val)
      break if val == self
    end
    stor
  end

  private

  def add_to_num(stor, val)
    DEC_TO_ROM.each do |decimal_value, roman_numeral|
      if decimal_value + val <= self
        stor << roman_numeral
        val += decimal_value
        break
      end
    end
    [stor, val]
  end

  def reverse_digits
    to_s.chars.reverse.map(&:to_i)
  end
end

class Fixnum
  include Roman
end

83.to_roman
