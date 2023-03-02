# frozen_string_literal: true

# 1. Add a class method to your MyCar class that calculates the gas mileage of
# any car.

# 2. Override the to_s method to create a user friendly print out of your object.

class MyCar
  attr_accessor :color, :miles_traveled, :fuel_used
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

  def gas_mileage
    @gas_mileage = @miles_traveled / @fuel_used
  end

  def to_s
    puts "You are driving a #{@year} #{@color} #{@model} car!"
  end
end
