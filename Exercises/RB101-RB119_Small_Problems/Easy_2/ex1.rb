# frozen_string_literal: true

# Build a program that randomly generates and prints Teddy's age. To get the
# age, you should generate a random number between 20 and 200.

def teddy_age
  age = (20..200).to_a.sample
  puts "Teddy's age is #{age} years old!"
end

teddy_age
