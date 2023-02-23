def find_fib_len(length)
  fib = [1,1]

  loop do
    fib << fib[-1] + fib[-2]
    break if fib[-1].to_s.size >= length
  end

  fib.size
end

puts find_fib_len(1000)
