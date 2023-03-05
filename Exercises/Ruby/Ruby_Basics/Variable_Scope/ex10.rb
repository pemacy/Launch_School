# frozen_string_literal: true

# What will the following code print, and why? Don't run the code until you have tried to answer.

a = 7
array = [1, 2, 3]

def my_value(ary)
  ary.each do |b|
    a += b
  end
end

my_value(array)
puts a

# => undefined method '+' for nil class
#     'a' is undefined in the method, the 'a' variable outside the method
#     is not visible inside the method, so it's value is nil and can't
#     use the moethod '+'
