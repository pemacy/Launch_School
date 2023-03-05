# frozen_string_literal: true

# Run the code as it is shown below, and take notice of any error messages.

def dog(name)
  return name
end

def cat(name)
  return name
end

puts "The dog's name is #{dog('Spot')}."
puts "The cat's name is #{cat('Ginger')}."

# original methods produced the errors:
# in 'dog' wrong number of arguments (given 1, expected 0) (ArgumentError)
# in 'cat' wrong number of arguments (given 0, expecte1) (ArgumentError)
