class Trinary
  attr_accessor :tri

  def initialize(num)
    @tri = num
  end

  def to_decimal
    validate
    convert_to_decimal
  end

  private

  def convert_to_decimal(n = tri.to_i, count = 0)
    return 0 if n.zero?
    n, rem = n.divmod(10)
    (rem * (3 ** count)) + convert_to_decimal(n, count + 1)
  end

  def validate
    remove_leading_zeros
    return false unless int_to_str_match?
    return false unless invalid_number_in_tri?
    true
  end

  def int_to_str_match?
    tri.to_i.to_s == tri
  end

  def invalid_number_in_tri?
    for idx in (0..tri.size-1)
      return false if tri[idx] =~ /[0-2]/
    end
    true
  end

  def remove_leading_zeros
    for idx in (0..tri.size-1)
      break if tri[idx] =~ /[^0]/
    end
    self.tri = tri[idx..-1]
  end
end

p tri_con = Trinary.new('00d0110').to_decimal
