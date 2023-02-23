CONVERT = (0..9).to_a.map{|el| el.to_s}

def num_to_str_signed(num)
  str = ''
  num < 0 ? sign = -1 : sign = 1
  num *= sign
  loop do
    num, remainder = num.divmod(10)
    str.prepend(CONVERT[remainder])
    break if num < 1
  end
  sign < 0 ? str.prepend('-') : str
end

p num_to_str_signed(-123)
