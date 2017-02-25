class MyCar
  @@my_car_counter = 0

  attr_accessor :color, :speed
  attr_reader :model, :year

  def initialize(year, color, model)
    @@my_car_counter += 1
    self.speed = 0
    @year = year
    self.color = color
    @model = model
  end

  def speed_up
    self.speed += 10
  end

  def brake
    self.speed -= 10
  end

  def shut_down
    self.speed = 0
    puts "#{@model} is shut down"
  end

  def info
    "This is a #{self.color} #{year} #{@model}"
  end

  def self.my_car_cntr
    @@my_car_counter
  end
end

volvo = MyCar.new(2010, 'Yellow', 'StationWagon')
buick = MyCar.new(2011, 'Blue', 'Sedan')
puts volvo.info
volvo.color= 'Blue'
puts volvo.info
puts volvo.model
puts MyCar.my_car_cntr

volvo.speed_up
puts volvo.speed
volvo.speed_up
puts volvo.speed
volvo.shut_down
puts volvo.speed
