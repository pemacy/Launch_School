# frozen_string_literal: true

require 'minitest/autorun'

describe 'string downcase' do
  it 'makes XYZ into xyz' do
    assert_equal 'XYZ'.downcase, 'xyz'
  end
end

class TestDowncase < Minitest::Test
  def test_downcase_method
    assert_equal 'XYZ'.downcase, 'xyz'
  end
end
