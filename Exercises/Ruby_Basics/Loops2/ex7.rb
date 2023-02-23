# frozen_string_literal: true

# The method below counts from 0 to 4. Modify the block so that it
# prints the current number and stops iterating when the current number
# equals 2.

# original
5.times do |index|
  puts index
  # ...
end

# solution
5.times do |index|
  puts index
  break if index == 2
end
