# 8_each_cons1.rb

require 'pry'

puts "==========================================="


def each_cons(arr, num)
  (arr.size - (num - 1)).times do |n|
     yield(*arr[n..-1].first(num))
  end
  nil
end

hash = {}
each_cons([1, 3, 6, 10], 1) do |value|
  hash[value] = true
end
p hash #== { 1 => true, 3 => true, 6 => true, 10 => true }

hash = {}
each_cons([1, 3, 6, 10], 2) do |value1, value2|
  hash[value1] = value2
end
p hash #== { 1 => 3, 3 => 6, 6 => 10 }

hash = {}
each_cons([1, 3, 6, 10], 3) do |value1, *values|
  hash[value1] = values
end
p hash #== { 1 => [3, 6], 3 => [6, 10] }

hash = {}
each_cons([1, 3, 6, 10], 4) do |value1, *values|
  hash[value1] = values
end
p hash #== { 1 => [3, 6, 10] }

hash = {}
each_cons([1, 3, 6, 10], 5) do |value1, *values|
  hash[value1] = values
end
p hash #== {}


puts "==========================================="
# ================================================

# Recursive
def con_rec(arr, num, &block)
  return nil if arr.size < num
  block.call(*arr.first(num))
  con_rec(arr.drop(1), num, &block)
end

hash = {}
result = con_rec([1, 3, 6, 10], 1) do |value1, value2|
  hash[value1] = true
end

p result #== nil
p hash #== { 1 => 3, 3 => 6, 6 => 10 }

hash = {}
con_rec([1, 3, 6, 10], 2) do |value1, value2|
  hash[value1] = value2
end
p hash #== { 1 => 3, 3 => 6, 6 => 10 }

hash = {}
con_rec([1, 3, 6, 10], 3) do |value1, *values|
  hash[value1] = values
end
p hash #== { 1 => [3, 6], 3 => [6, 10] }

hash = {}
con_rec([1, 3, 6, 10], 4) do |value1, *values|
  hash[value1] = values
end
p hash #== { 1 => [3, 6, 10] }

hash = {}
con_rec([1, 3, 6, 10], 5) do |value1, *values|
  hash[value1] = values
end
p hash #== {}


# ================================================
