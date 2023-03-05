# frozen_string_literal: true

# Write a method that counts the number of occurrences of each element in a
# given array.

def count_occurrences(arr)
  arr.each_with_object(Hash.new(0)) do |el, hsh|
    hsh[el] += 1
  end
end

vehicles = [
  'car', 'car', 'truck', 'car', 'SUV', 'truck',
  'motorcycle', 'motorcycle', 'car', 'truck'
]

puts count_occurrences(vehicles)

# car => 4
# truck => 3
# SUV => 1
# motorcycle => 2
