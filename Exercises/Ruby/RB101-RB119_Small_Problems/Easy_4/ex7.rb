# frozen_string_literal: true

# The String#to_i method converts a string of numeric characters (including an
# optional plus or minus sign) to an Integer. String#to_i and the Integer
# constructor (Integer()) behave similarly. In this exercise, you will create a
# method that does the same thing.

# Write a method that takes a String of digits, and returns the appropriate
# number as an integer. You may not use any of the methods mentioned above.

# For now, do not worry about leading + or - signs, nor should you worry about
# invalid characters; assume all characters will be numeric.

# You may not use any of the standard conversion methods available in Ruby to
# convert a string to a number, such as String#to_i, Integer(), etc. Your method
# should do this the old-fashioned way and calculate the result by analyzing the
# characters in the string.

def string_to_integer(str)
  str_arr = []
  str.chars.reverse.each do |c|
    str_arr << case c
               when '0' then 0
               when '1' then 1
               when '2' then 2
               when '3' then 3
               when '4' then 4
               when '5' then 5
               when '6' then 6
               when '7' then 7
               when '8' then 8
               when '9' then 9
               end
  end

  num = 0

  str_arr.each_with_index do |n, i|
    num += n * (10 ** i)
  end
  num
end

puts string_to_integer('4321') == 4321
puts string_to_integer('570') == 570
