# frozen_string_literal: true

# We want to iterate through the numbers array and return a new array containing
# only the even numbers. However, our code isn't producing the expected output.
# Why not? How can we change it to produce the expected result?

numbers = [5, 2, 9, 6, 3, 1, 8]

even_numbers = numbers.map do |n|
  n if n.even?
end

p even_numbers # expected output: [2, 6, 8]

# => the output will be [nil, 2, nil, 6, nil, nil, 8]
# map will put a value for each item in the array
#
# to get only the elements that return true to the condition, use #select
