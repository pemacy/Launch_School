# frozen_string_literal: true

# In the code below, an array containing five numbers is assigned to numbers.

numbers = [5, 9, 21, 26, 39]

# Use Array#select to iterate over numbers and return a new array that contains
# only numbers divisible by three. Assign the returned array to a variable
# named divisible_by_three and print its value using #p.

div_by_3 = numbers.select do |num|
  (num % 3).zero?
end

p div_by_3
