def buy_fruit(arr)
  fruit_arr = []
  arr.each do |fruit|
    fruit[1].times {fruit_arr << fruit[0]}
  end
  fruit_arr
end

p buy_fruit([["apples", 3], ["orange", 1], ["bananas", 2]])


# LAUNCH SCHOOL SOLUTION
def buy_fruit(list)
  list.map { |fruit, quantity| [fruit] * quantity }.flatten
end
