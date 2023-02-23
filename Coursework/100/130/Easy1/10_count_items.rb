# 10_count_items.rb

require 'set'

def count(item, counter = 0)
  item.each { |*args| counter += 1 if yield(*args) }
  counter
end

hsh = {a:2, b:2}
p count(hsh) { |k,v| v.even? } == 2             # => false
p count(hsh) { |k,v| k == :b } == 1             # => true

arr = [1,2]
p count(arr) { |el| el > 0 } == 2               # => false
p count(arr) { |el| el > 1 } == 1               # => true

set = Set.new([1,2])
p count(set) { |s| s > 0 } == 2                 # => false
p count(set) { |s| s > 1 } == 1                 # => true


# Further Exploration
def count(item)
  item.select { |*args| yield(*args) }.size
end

# Recursion for Array argument
def count(arr, &block)
  return 0 if arr.empty?
  count(arr.drop(1), &block) + (block.call(arr.first) ? 1 : 0)
end
