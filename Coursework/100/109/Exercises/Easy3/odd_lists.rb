def oddities(arr)
  arr.select.with_index { | _, index | index.even?}
end

p oddities([2,3,4,5,6])
