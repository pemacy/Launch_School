# frozen_string_literal: true

# In the previous two exercises, you developed methods that convert simple
# numeric strings to signed Integers. In this exercise and the next, you're
# going to reverse those methods.

# Write a method that takes a positive integer or zero, and converts it to a
# string representation.

# You may not use any of the standard conversion methods available in Ruby,
# such as Integer#to_s, String(), Kernel#format, etc. Your method should do this
# the old-fashioned way and construct the string by analyzing and manipulating
# the number.

def integer_to_string(num)
  str_arr = []
  loop do
    last_digit = num % 10
    num /= 10
    str_arr << string_for(last_digit)

    break if num == 0
  end
  str_arr.reverse.join
end

def string_for(digit)
  case digit
  when 0 then '0'
  when 1 then '1'
  when 2 then '2'
  when 3 then '3'
  when 4 then '4'
  when 5 then '5'
  when 6 then '6'
  when 7 then '7'
  when 8 then '8'
  when 9 then '9'
  end
end

puts integer_to_string(4321) == '4321'
puts integer_to_string(0) == '0'
puts integer_to_string(5000) == '5000'
