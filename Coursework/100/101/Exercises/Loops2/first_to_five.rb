number_a = 0
number_b = 0

loop do
  number_a += rand(2)
  number_b += rand(2)
  next unless number_b == 5 || number_a == 5
  puts "5 was reached! #{number_a}, #{number_b}"
  break
end
