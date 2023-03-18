# frozen_string_literal: true

# Write a test that will fail if 'xyz' is one of the elements in the Array
# list:

require 'minitest/autorun'

describe 'test item not in array' do
  it 'does not include xyz' do
    refute_includes [1,2,3], 'abc', 'failure: array includes xyz'
  end
end

class IncludesTest < Minitest::Test
  def setup
    @list = [1,2,3]
  end

  def test_list_not_includes_xyz
    refute_includes [1,2,3], 'abc', 'failure: array includes xyz'
  end
end
