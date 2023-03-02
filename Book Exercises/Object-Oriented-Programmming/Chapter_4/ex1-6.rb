# frozen_string_literal: true

# 1. Create a superclass called Vehicle for your MyCar class to inherit from
# and move the behavior that isn't specific to the MyCar class to the
# superclass. Create a constant in your MyCar class that stores information
# about the vehicle that makes it different from other types of Vehicles.

# Then create a new class called MyTruck that inherits from your superclass
# that also has a constant defined that separates it from the MyCar class in
# some way.

# 2. Add a class variable to your superclass that can keep track of the number
# of objects created that inherit from the superclass. Create a method to
# print out the value of this class variable as well.

# 3. Create a module that you can mix in to ONE of your subclasses that
# describes a behavior unique to that subclass.

# 4. Print to the screen your method lookup for the classes that you have created.

# 5. Move all of the methods from the MyCar class that also pertain to the
# MyTruck class into the Vehicle class. Make sure that all of your previous
# method calls are working when you are finished.

# 6. Write a method called age that calls a private method to calculate the
# age of the vehicle. Make sure the private method is not available from
# outside of the class. You'll need to use Ruby's built-in Time class to help.

module Insurance
  def claims
    puts "You have made #{@claims} on your vehicle"
  end
end

class Vehicle
  attr_accessor :color, :miles_traveled, :fuel_used
  attr_reader :year
  @@vehicles_created = 0

  def initialize(year, color, model)
    @year = year
    @color = color
    @model = model
    @speed = 0
    @status = "On"
    @@vehicles_created += 1
  end

  def self.vehicles_created
    puts "#{@@vehicles_created} vehicles created"
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

  def self.gas_mileage(gallons, miles)
    puts "#{miles / gallons} mpg"
  end

  def to_s
    puts "You are driving a #{@year} #{@color} #{@model} car!"
  end

  def age
    calculate_age
  end

  private

  def calculate_age
    Time.now.year - self.year
  end
end

class MyCar < Vehicle
  include Insurance

  attr_accessor :sedan_type
end

class MyTruck < Vehicle
  attr_accessor :cab_type
end

car = MyCar.new(2020, "white", "Mazda")
Vehicle.gas_mileage(5, 100)
Vehicle.vehicles_created
car.claims
