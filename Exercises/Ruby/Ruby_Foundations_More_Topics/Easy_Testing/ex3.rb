# frozen_string_literal: true

# Write a minitest assertion that will fail if value is not nil

require 'minitest/autorun'

describe 'nil test' do
  it 'is nil if its an unassigned instance variable' do
    assert_nil @var, 'is not nil'
  end
end

class NilTest < Minitest::Test
  def test_instance_var_nil
    assert_nil @var, 'it is not nil'
  end
end
