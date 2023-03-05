# frozen_string_literal: true

# Write a method that takes an Array of integers as input, multiplies all the
# numbers together, divides the result by the number of entries in the Array,
# and then prints the result rounded to 3 decimal places. Assume the array is
# non-empty.

def show_multiplicative_average(arr)
  ave = (arr.reduce(&:*) / arr.size.to_f).round(3).to_s
  # "%.3f" % ave
  format "%.3f", ave
end

puts show_multiplicative_average([3, 5])                # => The result is 7.500
puts show_multiplicative_average([6])                   # => The result is 6.000
puts show_multiplicative_average([2, 5, 7, 11, 13, 17]) # => The result is 28361.667
