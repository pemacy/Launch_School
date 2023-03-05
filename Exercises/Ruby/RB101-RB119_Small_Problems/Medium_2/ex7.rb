# frozen_string_literal: true

require 'date'

# Write a method that returns the number of Friday the 13ths in the year given
# by an argument. You may assume that the year is greater than 1752 (when the
# United Kingdom adopted the modern Gregorian Calendar) and that it will remain
# in use for the foreseeable future.

def friday_13th(year)
  d = Date.new(year)
  count = 0
  365.times do
    count += 1 if d.friday? && d.day == 13
    d = d.next_day
  end
  count
end

p friday_13th(2015) == 3
p friday_13th(1986) == 1
p friday_13th(2019) == 2
