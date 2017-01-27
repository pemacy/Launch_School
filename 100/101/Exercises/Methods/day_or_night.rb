def time_of_day(bool)
  puts "It's daytime!" if bool
  puts "It's nighttime!" unless bool
end

daylight = [true, false].sample
time_of_day(daylight)
