# 6_each_with_index.rb

# Using until loop
def each_with_index(arr)
  counter = 0
  until counter == arr.size
    yield(arr[counter], counter)
    counter += 1
  end
  arr
end

result = each_with_index([1, 3, 6]) do |value, index|
  puts "#{index} -> #{value**index}"
end

puts result == [1, 3, 6]

# Using #each
def each_w_i(arr)
  arr.each {|e| yield(e, arr.index(e))}
end

result = each_w_i([1, 3, 6]) do |value, index|
  puts "#{index} -> #{value**index}"
end

puts result == [1, 3, 6]

# Recursive

def e_w_i(arr, counter = 0, &block)
  counter == arr.size ? (return arr) : block.call(arr[counter], counter)
  e_w_i(arr, counter + 1, &block)
end

result = e_w_i([1, 3, 6]) do |value, index|
  puts "#{index} -> #{value**index}"
end

p result == [1, 3, 6]

# Using #reduce
def each_with_index(arr)
  arr.reduce(0) { |idx, el| yield(el, idx); idx + 1}
  arr
end

result = each_with_index([1, 3, 6]) do |value, index|
  puts "#{index} -> #{value**index}"
end

puts result == [1, 3, 6]
