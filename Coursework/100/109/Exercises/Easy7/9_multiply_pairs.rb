def multiply_all_pairs(arr1, arr2)
  times_order = arr1.size > arr2.size ? [arr1, arr2] : [arr2, arr1]
  products = []
  times_order[1].size.times do |n1|
    times_order[0].size.times do |n2|
      products << times_order[1][n1] * times_order[0][n2]
    end
  end
  products.sort
end

p multiply_all_pairs([2, 4], [4, 3, 1, 2])
