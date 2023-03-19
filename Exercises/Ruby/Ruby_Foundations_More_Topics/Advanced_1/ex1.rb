# frozen_string_literal: true

fac_100 = Enumerator.new do |y|
  val = 1
  count = 0

  while true
  # while count < 100
    count += 1
    y << val
    val *= count
  end
end

p fac_100.first(7)
# p fac_100.count { |val| val < 1000 }

0.upto(7) do |n|
  puts "Factorial of #{n} is #{fac_100.next}"
end
