# frozen_string_literal: true

# In the previous exercise, we developed a procedural method for computing the
# value of the nth Fibonacci numbers. This method was really fast, computing the
# 20899 digit 100,001st Fibonacci sequence almost instantly.

# In this exercise, you are going to compute a method that returns the last
# digit of the nth Fibonacci number.

def fibonacci(n)
  result = []
  i = 1
  while i <= n
    if i == 1 || i == 2
      result << 1
    else
      result << result[i - 3] + result[i - 2]
    end
    i += 1
  end
  result.last
end

def fibonacci_last(n)
  result = fibonacci(n)
  result.to_s.chars.last.to_i
end

p fibonacci_last(15)        # -> 0  (the 15th Fibonacci number is 610)
p fibonacci_last(20)        # -> 5 (the 20th Fibonacci number is 6765)
p fibonacci_last(100)       # -> 5 (the 100th Fibonacci number is 354224848179261915075)
p fibonacci_last(100_001)   # -> 1 (this is a 20899 digit number)
p fibonacci_last(1_000_007) # -> 3 (this is a 208989 digit number)
p fibonacci_last(123456789) # -> 4
