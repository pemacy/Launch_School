def select(array)
  true_values = []
  counter = 0

  while counter < array.size
    block_value = yield(array[counter])
    # p block_value
    true_values << array[counter] if block_value
    counter += 1
  end

  true_values
end

array = [1, 2, 3, 4, 5]

p select(array) { |num| num.odd? }      # => [1, 3, 5]
p select(array) { |num| puts num }      # => [], because "puts num" returns nil and evaluates to false
p select(array) { |num| num + 1 }       # => [1, 2, 3, 4, 5], because "num + 1" evaluates to true
