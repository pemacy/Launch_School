def interleave(arr1, arr2)
  arr = (0..arr1.size-1).each_with_object([]) do |i,arr|
    arr << arr1[i]
    arr << arr2[i]
  end
  arr
end

p interleave([1,2,3],['a','b','c'])

def interleave_zip(arr1, arr2)
  arr1.zip(arr2).flatten
end

p interleave_zip([1,2,3],['a','b','c'])
