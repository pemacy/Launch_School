# frozen_string_literal: true

# What will the following code print, and why? Don't run the code until you have tried to answer.

a = 7

def my_value(b)
  b = a + a
end

my_value(a)
puts a

# => the program will thruw an error because 'a' is not defined within the scope of the method - methods have no notion of inner/outer scope with respect to local variables
