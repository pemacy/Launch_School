# frozen_string_literal: true

# What will the following code print, and why? Don't run the code until you have tried to answer.

a = "Xyzzy"

def my_value(b)
  b = 'yzzyX'
end

my_value(a)
puts a

# => 'a' will still be it's original value. the method creates a local variable scoped inside the method that equals a value, and that dows not affect the value of 'a'
