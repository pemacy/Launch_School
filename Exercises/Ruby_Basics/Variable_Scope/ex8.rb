# frozen_string_literal: true

# What will the following code print, and why? Don't run the code until you have tried to answer.

array = [1, 2, 3]

array.each do |element|
  a = element
end

puts a

# => puts will produce an error because 'a' is not defined in the outer scope of the block
