# frozen_string_literal: true

# 1. Create an empty class named Cat.

# 3. Using the code from the previous exercise, add an #initialize method that
# prints I'm a cat! when a new Cat object is instantiated.

# 4. Using the code from the previous exercise, add a parameter to #initialize
# that provides a name for the Cat object. Use an instance variable to print a
# greeting with the provided name. (You can remove the code that displays I'm
# a cat!.)

# 5. Using the code from the previous exercise, move the greeting from the
# #initialize method to an instance method named #greet that prints a greeting when invoked.

# 6. Using the code from the previous exercise, add a getter method named
# #name and invoke it in place of @name in #greet.

# 7. Using the code from the previous exercise, add a setter method named #nam
# e=. Then, rename kitty to 'Luna' and invoke #greet again.

# 8. Using the code from the previous exercise, replace the getter and setter
# methods using Ruby shorthand.

# 9. Using the following code, create a module named Walkable that contains a
# method named #walk. This method should print Let's go for a walk! when
# invoked. Include Walkable in Cat and invoke #walk on kitty.

module Walkable
  def walk
    puts "Let's go for a walk!"
  end
end

class Cat
  include Walkable

  attr_reader :name
  attr_writer :name

  def initialize(name = nil)
    @name = name
    puts "Hello! My name is #{self.name}"
    puts "I'm a cat!"
  end

  # def name
  #   @name
  # end

  # def name=(new_name)
  #   @name = new_name
  # end

  def greet
    puts "Hello! My name is #{name}"
  end
end

# 2. Using the code from the previous exercise, create an instance of Cat
# and assign it to a variable named kitty.

kitty = Cat.new
kitty = Cat.new('Sophie')
kitty.greet
kitty.name = 'Luna'
kitty.greet
kitty.walk
