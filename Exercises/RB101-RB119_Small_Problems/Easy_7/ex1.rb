# frozen_string_literal: true

# Write a method that combines two Arrays passed in as arguments, and returns a
# new Array that contains all elements from both Array arguments, with the
# elements taken in alternation.

# You may assume that both input Arrays are non-empty, and that they have the
# same number of elements.

def interleave(arr_1, arr_2)
  count = arr_1.size
  combined_arr = []
  count.times do |i|
    combined_arr << arr_1[i]
    combined_arr << arr_2[i]
  end
  combined_arr
end

puts interleave([1, 2, 3], ['a', 'b', 'c']) == [1, 'a', 2, 'b', 3, 'c']
