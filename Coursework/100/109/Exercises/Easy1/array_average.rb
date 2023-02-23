def average(arr = [0])
  ave = 0
  arr.each { |n| ave += n.to_f }

  ave / arr.size
end

puts average([1, 5, 87, 45, 8, 8]).round(2)
puts average([9, 47, 23, 95, 16, 52]).round(2)
