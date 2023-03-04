# frozen_string_literal: true

# 1. Using the following code, create two classes - Truck and Car - that both
# inherit from Vehicle

# 2. Change the following code so that creating a new Truck automatically
# invokes #start_engine.

class Vehicle
  attr_reader :year

  def initialize(year)
    @year = year
  end
end

class Truck < Vehicle
  def initialize(year)
    super
    start_engine
  end

  def start_engine
    puts 'Ready to go!'
  end
end

class Car < Vehicle
end

truck1 = Truck.new(1994)
puts truck1.year

car1 = Car.new(2006)
puts car1.year
