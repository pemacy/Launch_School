# frozen_string_literal: true

require 'minitest/autorun'
require_relative 'text'

class TextTest < Minitest::Test
  def setup
    @str = File.open('sample_text.txt').read
    @text = Text.new @str
  end

  def teardown
    puts 'Torndown'
  end

  def test_swap
    assert_equal @text.swap('t', 'g'), @str.gsub('t', 'g')
  end

  def test_word_count
    assert_equal 72, @text.word_count
  end
end
