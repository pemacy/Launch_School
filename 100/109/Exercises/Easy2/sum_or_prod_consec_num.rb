def sum(num)
  # sum = 0
  # 1.upto(num) { |int| sum += int}
  sum = (1..num).inject {|sum, n| sum + n}
  puts "The sum of the integers between 1 and #{num} is #{sum}"
end

def product(num)
  # product = 1
  # 1.upto(num) { |int| product *= int}
  product = (1..num).reduce(:*)
  puts "The product of the integers between 1 and #{num} is #{product}"
end

puts "Please enter an integer greater than 0"
num = gets.to_i
puts "Enter 's' to compute the sum, 'p' to compute the product."
operator = gets.chomp.downcase

case operator
when 's'
  sum(num)
when 'p'
  product(num)
else
  puts "Oops. Unkown operation"
end

# sum(num) if operator.eql?('s')
# product(num) if operator.eql?('p')
