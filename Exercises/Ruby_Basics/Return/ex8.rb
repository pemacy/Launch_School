# frozen_string_literal: true

# What will the following code print? Why? Don't run it until you've attempted to answer.

def count_sheep
  5.times do |sheep|
    puts sheep
  end
  10
end

puts count_sheep

# it will print 0-4, then it will print 10 b/c that's the return value of the methodd
