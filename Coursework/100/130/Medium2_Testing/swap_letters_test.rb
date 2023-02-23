require 'minitest/autorun'
require 'minitest/reporters'
Minitest::Reporters.use!

require_relative 'swap_letters'

class SwapLettersTest < Minitest::Test
  def setup
    @file = File.open("loren.txt", "r")
    @txt = Text.new(@file.read)
  end

  def test_swap
    l1, l2 = @txt.text[0], '@'
    swapped = @txt.swap(l1, l2)
    assert_equal('@', swapped[0])
  end

  def test_count_letters
    assert_equal 72, @txt.word_count
  end

  def teardown
    @file.close
    puts "File has been closed: #{@file.closed?}"
  end
end
