# frozen_string_literal: true

# Modify the code below so "Hello!" is printed 5 times.

say_hello = true

while say_hello
  puts 'Hello!'
  say_hello = false
end

# => Answer

say_hello = true
count = 1

while say_hello
  puts 'Hello!'
  say_hello = false if count >= 5
  count += 1
end
