# 2.zipper.rb

def zip(arr1, arr2)
  arr1.map { |e| [e,arr2[arr1.index(e)]] }
  # OR
  # arr1.map.with_index { |e,i| [e,arr2[i]] }
end

p zip([1,2,3],[4,5,6])

# Recursive
def zipper(arr1, arr2)
  return [] if arr1.empty?
  [[arr1.first, arr2.first]] + zipper(arr1.drop(1), arr2.drop(1))
end


p zipper([1,2,3],[:a,:b,:c])
