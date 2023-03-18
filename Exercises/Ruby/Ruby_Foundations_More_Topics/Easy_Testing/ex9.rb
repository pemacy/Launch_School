# frozen_string_literal: true

# Write a test that will fail if list and the return value of list.process are
# different objects.

require 'minitest/autorun'

class List < Array
  def process
    self.first
  end
end

describe 'different object test' do
  before do
    @list = List.new
  end

  it 'asserts different objects' do
    refute_match @list, @list.process
  end

  it 'asserts list is the same as an array' do
    assert_kind_of Array, @list
  end
end

class ListTest < Minitest::Test
  def setup
    @list = List.new
  end

  def test_different_objects
    refute_match @list, @list.process
  end
end
