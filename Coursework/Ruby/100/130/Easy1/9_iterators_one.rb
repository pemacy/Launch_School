# 9_iterators_one.rb

require 'set'

def one?(item, count = 0)
  item.each { |*args| count += 1 if yield(*args) }
  count == 1 ? true : false
end

hsh = {a:2, b:2}
p one?(hsh) { |k,v| v == 2 }              # => false
p one?(hsh) { |k,v| k == :b }             # => true

arr = [1,2]
p one?(arr) { |el| el > 0 }                # => false
p one?(arr) { |el| el > 1 }                # => true

set = Set.new([1,2])
p one?(set) { |s| s > 0 }                  # => false
p one?(set) { |s| s > 1 }                  # => true

# Recursive Array Form
def one?(arr, counter = 0, &block)
  return counter == 1 if arr.empty? || counter > 1
  counter += 1 if block.call(arr.first)
  one?(arr.drop(1), counter, &block)
end
