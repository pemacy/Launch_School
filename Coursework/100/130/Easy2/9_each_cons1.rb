# 8_each_cons1.rb

require 'pry'

def each_cons(arr)
  (arr.size - 1).times { |n| yield(arr.first(2)) }
  nil
end

hash = {}
result = each_cons([1, 3, 6, 10]) do |value1, value2|
  hash[value1] = value2
end

p result #== nil
p hash #== { 1 => 3, 3 => 6, 6 => 10 }

hash = {}
each_cons([]) do |value1, value2|
  hash[value1] = value2
end
p hash == {}

hash = {}
each_cons(['a', 'b']) do |value1, value2|
  hash[value1] = value2
end
p hash == {'a' => 'b'}

# Recursive
def con_rec(arr, &block)
  return nil if arr.size <= 1
  yield(arr.first(2))
  con_rec(arr.drop(1), &block)
end

hash = {}
result = con_rec([1, 3, 6, 10]) do |value1, value2|
  hash[value1] = value2
end

p result #== nil
p hash #== { 1 => 3, 3 => 6, 6 => 10 }

hash = {}
con_rec([]) do |value1, value2|
  hash[value1] = value2
end
p hash == {}

hash = {}
con_rec(['a', 'b']) do |value1, value2|
  hash[value1] = value2
end
p hash == {'a' => 'b'}
