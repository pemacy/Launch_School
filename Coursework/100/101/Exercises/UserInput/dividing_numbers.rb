def valid_number?(number_string)
  number_string.to_i.to_s == number_string
end

numerator = nil
denominator = nil

loop do
  puts "Enter numerator"
  numerator = gets.chomp
  break if valid_number?(numerator)
  puts "Invalid input, ony integers are allowed"
end

loop do
  puts "Enter denominator"
  denominator = gets.chomp
  break if valid_number?(denominator) && denominator != '0'
  puts "Invalid input, only non-zero integers are allowed"
end

puts "#{numerator} / #{denominator} = #{numerator.to_i / denominator.to_i}"
