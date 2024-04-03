def multiply(first_num, second_num)
  first_num.send(:*, second_num)
end

def square(n)
  multiply(n, n)
end

def power_to_the_n(num1, n)
  square = square(num1)
  exp = square
  (n - 2).times { exp = num1 * square }
  exp
end

puts power_to(-8,3)
