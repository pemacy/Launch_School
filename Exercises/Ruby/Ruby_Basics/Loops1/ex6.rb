 # frozen_string_literal: true

# Using a while loop, print 5 random numbers between 0 and 99 (inclusive). The code below shows an example of how to begin solving this exercise.

numbers = []
count = 0
rand = Random.new

while count < 5
  numbers << rand.rand(100)
  count += 1
end

puts numbers
