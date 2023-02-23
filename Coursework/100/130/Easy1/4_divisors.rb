def divisors(num)
  div = []
  1.upto(num ** 0.5) do |n|
    div << [n, num / n] if (num % n).zero?
  end
  div.flatten.uniq.sort
end

p divisors(1) == [1]
p divisors(7) == [1, 7]
p divisors(12) == [1, 2, 3, 4, 6, 12]
p divisors(98) #== [1, 2, 7, 14, 49, 98]
p divisors(999962000357)
