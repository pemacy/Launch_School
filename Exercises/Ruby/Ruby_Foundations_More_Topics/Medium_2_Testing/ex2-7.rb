# frozen_string_literal: true

# Let's start things from the ground up. We want to make a simple test suite for our CashRegister class. Setup the initial testing file. You don't have to have any tests in your test file. For this exercise, write everything you would need to start testing CashRegister, excluding the tests themselves (necessary requires, test class, etc.).

require 'minitest/autorun'
require_relative 'transaction'
require_relative 'cash_register'

class CashRegisterTest < Minitest::Test
  def setup
    @register = CashRegister.new(100)
    @transaction = Transaction.new(10)
  end

  def test_accept_money
    @transaction.amount_paid = 10
    assert_equal @register.total_money, 100
    @register.accept_money(@transaction)
    assert_equal @register.total_money, 110
  end

  def test_change
    @transaction.amount_paid = 10
    assert_equal 0, @register.change(@transaction)
  end

  def test_give_receipt
    out, err = capture_io { @register.give_receipt(@transaction) }
    assert_equal "You've paid $10.\n", out
  end

  def test_prompt_for_payment
    input = StringIO.new("15\n")
    output = StringIO.new
    @transaction.prompt_for_payment(input: input, output: output)
    assert_equal 15, @transaction.amount_paid
  end
end
