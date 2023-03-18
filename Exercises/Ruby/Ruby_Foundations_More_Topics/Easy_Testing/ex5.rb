# frozen_string_literal: true

# Write a minitest assertion that will fail if the 'xyz' is not in the Array list

require 'minitest/autorun'

describe 'items included in array' do
  it 'asserts xyz is in the array' do
    assert_includes ['xyz'], 'xyz', 'it is not in the list'
  end

  it 'refutes that abc is not in the array' do
    refute_includes ['xyz'], 'abc', 'it is in the list'
  end
end

class IncludesTest < Minitest::Test
  def test_includes_xyz
    assert_includes ['xyz'], 'xyz', 'it is not in the list'
  end

  def test_does_not_incude_abc
    refute_includes ['xyz'], 'abc', 'it is in the list'
  end
end
