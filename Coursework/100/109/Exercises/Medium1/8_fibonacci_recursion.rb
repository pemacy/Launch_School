def fib(n)
  return 1 if n == 2 || n == 1
  fib(n-1) + fib(n-2)
end

p fib(12)
