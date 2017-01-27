require 'date'

MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
MINUTES_PER_DAY = MINUTES_PER_HOUR * HOURS_PER_DAY

def time_of_day(num)
  minutes = num % MINUTES_PER_DAY
  hours, minutes = minutes.divmod(MINUTES_PER_HOUR)
  # "%02d:%02d" %[hours,minutes]  -- ONE FORMAT METHOD
  p format('%02d:%02d',hours, minutes)
end

time_of_day(-4231)


# USING DATE CLASS AND CONSIDERING DAY OF THE WEEK
def time_of_day_and_week(delta_minutes)
  t = Date.new(2017,1,15)
  day, minutes = delta_minutes.divmod(MINUTES_PER_DAY)

  # If delta_minutes is negative, need to subtract day from 8 to print out the day of the week correctly using Date#strftime
  delta_minutes >= 0 ? day : day += 8
  # Nexted ternaries to determine day of the week (1-7)
  day_of_week = day >= 0 ? ( day == 1 ? t : t.next_day(day) ) :
                  t.prev_day(day)

  hours, minutes = minutes.divmod(MINUTES_PER_HOUR)

  p day_of_week.strftime('%A') + format(' %02d:%02d',hours, minutes)
end

time_of_day_and_week(-4231)
