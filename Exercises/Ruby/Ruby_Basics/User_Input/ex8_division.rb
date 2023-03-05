# frozen_string_literal: true

# Write a program that asks the user to enter two integers,
# then prints the results of dividing the first by the second.
# The second number must not be 0. Since this is user input,
# there's a good chance that the user won't enter a valid integer.
# Therefore, you must validate the input to be sure it is an integer.
# You can use the following code to determine whether the input is an integer:

def valid_number?(number_string)
  number_string.to_i.to_s == number_string
end

num_1 = nil
num_2 = nil
result = nil
puts 'Enter two numbers to divide.'

loop do
  puts 'Enter numerator:'
  num_1 = gets.chomp
  puts 'Enter denominator:'
  num_2 = gets.chomp

  valid_inputs = valid_number?(num_1) && valid_number?(num_2)

  num_1 = num_1.to_i
  num_2 = num_2.to_i
  no_zeroes = num_1.positive? && num_2.positive?

  if valid_inputs && no_zeroes
    result = num_1 / num_2
    break
  else
    puts 'Input invalid, only intergers allowed.'
  end
end

puts "#{num_1} / #{num_2} = #{result}"
