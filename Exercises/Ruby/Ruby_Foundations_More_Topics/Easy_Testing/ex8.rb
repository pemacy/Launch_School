# frozen_string_literal: true

# Write a minitest assertion that will fail if the class of value is not
# Numeric or one of Numeric's subclasses (e.g., Integer, Float, etc).

require 'minitest/autorun'

describe 'Numeric class assertion' do
  it 'asserts an integer is a part of the numeric class' do
    assert_kind_of Numeric, 6
  end

  it 'asserts a float is a part of the numeric class' do
    assert_kind_of Numeric, 6.0
  end
end

class NumericClassTest < Minitest::Test
  def test_integer_is_subclass_of_numeric
    assert_kind_of Numeric, 1
  end

  def test_float_is_subclass_of_numeric
    assert_kind_of Numeric, 1.0
  end
end
