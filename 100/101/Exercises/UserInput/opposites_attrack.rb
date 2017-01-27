def valid_number?(number_string)
  number_string.to_i.to_s == number_string && number_string.to_i != 0
end

def read_input
  loop do
    puts "Please enter a positive or negative integer"
    num = gets.chomp
    return num.to_i if valid_number?(num)
    puts "Invalid input. Only non-zero integers are allowed."
  end
end

num1 = nil
num2 = nil

loop do
  num1 = read_input
  num2 = read_input
  break if num1 * num2 < 0
  puts "Sorry. One integer must be positive, one must be negative."
  puts "Please start over."
end

puts "#{num1} + #{num2} = #{num1 + num2}"
