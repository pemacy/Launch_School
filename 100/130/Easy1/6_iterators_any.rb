# 6_iterators_any.rb
require 'set'
def any?(collection)
  collection.each { |*args| return true if yield(*args) }
  false
end

hsh = {a:1, b:2}
any?(hsh) { |k,v| k == :b && v == 2 }   # => true
any?(hsh) { |k,v| k == :c  || v == 3}   # => false

arr = [1,2]
any?(arr) { |el| el > 1 }               # => true
any?(arr) { |el| el >2 }                # => false

set = Set.new([1,2])
any?(set) { |s| s >1 }                  # => true
any?(set) { |s| s > 2 }                 # => false

# recursive for Array form:
def any1?(arr, &block)
  return false if arr.empty?
  block.call(arr.first) ? true : any?(arr.drop(1), &block)
end

p any1?(hsh) { |k,v| k == :b && v == 2 }   # => true
p any1?(hsh) { |k,v| k == :c  || v == 3}   # => false
