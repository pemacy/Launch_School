# frozen_string_literal: true

# Create a class called MyCar. When you initialize a new instance or object of
# the class, allow the user to define some instance variables that tell us the
# year, color, and model of the car. Create an instance variable that is set
# to 0 during instantiation of the object to track the current speed of the
# car as well. Create instance methods that allow the car to speed up, brake,
# and shut the car off.

class MyCar
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
