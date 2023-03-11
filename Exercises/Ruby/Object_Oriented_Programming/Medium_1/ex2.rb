# frozen_string_literal: true

# A fixed-length array is an array that always has a fixed number of elements.
# Write a class that implements a fixed-length array, and provides the
# necessary methods to support the following code:

# The below code should output true 16 times.
class FixedArray
  def initialize(arr_num)
    @arr_num = arr_num
    @arr = [nil] * arr_num
  end

  def [](index)
    raise IndexError if index > @arr_num

    @arr[index]
  end

  def []=(index, element)
    raise IndexError if index > @arr_num

    @arr[index] = element
  end

  def to_a
    @arr
  end

  def to_s
    @arr.to_s
  end
end

fixed_array = FixedArray.new(5)
puts fixed_array[3] == nil
puts fixed_array.to_a == [nil] * 5

fixed_array[3] = 'a'
puts fixed_array[3] == 'a'
puts fixed_array.to_a == [nil, nil, nil, 'a', nil]

fixed_array[1] = 'b'
puts fixed_array[1] == 'b'
puts fixed_array.to_a == [nil, 'b', nil, 'a', nil]

fixed_array[1] = 'c'
puts fixed_array[1] == 'c'
puts fixed_array.to_a == [nil, 'c', nil, 'a', nil]

fixed_array[4] = 'd'
puts fixed_array[4] == 'd'
puts fixed_array.to_a == [nil, 'c', nil, 'a', 'd']
puts fixed_array.to_s == '[nil, "c", nil, "a", "d"]'

puts fixed_array[-1] == 'd'
puts fixed_array[-4] == 'c'

begin
  fixed_array[6]
  puts false
rescue IndexError
  puts true
end

begin
  fixed_array[-7] = 3
  puts false
rescue IndexError
  puts true
end

begin
  fixed_array[7] = 3
  puts false
rescue IndexError
  puts true
end
