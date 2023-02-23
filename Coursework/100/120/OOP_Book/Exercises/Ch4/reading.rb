
class Animal
  def speak
    'Hello'
  end
end

class GoodDog < Animal
  attr_accessor :name

  def initialize(n)
    self.name = n
  end

  def speak
    "#{@name} says " + super
  end
end

sparky = GoodDog.new("Sparky")
puts sparky.speak
p sparky.class.ancestors
