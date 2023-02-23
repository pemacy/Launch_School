class Clock
  attr_accessor :hr, :min

  def initialize(hr, min)
    @hr, @min = hr, min
  end

  def self.at(hr, min = 0)
    new(hr, min)
  end

  def to_s
    "%02d:%02d" % [hr, min]
  end

  def ==(other_clock)
    other_clock.hr == hr && other_clock.min == min
  end

  def +(mins)
    @hr = (hr + (min + mins) / 60) % 24
    @min = (min + mins) % 60
    self
  end

  def -(mins)
    self.+(-mins)
    # @hr = (24 + hr - ((60 - min + mins) / 60)) % 24
    # @min = 60 - ((min + mins) % 60)
    # self
  end
end

# c = Clock.at(10, 35) - 90
# puts c
