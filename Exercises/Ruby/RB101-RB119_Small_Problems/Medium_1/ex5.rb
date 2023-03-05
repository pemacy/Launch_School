# frozen_string_literal: true

# Write a method that displays a 4-pointed diamond in an n x n grid, where n is
# an odd integer that is supplied as an argument to the method. You may assume
# that the argument will always be an odd integer.

def diamond(num)
  1.upto(num) do |i|
    puts "#{'*' * i}".center(num, ' ') if i.odd?
  end
  num.downto(1) do |i|
    puts "#{'*' * i}".center(num, ' ') if i.odd? && i < num
  end
end

diamond(1)
diamond(3)
diamond(9)
