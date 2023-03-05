# frozen_string_literal: true

# Write a program that will ask for user's name. The program will then greet the
# user. If the user writes "name!" then the computer yells back to the user.

def greeting
  puts 'What is you name?'
  name = gets.chomp
  if name[-1] == '!'
    puts "HELLO #{name.upcase}. WHY ARE WE SCREAMING?"
  else
    puts "Hello #{name}"
  end
end

greeting
