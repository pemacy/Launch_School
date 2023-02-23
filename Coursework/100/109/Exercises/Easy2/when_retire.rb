print "What is your age?  "
age = gets.chomp
print "At what age would you like to retire?  "
retire_age = gets.chomp

years_until_retirement = retire_age.to_i - age.to_i
current_year = Time.new.year

puts "It's #{current_year}.  You will retire in #{current_year + years_until_retirement}"
puts "You have only #{years_until_retirement} to go!"
