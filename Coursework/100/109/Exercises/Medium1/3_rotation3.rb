def rotate_array(arr)
  arr = arr[1..-1]+ [arr[0]]
end

p rotate_array([7, 3, 5, 2, 9, 1])

def rotate_right(num, count)
  num_arr = num.to_s.chars.map{|n| n.to_i}
  num_size = num_arr.size
  left_side = num_arr[0, num_size - count]
  rt_side = rotate_array(num_arr[num_size - count,count])
  left_side + rt_side
end

p rotate_right(735291, 5)

def max_rotation(num)
  p num.to_s.size
  (num.to_s.size).downto(1) do |n|
    num = rotate_right(num, n).join.to_i
  end
  num
end

p max_rotation(8_703_529_146)
