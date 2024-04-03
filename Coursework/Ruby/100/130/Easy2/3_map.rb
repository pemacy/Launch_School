# 3_map.rb

def map(arr, &block)
  counter = 0
  result = []
  until counter > arr.size - 1
    result << block.call(arr[counter])
    counter += 1
  end
  result
end

p map([1, 3, 6]) { |value| value**2 } == [1, 9, 36]
p map([1, 3, 4]) { |value| (1..value).to_a } == [[1], [1, 2, 3], [1, 2, 3, 4]]
p map([]) { |value| true } == []

# Recursive
def mapper(arr, &block)
  return [] if arr.empty?
  [block.call(arr.first)] + mapper(arr.drop(1), &block)
end

p mapper({a:1, b:2}) { |k, v| [k,v] }
p mapper([]) { |value| true } == []
