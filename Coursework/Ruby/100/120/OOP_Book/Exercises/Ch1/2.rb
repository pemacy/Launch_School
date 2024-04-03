# What is a module? What is its purpose? How do we use them with our classes? Create a module for the class you created in exercise 1 and include it properly.

# A module is like a class where it can have it's own methods, but unlike a class, you can't make instances of a Module

require './module'

class ExampleClass
  include MyMod

  def speak(name)
    "hello #{name}"
  end
end

welp = ExampleClass.new
welp.woof
