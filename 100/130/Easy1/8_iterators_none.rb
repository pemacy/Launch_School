# 8_iterators_none.rb

require 'set'

def none?(item)
  item.each { |*args| return false if yield(*args) }
  true
end

hsh = {a:1, b:2}
p none?(hsh) { |k,v| k == :b && v == 2 }   # => false
p none?(hsh) { |k,v| k == :c  || v == 3}   # => true

arr = [1,2]
p none?(arr) { |el| el > 1 }               # => false
p none?(arr) { |el| el >2 }                # => true

set = Set.new([1,2])
p none?(set) { |s| s >1 }                  # => false
p none?(set) { |s| s > 2 }                 # => true

# Recursive Array form
def none?(arr, &block)
  return true if arr.empty?
  block.call(arr.first) ? false : none?(arr.drop(1), &block)
end
