# frozen_string_literal: true

# Consider the following method and a call to that method:

def my_method(a, b = 2, c = 3, d)
  p [a, b, c, d]
end

my_method(4, 5, 6)

# it will print out [4, 5, 3, 6], because Ruby will fill missing arguments in-order
