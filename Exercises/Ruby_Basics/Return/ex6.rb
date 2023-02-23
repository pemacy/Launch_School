# frozen_string_literal: true

# What will the following code print? Why? Don't run it until you've attempted to answer.

def meal
  return 'Breakfast'
  'Dinner'
  puts 'Dinner'
end

puts meal

# it will print 'Breakfast', the method will exit b/c of the return line before
# it reaches the puts 'Dinner' command
