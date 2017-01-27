def sum(arr)
  sum_subset = []
  counter = 0
  loop do
    sum_subset << arr[0..counter]
    counter += 1
    break if counter == arr.size
  end
  sum_subset << sum_subset.map{|e| e.reduce(:+)}
  sum_subset[-1] = sum_subset.last.reduce(:+)
  sum_subset
end

p sum([3, 5, 2])
