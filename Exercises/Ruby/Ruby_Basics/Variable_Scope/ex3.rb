# frozen_string_literal: true

# What will the following code print, and why? Don't run the code until you have tried to answer.

a = 7

def my_value(b)
  a = b
end

my_value(a + 5)
puts a

# => puts a will print out 7, because you have creatged a new variable 'a'
# within the my_value method, which shadows the variable outside the method
