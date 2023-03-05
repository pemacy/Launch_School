# frozen_string_literal: true

# What will the following code print, and why? Don't run the code until you have tried to answer.

a = 7
array = [1, 2, 3]

array.each do |element|
  a = element
end

puts a

# => a will be 3, blocks can see variables from outside the scope of the block
