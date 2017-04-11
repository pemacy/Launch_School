require "minitest/autorun"
# require 'minitest/reporters'
# Minitest::Reporters.use!

require_relative 'cash_register'

class CashRegisterTest < Minitest::Test
  def test_accept_money
    register = CashRegister.new(100)
    trans = Transaction.new(10)
    trans.amount_paid = 10

    assert_equal(register.total_money + trans.amount_paid, register.accept_money(trans))
  end

  def test_change
    register = CashRegister.new(100)
    trans = Transaction.new(10)
    trans.amount_paid = 12.50

    assert_equal(trans.amount_paid - trans.item_cost, register.change(trans))
  end

  def test_give_receipt
    register = CashRegister.new(100)
    trans = Transaction.new(10)

    correct_receipt = "You've paid $10.\n"
    assert_output(correct_receipt) do
      register.give_receipt(trans)
    end
  end

  def test_prompt_for_payment
    trans = Transaction.new(50)
    paid = File.new('paid.txt', "a+")
    paid.print "75\n"
    capture_io do
      trans.prompt_for_payment(input: File.new(paid))
    end
    assert_equal(75, trans.amount_paid)
    paid.close
  end
end
