require 'date'

class Meetup
  def initialize(month, year)
    @month, @year = month, year
  end

  def day(weekday, schedule)
    day = find_scheduled_day(weekday, schedule) + 1
    Date.new(@year, @month, day)
  end

  private

  def find_scheduled_day(weekday, schedule)
    meetup = get_meetup_times[schedule].to_a
    start_day = Date.new( @year, @month, 1 )
    meetup.select { |day| ( start_day + day ).send( "#{weekday}?" ) }.first
  end

  def get_meetup_times
    total_days = Date.new(@year, @month, -1).day
    { first: 0..6, second: 7..13, third: 14..20, fourth: 21..27,
      last: (total_days-7)..(total_days-1), teenth: 12..18 }
  end
end

p Meetup.new(5, 2013).day(:tuesday, :first)
p Meetup.new(4, 2013).day(:friday, :teenth)
