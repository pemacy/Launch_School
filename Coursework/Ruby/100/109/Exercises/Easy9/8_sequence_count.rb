def seq(count, num)
  count_arr = []
  count.times do |n|
    count_arr << num + num * n
  end
  count_arr
end

p seq(0, 1000)
