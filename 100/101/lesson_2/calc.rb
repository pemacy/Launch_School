# calc.rb

Kernel.puts("Enter 2 numbers")
Kernel.puts("Number 1:")
a = Kernel.gets().chomp().to_i
Kernel.puts("Number 2:")
b = Kernel.gets().chomp().to_i
Kernel.puts("Enter operator to use (add, substract, multiply, divide)")
c = Kernel.gets().chomp()

case c
when "add"
  result = a + b
when "subtract"
  result = a - b
when "multiply"
  result = a * b
when "divide"
  result = a / b
end

Kernel.puts("Result is: #{result}")
