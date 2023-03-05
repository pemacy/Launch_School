# frozen_string_literal: true

# Write a method that takes two Arrays as arguments, and returns an Array that
# contains all of the values from the argument Arrays. There should be no
# duplication of values in the returned Array, even if there are duplicates in
# the original Arrays.

def merge(arr_1, arr_2)
  temp = arr_1.dup
  for el in arr_2
    temp << el unless temp.include? el
  end
  temp
end

puts merge([1, 3, 5], [3, 6, 9]) == [1, 3, 5, 6, 9]
