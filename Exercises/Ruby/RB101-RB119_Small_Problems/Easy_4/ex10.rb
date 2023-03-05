# frozen_string_literal: true

# In the previous exercise, you developed a method that converts non-negative
# numbers to strings. In this exercise, you're going to extend that method by
# adding the ability to represent negative numbers as well.

# Write a method that takes an integer, and converts it to a string
# representation.

# You may not use any of the standard conversion methods available in Ruby, such
# as Integer#to_s, String(), Kernel#format, etc. You may, however, use
# integer_to_string from the previous exercise.

def signed_integer_to_string(num)
  sign = num.positive? ? '+' : '-'
  sign = '' if num.zero?
  str_arr = []
  num = num.abs
  loop do
    last_digit = num % 10
    num /= 10
    str_arr << string_for(last_digit)

    break if num == 0
  end
  str_arr.reverse.unshift(sign).join
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

puts signed_integer_to_string(4321) == '+4321'
puts signed_integer_to_string(-123) == '-123'
puts signed_integer_to_string(0) == '0'
