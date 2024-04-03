# 7_each_with_object.rb

def each_with_object(arr, obj)
  arr.each { |e| yield(e, obj) } && obj
end

result = each_with_object([1, 3, 5], []) do |value, list|
  list << value**2
end
p result #== [1, 9, 25]

result = each_with_object([1, 3, 5], {}) do |value, hash|
  hash[value] = value**2
end
p result #== { 1 => 1, 3 => 9, 5 => 25 }


# Recursive

def ech(arr, obj, &block)
  arr.empty? ? (return obj) : block.call(arr.first, obj)
  ech(arr.drop(1), obj, &block)
end

result = ech([1, 3, 5], []) do |value, list|
  list << value**2
end
p result #== [1, 9, 25]

result = ech([1, 3, 5], {}) do |value, hash|
  hash[value] = value**2
end
p result #== { 1 => 1, 3 => 9, 5 => 25 }
