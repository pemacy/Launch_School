# frozen_string_literal: true

# Consider the following class:

# Modify this class so both flip_switch and the setter method switch= are
# private methods.

class Machine
  attr_reader :switch

  def start
    self.flip_switch(:on)
  end

  def stop
    self.flip_switch(:off)
  end

  private

  attr_writer :switch

  def flip_switch(desired_state)
    self.switch = desired_state
  end
end

m = Machine.new
m.start
puts m.switch
m.stop
puts m.switch
begin
  m.switch = :on
rescue
  puts 'unable'
end

puts m.switch

begin
  m.flip_switch(:on)
rescue
  puts 'unable'
end
