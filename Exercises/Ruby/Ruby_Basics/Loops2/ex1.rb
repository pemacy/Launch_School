# frozen_string_literal: true

# Write a loop that prints numbers 1-5 and whether the number is even or odd.
# Use the code below to get started

# original code
count = 1

loop do
  count += 1
end

# solution
count = 1

loop do
  category = case count.even?
             when true then 'even'
             when false then 'odd'
             end
  puts "#{count} is #{category}"
  count += 1
  break if count > 5
end
