def rev!(arr)
  rev_index = []
  temp_arr = arr.dup
  (arr.size - 1).downto(0) { |i| rev_index << i }
  arr.map!.with_index { |el,i| el = temp_arr[rev_index[i]]}
end

list = [1,2,3,4]
result = rev!(list)
p list.object_id
p result.object_id
p result
