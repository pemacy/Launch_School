# frozen_string_literal: true

# Write a minitest assertion that will fail if value is not an instance of the
# Numeric class exactly. value may not be an instance of one of Numeric's
# superclasses.

require 'minitest/autorun'

describe 'Numeric class assertion' do
  it 'asserts a number is a part of the numeric class' do
    num = Numeric.new
    assert_instance_of Numeric, num
  end

  it 'refutes that an interger is an instance of Numeric' do
    refute_instance_of Numeric, 1
  end
end

class NumericClassTest < Minitest::Test
  def test_is_numeric_class
    num = Numeric.new
    assert_instance_of Numeric, num
  end

  def test_refute_numeric
    refute_instance_of Numeric, 1
  end
end
