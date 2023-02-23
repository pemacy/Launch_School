# frozen_string_literal: true

# What will the following code print, and why? Don't run the code until you have tried to answer.

a = 7
array = [1, 2, 3]

array.each do |a|
  a += 1
end

puts a

# => puts will print out 7 because the block defines a variable 'a' and shadows the outside variable 'a'
