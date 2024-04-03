# 7_iterators_all.rb

require 'set'

def all?(item)
  item.each { |*args| return false unless yield(*args) }
  true
end

hsh = {a:2, b:2}
p all?(hsh) { |k,v| v == 2 && k != :c }   # => true
p all?(hsh) { |k,v| k == :b }             # => false

arr = [1,2]
p all?(arr) { |el| el > 0 }                # => true
p all?(arr) { |el| el > 1 }                # => false

set = Set.new([1,2])
p all?(set) { |s| s > 0 }                  # => true
p all?(set) { |s| s > 1 }                  # => false


# recursive:
def all?(arr, &block)
  return true if arr.empty?
  block.call(arr.first) ? all?(arr.drop(1), &block) : false
end
