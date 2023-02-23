# frozen_string_literal: true

def sum_or_prod
  puts 'Please enter an integer greater than 0:'
  i = gets.chomp.to_i
  puts "Enter 's' to compute the sum, 'p' to compute the product:"
  operation = gets.chomp
  compute = case operation
            when 's'
              operation = 'sum'
              (1..i).reduce(&:+)
            when 'p'
              operation = 'product'
              (1..i).reduce(&:*)
            end
  puts "The #{operation} of the integers between 1 and #{i} is #{compute}"
end

sum_or_prod
