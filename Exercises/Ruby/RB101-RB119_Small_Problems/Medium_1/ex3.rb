# frozen_string_literal: true

# If you take a number like 735291, and rotate it to the left, you get 352917.
# If you now keep the first digit fixed in place, and rotate the remaining
# digits, you get 329175. Keep the first 2 digits fixed in place and rotate
# again to 321759. Keep the first 3 digits fixed in place and rotate again to
# get 321597. Finally, keep the first 4 digits fixed in place and rotate the
# final 2 digits to get 321579. The resulting number is called the maximum
# rotation of the original number.

# Write a method that takes an integer as argument, and returns the maximum
# rotation of that argument. You can (and probably should) use the
# rotate_rightmost_digits method from the previous exercise.

# Note that you do not have to handle multiple 0s.

def rotate_array(arr)
  new_arr = arr.dup
  new_arr.push(new_arr.shift)
end

def rotate_rightmost_digits(num, digits)
  rotated = num.to_s.chars[0...-digits] + rotate_array(num.to_s.chars[-digits..-1])
  rotated.join.to_i
end

def max_rotation(num)
  num_chars = num.to_s.chars
  num_digits = num_chars.size
  temp_array = num_chars
  rotated_array = []

  num_digits.times do |i|
    num_section = temp_array.join.to_i
    right_digits = num_digits - i
    temp_size_before = temp_array.size

    temp_array = rotate_rightmost_digits(num_section, right_digits)
      .to_s.chars
    temp_size_after = temp_array.size

    temp_array.unshift('0') if temp_size_after < temp_size_before # accounting for leading 0

    rotated_array << temp_array[i]
  end

  rotated_array.join.to_i
end

p max_rotation(735291) == 321579
p max_rotation(3) == 3
p max_rotation(35) == 53
p max_rotation(105) == 15 # the leading zero gets dropped
p max_rotation(8_703_529_146) == 7_321_609_845
