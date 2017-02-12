def rotate_array(arr)
  arr = arr[1..-1]+ [arr[0]]
end

p rotate_array([7, 3, 5, 2, 9, 1])

def rotate_right(num, n)
  num = num.to_s.chars
  num[-n..-1] = rotate_array(num[-n..-1])
  num.join.to_i
end

p rotate_right(735291, 4)
