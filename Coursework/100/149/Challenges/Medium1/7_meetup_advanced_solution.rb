require 'date'

class Meetup
  DAYS = { first: 0, second: 1, third: 2, fourth: 3, last: -1 }

  def initialize(month, year)
    @days = *Date.new(year, month)...Date.new(year, month).next_month
  end

  def day(weekday, schedule)
    days = @days.select { |day| day.send("#{weekday}?") }
    days[DAYS[schedule]] rescue days.find { |day| day.mday.between?(13, 19) }
  end
end

p Meetup.new(12, 2013).day(:monday, :fourth)
p Meetup.new(12, 2013).day(:monday, :last)
