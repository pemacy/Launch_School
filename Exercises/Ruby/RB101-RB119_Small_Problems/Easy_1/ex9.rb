# frozen_string_literal: true

# Write a method that takes a non-empty string argument, and returns the middle
# character or characters of the argument. If the argument has an odd length,
# you should return exactly one character. If the argument has an even length,
# you should return exactly two characters.

def center_of(str)
  length = str.length
  center = length / 2
  if length.even?
    center_right = center
    center_left = center - 1
    str[center_left .. center_right]
  else
    str[center]
  end
end

puts center_of('I love ruby') == 'e'
puts center_of('Launch School') == ' '
puts center_of('Launch') == 'un'
puts center_of('Launchschool') == 'hs'
puts center_of('x') == 'x'
