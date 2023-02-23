# frozen_string_literal: true

# What errors does the following code raise and what do they mean:

def find_first_nonzero_among(numbers)
  numbers.each do |n|
    return n if n.nonzero?
  end
end

# Examples

find_first_nonzero_among(0, 0, 1, 0, 2, 0)
find_first_nonzero_among(1)


#
# => the first error will be that too many arguments are passed, it's only expecting 1
# => the second error will be a method call error, no method 'each' exists for Interger class
