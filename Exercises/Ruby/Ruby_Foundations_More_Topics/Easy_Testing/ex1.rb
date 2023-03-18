# frozen_string_literal: true

# Write a minitest assertion that will fail if the value.odd? is not true.

require 'minitest/autorun'

class Odder
  def odd?(num)
    num.odd?
  end
end

describe Odder do
  it 'asserts 5 is odd' do
    assert 5.odd?, '5 is not odd'
  end

  it 'asserts 4 is not odd' do
    refute 4.odd?, '4 is odd'
  end
end


class IntegerTest < Minitest::Test
  def test_that_3_is_odd
    assert 3.odd?, "Not odd"
  end
end
