def mult3(num)
  n3 = (1..num).select{ |x| x % 3 == 0 || x % 5 == 0}
  # n3.reduce(:+)
  n3.inject { |memo, obj| memo + obj}
end

puts mult3(1000)
