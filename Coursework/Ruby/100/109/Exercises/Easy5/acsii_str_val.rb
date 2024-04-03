def ascii_value(str)
  ascii_arr = []
  str.each_byte{ |c| ascii_arr << c}
  ascii_arr.reduce(:+)
end

puts ascii_value('')
