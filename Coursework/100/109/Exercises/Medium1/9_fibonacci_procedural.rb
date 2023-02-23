def fib(num)
  a = 0
  b = 1
  counter = 1
  sto = 0

  loop do
    sto = a
    a = b
    b = sto + a
    counter += 1
    break unless counter < num
  end

  b
end

p fib(100001)


# MORE CONCISE SOLUTION

def fib(num)
  first, second = 0 , 1
  2.upto(num) do
    first, second = second, first + second
  end
  second
end

p fib(20)
