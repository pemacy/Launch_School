def show_multiplicative_average(arr)
  (arr.map(&:to_f).reduce(:*)/arr.size).round(3)
end

p show_multiplicative_average([2, 5, 7, 11, 13, 17])
