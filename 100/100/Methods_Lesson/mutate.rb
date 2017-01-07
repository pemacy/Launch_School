# Example of a method that modifies its argument permanently
# mutate.rd
a=[1,2,3]
def mutate(array)
  array.pop
end

def no_mutate(array)
  array.last
end

p "Before mutate method: #{a}"
p mutate(a)
p "After mutate method #{a}"
p no_mutate(a)
p "After no mutate method #{a}"
