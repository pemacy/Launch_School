# frozen_string_literal: true

# Write a class that will display:
# ABC
# xyz

class Transform
  def initialize(str)
    @str = str
  end

  def uppercase
    @str.upcase
  end

  def self.lowercase(text)
    text.downcase
  end
end

# when the following code is run:

my_data = Transform.new('abc')
puts my_data.uppercase
puts Transform.lowercase('XYZ')
