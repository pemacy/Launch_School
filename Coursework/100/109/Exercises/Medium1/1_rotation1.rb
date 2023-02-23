def rotate_array(arr)
  arr = arr[1..-1]+ [arr[0]]
end

p rotate_array([7, 3, 5, 2, 9, 1])
