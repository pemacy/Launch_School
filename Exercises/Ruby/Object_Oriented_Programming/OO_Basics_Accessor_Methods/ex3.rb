# frozen_string_literal: true

# Modify the following code so that the value of @phone_number can still be
# read as on line 10, but cannot be changed as on line 12.

class Person
  # attr_accessor :phone_number - old code
  attr_reader :phone_number # new code

  def initialize(number)
    @phone_number = number
  end
end

person1 = Person.new(1234567899)
puts person1.phone_number

person1.phone_number = 9987654321
puts person1.phone_number
