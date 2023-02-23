# 1_bookl_assert.rb

require 'minitest/autorun'
require 'minitest/reporters'
Minitest::Reporters.use!

class Odder
  def od(value)
    value.odd?
  end
end

class Tester < Minitest::Test
  def test_odd
    tod = Odder.new
    # assert(tod.od(4), 'value is not odd')
    assert(tod.od(5), 'value is not odd')
  end
end


# Tester.new.test_odd(4)
# Teter.new.test_odd(5)
