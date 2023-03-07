# frozen_string_literal: true

# What output does this code print? Fix this class so that there are no
# surprises waiting in store for the unsuspecting developer.

class Pet
  attr_reader :name

  def initialize(name)
    @name = name.to_s
  end

  def to_s
    # @name.upcase! - old code
    "My name is #{@name.upcase}." # new code
  end
end

name = 'Fluffy'
fluffy = Pet.new(name)
puts fluffy.name
puts fluffy
puts fluffy.name
puts name
