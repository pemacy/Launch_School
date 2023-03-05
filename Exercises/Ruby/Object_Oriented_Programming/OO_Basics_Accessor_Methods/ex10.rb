# frozen_string_literal: true

# Modify the following code to accept a string containing a first and last nam
# e. The name should be split into two instance variables in the setter metho
# d, then joined in the getter method to form a full name.

class Person
  # attr_accessor :name - old code

  def name=(name)
    @first, @last = name.split
  end

  def name
    "#{@first} #{@last}"
  end
end

person1 = Person.new
person1.name = 'John Doe'
puts person1.name
