# frozen_string_literal: true

# What will the following code print? Why? Don't run it until you've attempted to answer.

def count_sheep
  5.times do |sheep|
    puts sheep
  end
end

puts count_sheep

# the code will print 0-4 inside the times block, and 5 because of the return
# value of the times block
