# frozen_string_literal: true

# Now that we have a Walkable module, we are given a new challenge. Apparently
# some of our users are nobility, and the regular way of walking simply isn't
# good enough. Nobility need to strut.

# We need a new class Noble that shows the title and name when walk is
# called:

module Walkable
  def walk
    puts "#{self.name} #{self.gait} forward"
  end
end

# given code
class Person
  include Walkable

  attr_reader :name

  def initialize(name)
    @name = name
  end

  private

  def gait
    "strolls"
  end
end

class Noble < Person
  attr_reader :title

  def initialize(name, title)
    super(name)
    @title = title
  end

  private

  def gait
    "struts"
  end
end

byron = Noble.new("Byron", "Lord")
byron.walk
# => "Lord Byron struts forward"
puts byron.name
# => "Byron"
puts byron.title
# => "Lord"
