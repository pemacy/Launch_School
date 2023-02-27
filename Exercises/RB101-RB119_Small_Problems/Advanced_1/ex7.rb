# frozen_string_literal: true

# Write a method that takes two sorted Arrays as arguments, and returns a new
# Array that contains all elements from both arguments in sorted order.

# You may not provide any solution that requires you to sort the result array.
# You must build the result array one element at a time in the proper order.

# Your solution should not mutate the input arrays.

def merge(arr_1, arr_2)
  compares = arr_1.size + arr_2.size
  sorted_arr = []
  compares.times do
    if arr_1.empty? || (arr_2.first && (arr_2.first < arr_1.first))
      sorted_arr << arr_2.shift
    else
      sorted_arr << arr_1.shift
    end
  end
  sorted_arr
end

p merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9]
p merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3]
p merge([], [1, 4, 5]) == [1, 4, 5]
p merge([1, 4, 5], []) == [1, 4, 5]
