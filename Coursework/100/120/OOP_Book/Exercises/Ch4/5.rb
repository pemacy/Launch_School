module Convertable
  def is_convertable?(poptop)
    poptop ? true : false
  end
end

class Vehicle
  @@number_of_vehicles = 0
  attr_accessor :color
  attr_reader :year, :model

  def initialize(year, model, color)
    @@number_of_vehicles += 1
    @year = year
    @model = model
    self.color = color
    @speed = 0
  end

  def self.gas_mileage(gallons, miles)
    puts "#{miles / gallons} miles per gallon of gas"
  end

  def speed_up(mph)
    @speed += mph
    puts "You push the gas and accelerate #{mph} mph."
  end

  def brake(mph)
    @speed -= mph
    puts "You push the brake and decelerate #{mph} mph."
  end

  def current_speed
    puts "You are going #{@speed} miles per hour"
  end

  def shut_down
    puts "Let's park this bad boy"
  end

  def spray_paint(color)
    self.color = color
  end

end

class MyCar < Vehicle
  include Convertable

  NUMBER_OF_DOORS = 4

  def to_s
    "This car is a #{self.year} #{self.model} and is #{self.color}"
  end

end

class MyTruck < Vehicle

  NUMBER_OF_DOORS = 2
end

lumina = MyCar.new(1997, 'chevy lumina', 'white')
lumina.speed_up(20)
lumina.current_speed
lumina.speed_up(20)
lumina.current_speed
lumina.brake(20)
lumina.current_speed
lumina.brake(20)
lumina.current_speed
lumina.shut_down
MyCar.gas_mileage(13, 351)
lumina.spray_paint("red")
puts lumina
puts MyCar.ancestors
puts MyTruck.ancestors
puts Vehicle.ancestors
