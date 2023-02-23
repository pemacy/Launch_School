# frozen_string_literal: true

# In the previous exercise, you developed a method that converts simple numeric
# strings to Integers. In this exercise, you're going to extend that method to
# work with signed numbers.

# Write a method that takes a String of digits, and returns the appropriate
# number as an integer. The String may have a leading + or - sign; if the first
# character is a +, your method should return a positive number; if it is a -,
# your method should return a negative number. If no sign is given, you should
# return a positive number.

# You may assume the string will always contain a valid number.

# You may not use any of the standard conversion methods available in Ruby, such
# as String#to_i, Integer(), etc. You may, however, use the string_to_integer
# method from the previous lesson.

def string_to_signed_integer(str)
  signed = str =~ /^[+|-]/
  end_multiplier = 1
  if signed
    end_multiplier = -1 if str.match(/^-/)
    str = str[1..-1]
  end
  string_to_integer(str) * end_multiplier
end

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

puts string_to_signed_integer('4321') == 4321
puts string_to_signed_integer('-570') == -570
puts string_to_signed_integer('+100') == 100
