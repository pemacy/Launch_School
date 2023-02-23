# fibonacci.rb

=begin

a = 0
b = 1

def fibonacci(number)
  for i in 1..number
    f = a + b
    a = b
    b = f
  end
  puts f
end

print 'How many fibonacci sequences would you like to iterate?'
num = gets.chomp.to_i

=end

# recursive solution
def fibonacci(number)
  if number < 2
    number
  else
    fibonacci(number - 1) + fibonacci(number - 2)
  end
end

puts fibonacci(6)
