# frozen_string_literal: true

# Write a method that displays an 8-pointed star in an nxn grid, where n is an
# odd integer that is supplied as an argument to the method. The smallest such
# star you need to handle is a 7x7 grid.

def star(num)
  arr = []
  1.upto(num - 1) do |n|
    next if n.even?

    adjust = (n + 1) / 2
    arr << ('*'.ljust(adjust) + '*' + '*'.rjust(adjust)).center(num)
  end
  puts arr.reverse
  puts '*' * num
  puts arr
end

star(7)
star(9)
