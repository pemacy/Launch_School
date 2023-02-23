def friday_13th?(year)
  counter = 0
  1.upto(12) do |month|
    counter += 1 if Time.new(year, month, 13).friday?
  end
  counter
end

p friday_13th?(2015) == 3
p friday_13th?(1986) == 1
p friday_13th?(2019) == 2
