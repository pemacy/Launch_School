# frozen_string_literal: true

# When the user inputs 10, we expect the program to print The result is 50!,
# but that's not the output we see. Why not?

def multiply_by_five(n)
  n * 5
end

puts "Hello! Which number would you like to multiply by 5?"
number = gets.chomp

puts "The result is #{multiply_by_five(number)}!"

# => gets.chomp returns a string, but the method multiply_by_five needs an
# integer.  To solve this problem you need to convert it to an integer first
# with gets.chomp.to_i
