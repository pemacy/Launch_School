# frozen_string_literal: true

# Write a method that can rotate the last n digits of a number. For example:

def rotate_array(arr)
  new_arr = arr.dup
  new_arr.push(new_arr.shift)
end

def rotate_rightmost_digits(num, digits)
  rotated = num.to_s.chars[0...-digits] + rotate_array(num.to_s.chars[-digits..-1])
  rotated.join.to_i
end

p rotate_rightmost_digits(735291, 1) == 735291
p rotate_rightmost_digits(735291, 2) == 735219
p rotate_rightmost_digits(735291, 3) == 735912
p rotate_rightmost_digits(735291, 4) == 732915
p rotate_rightmost_digits(735291, 5) == 752913
p rotate_rightmost_digits(735291, 6) == 352917
