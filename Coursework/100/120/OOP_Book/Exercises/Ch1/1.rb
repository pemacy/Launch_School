# How do we create an object in Ruby? Give an example of the creation of an object.

# We create an object by creating a class.  If we then call the 'new' method on the class we have defined and set it to a variable, that creates an instance of that class

class ExampleClass
  def speak(name)
    "hello #{name}"
  end
end

welp = ExampleClass.new
puts "enter a name"
name = gets.chomp
puts welp.speak(name)
