# frozen_string_literal: true

# What will the following code print, and why? Don't run the code until you have tried to answer.

a = 7

def my_value(a)
  a += 10
end

my_value(a)
puts a

# => value will be 7, another local variable is created in the my_value method
# the variable 'a' in my_value shadows the variable 'a' outside the method
