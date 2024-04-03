def merge(arr1, arr2)
  arr1 += arr2
  delete_arr = []
  arr1.each_with_index do | el, i |
      (i+1).upto(arr1.size - 1) do | i2 |
        delete_arr << i2 if el == arr1[i2]
    end
  end

  delete_arr.each { |el| arr1.delete_at(el) }
  arr1
end

p merge([1, 3, 5], [3, 6, 9])

def merge(array_1, array_2)
  array_1 | array_2
end
