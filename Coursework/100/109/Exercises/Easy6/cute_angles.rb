DEGREE = "\xC2\xB0"

def dms(num)
  decimal = num - num.truncate
  minutes = (decimal * 60).abs
  seconds = ((minutes - minutes.truncate) * 60).round
  "%(#{num.truncate}#{DEGREE}#{minutes.truncate}'#{seconds}\")"
end

puts dms(-123.234)
