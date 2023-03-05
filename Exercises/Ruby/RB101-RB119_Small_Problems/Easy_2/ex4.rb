# frozen_string_literal: true

def retire
  puts 'Whast is your age?'
  age = gets.chomp.to_i
  puts 'At what age would you like to retire?'
  retire_age = gets.chomp.to_i
  year = Time.now.year
  puts "It's #{year}. Your will retire in #{year + retire_age - age}"
  puts "You only have #{retire_age - age} years of work to go!"
end

retire
