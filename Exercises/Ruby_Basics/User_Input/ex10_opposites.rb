# frozen_string_literal: true

# Write a program that requests two integers from the user, adds them
# together, and then displays the result. Furthermore, insist that one
# of the integers be positive, and one negative; however, the order in
# which the two integers are entered does not matter.

# Do not check for the positive/negative requirement until both integers
# are entered, and start over if the requirement is not met.

# You may use the following method to validate input integers:

def valid_number?(number_string)
  number_string.to_i.to_s == number_string && number_string.to_i != 0
end

num_1 = nil
num_2 = nil

loop do
  puts 'Enter a positive or negative number:'
  num_1 = gets.chomp
  puts 'Enter another positive or negative number:'
  num_2 = gets.chomp
  num_product = num_1.to_i * num_2.to_i
  valid_numbers = valid_number(num_1) && valid_number(num_2)
  break if valid_numbers && num_product.negative?

  puts 'Invalid input, only non-zero integers are allowed'
end

result = num_1.to_i + num_2.to_i
puts "#{num_1} + #{num_2} = #{result}"
