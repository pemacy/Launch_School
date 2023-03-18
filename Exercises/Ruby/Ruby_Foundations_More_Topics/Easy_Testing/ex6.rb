# frozen_string_literal: true

# Write a minitest assertion that will fail unless employee.hire raises a
# NoExperienceError exception.

require 'minitest/autorun'

class NoExperienceError < StandardError; end

class Employee
  def hire
    raise NoExperienceError
  end
end

describe 'raises an expection when called' do
  before do
    @employee = Employee.new
  end

  it 'raises NoExperienceError exeption' do
    assert_raises(NoExperienceError) { @employee.hire }
  end
end

class ExperienceTest < Minitest::Test
  def setup
    @employee = Employee.new
  end

  def test_no_experience_error
    assert_raises(NoExperienceError) { @employee.hire }
  end
end
