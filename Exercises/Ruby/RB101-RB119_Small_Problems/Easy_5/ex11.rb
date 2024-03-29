# frozen_string_literal: true

# Write a method that takes one argument, a positive integer, and returns a list
# of the digits in the number.

def digit_list(num)
  if num < 10
    [num % 10]
  else
    num, digit = num.divmod(10)
    digit_list(num).push(digit)
  end
end

p digit_list(12345) == [1, 2, 3, 4, 5]     # => true
puts digit_list(7) == [7]                     # => true
puts digit_list(375290) == [3, 7, 5, 2, 9, 0] # => true
puts digit_list(444) == [4, 4, 4]             # => true
