# frozen_string_literal: true

# You want to create a nice interface that allows you to accurately describe
# the action you want your program to perform. Create a method called
# spray_paint that can be called on an object and will modify the color of the car.

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

  def spray_paint(color)
    @color = color
  end
end
