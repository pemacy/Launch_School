def transpose(arr)
  m = arr.size
  n = arr[0].size
  new_arr = Array.new(n, [])

  m.times do |i1|
    n.times do |i2|
      new_arr[i2] += [arr[i1][i2]]
    end
  end
  new_arr
end

p transpose([['a','b','c']])
p transpose([[1], [2], [3], [4]])
p transpose([[1, 2, 3, 4, 5], [4, 3, 2, 1, 0], [3, 7, 8, 6, 2]]) ==
  [[1, 4, 3], [2, 3, 7], [3, 2, 8], [4, 1, 6], [5, 0, 2]]
p transpose([[1]]) == [[1]]
