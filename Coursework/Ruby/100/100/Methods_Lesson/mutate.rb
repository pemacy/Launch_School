# Example of a method that modifies its argument permanently
# mutate.rd
a=[1,2,3]
def mutate(array)
  array.pop
end

def no_mutate(array)
  array.last
end

puts "Before mutate method: #{a}"
mutate(a)
puts "After mutate method #{a}"
no_mutate(a)
puts "After no mutate method #{a}"
