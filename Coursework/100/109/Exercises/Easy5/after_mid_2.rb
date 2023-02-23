def after_midnight(time)
  time = time.split(':').map(&:to_i)
  time[0] = time[0] < 24 ? time[0] * 60 : 0
  time.reduce(:+)
end

def before_midnight(time)
  time = time.split(':').map(&:to_i)
  time[0] = time[0] < 24 ? (24 - time[0]) * 60 : 0
  time[1] = time[1] != 0 ? 60 - time[1] : 0
  time.reduce(:+)
end

p after_midnight('05:00')
p before_midnight('24:00')


require 'time'

SECONDS_IN_MIN = 60
MINUTES_IN_HR = 60
HR_IN_DAY = 24
SECONDS_IN_DAY = SECONDS_IN_MIN * MINUTES_IN_HR * HR_IN_DAY

def midnight(time_string)
  # Minutes before midnight
  before_mid = (SECONDS_IN_DAY - (Time.parse("24:00") - Time.parse(time_string))) / 60

  # Minutes after midnight
  after_mid = (Time.parse(time_string) - Time.parse("00:00")) / 60

  [before_mid, after_mid].map(&:to_i)
end

p midnight("05:00")
