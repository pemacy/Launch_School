def sum(num)
  sum = 0
  num = num.to_s.chars
  for n in num
    sum += n.to_i
  end
  sum
end

# WITH REDUCE
def sum_reduce(num)
  num.to_s.chars.map(&:to_i).reduce(:+)
end

puts sum(23) == 5
puts sum(496) == 19
puts sum(123_456_789) == 45

puts sum_reduce(14)
