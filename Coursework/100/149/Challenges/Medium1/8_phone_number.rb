class PhoneNumber
  MATCH_NUM = /\A1?\W?(\d{3})\W*?\s*?(\d{3})\W*?\s*?(\d{4})\z/

  def initialize(number)
    @number = number.match(MATCH_NUM).to_a[1..-1]
  end

  def number
    invalid ? invalid : @number.join
  end

  def area_code
    @number[0]
  end

  def to_s
    invalid ? invalid : "(#{@number[0]}) #{@number[1]}-#{@number[2]}"
  end

  def invalid
    return ('0' * 10) if @number.nil?
    false
  end
end

# puts PhoneNumber.new('21234567890')
# puts PhoneNumber.new('11234567890')
