PASSWORD = 'yup'

loop do
  puts "Enter your password:"
  input = gets.chomp
  break if input.eql?(PASSWORD)
  puts "Invalide password!"
end

puts "Welcome!"
