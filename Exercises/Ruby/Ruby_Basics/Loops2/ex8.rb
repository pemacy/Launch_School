# frozen_string_literal: true

# Using next, modify the code below so that it only prints
# positive integers that are even.

# original
number = 0

until number == 10
  number += 1
  puts number
end

# solution
number = 0

until number == 10
  number += 1
  next if number.odd?

  puts number
end
