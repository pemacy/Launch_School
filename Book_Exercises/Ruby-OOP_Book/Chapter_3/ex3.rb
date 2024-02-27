# frozen_string_literal: true

# When running the following code...

class Person
  attr_reader :name
  def initialize(name)
    @name = name
  end
end

bob = Person.new("Steve")
bob.name = "Bob"


# We get the following error...
#
# test.rb:9:in `<main>': undefined method `name=' for
# #<Person:0x007fef41838a28 @name="Steve"> (NoMethodError)

# Why do we get this error and how do we fix it?

# There is no setter method for name
# fix it by uing attr_accessor instead of attr_reader
