def fib(num)
  first, second = 0 , 1
  2.upto(num) do
    first, second = second, first + second
  end
  second
end

def fib_last(num)
  fib_number = fib(num)
  fib_number.to_s[-1].to_i
end

# p fib_last(10000)


# OPTIMIZED SOLUTION
def last_digit_optimized(num)
  last_2 = [1,1]
  3.upto(num) do
    last_2 = [last_2.last, (last_2.first + last_2.last) % 10]
  end
  last_2.last
end

p last_digit_optimized(20000002)
