# frozen_string_literal: true

# Add an accessor method to your MyCar class to change and view the color of
# your car. Then add an accessor method that allows you to view, but not modify,
# the year of your car.

class MyCar
  attr_accessor :color
  attr_reader :year

  def initialize(year, color, model)
    @year = year
    @color = color
    @model = model
    @speed = 0
    @status = on
  end

  def speed_up(value)
    @speed += value
    puts "You've sped up! You now are going #{@speed}MPH"
  end

  def brake(value)
    @speed -= value
    puts "The brakes are slowing you down, you now are going #{@speed}MPH"
  end

  def shutdown
    @status = off
    puts "The car is shut down"
  end
end
