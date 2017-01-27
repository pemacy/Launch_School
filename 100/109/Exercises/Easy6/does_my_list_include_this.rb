def include?(arr, value)
  0.upto(arr.size - 1) do |i|
    return true if arr[i] == value
  end
end

p include?([1,2,3,4,5], 9)


# other ways
def include_pther(arr, value)
  !! arr.find_index(value)
  false
end

def include_other2(arr, value)
  arr.each { |el| return true if el == value}
end
