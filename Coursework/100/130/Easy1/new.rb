# 10_count_items.rb

require 'set'

def count(item)
  item.select { |*args| yield(*args) }.size
end

hsh = {a:2, b:2}
p count(hsh) { |k,v| v.even? } == 2             # => false
p count(hsh) { |k,v| k == :b } == 1            # => true

arr = [1,2]
p count(arr) { |el| el > 0 } == 2               # => false
p count(arr) { |el| el > 1 } == 1               # => true

set = Set.new([1,2])
p count(set) { |s| s > 0 } == 2                 # => false
p count(set) { |s| s > 1 } == 1                 # => true
