# frozen_string_literal: true

# The time of day can be represented as the number of minutes before or after
# midnight. If the number of minutes is positive, the time is after midnight.
# If the number of minutes is negative, the time is before midnight.

# Write a method that takes a time using this minute-based format and returns
# the time of day in 24 hour format (hh:mm). Your method should work with any
# integer input.

# You may not use ruby's Date and Time classes.

MINUTES_PER_DAY = 1440
MINUTES_PER_HOUR = 60

def time_of_day(min)
  return '00:00' if min.zero?

  countdown = true unless min.positive?
  _days, min = min.abs.divmod(MINUTES_PER_DAY)

  min = MINUTES_PER_DAY - min if countdown

  hours, min = min.divmod(MINUTES_PER_HOUR)
  hours = hours.to_s.rjust(2, '0')
  min = min.to_s.rjust(2, '0')
  "#{hours}:#{min}"
end

puts time_of_day(0) == '00:00'
puts time_of_day(-3) == '23:57'
puts time_of_day(35) == '00:35'
puts time_of_day(-1437) == '00:03'
puts time_of_day(3000) == '02:00'
puts time_of_day(800) == '13:20'
puts time_of_day(-4231) == '01:29'
