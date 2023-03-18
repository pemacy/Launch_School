# frozen_string_literal: true

# Write a minitest assertion that will fail if the Array list is not empty.

require 'minitest/autorun'

describe 'empty array' do
  it 'asserts array is empty' do
    assert_empty [], 'it is not empty'
  end

  it 'refutes array is not empty' do
    refute_empty [1], 'it is empty'
  end
end

class EmptyTest < Minitest::Test
  def test_assert_array_empty
    assert_empty [], 'it is not empty'
  end

  def test_refute_array_empty
    refute_empty [1], 'it is empty'
  end
end
