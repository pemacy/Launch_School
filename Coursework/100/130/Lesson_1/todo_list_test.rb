require 'simplecov'
SimpleCov.start

require 'minitest/autorun'
require "minitest/reporters"
Minitest::Reporters.use!

require_relative 'todo_list'

class TodoListTest < MiniTest::Test

  def setup
    @todo1 = Todo.new("Buy milk")
    @todo2 = Todo.new("Clean room")
    @todo3 = Todo.new("Go to gym")
    @todos = [@todo1, @todo2, @todo3]

    @list = TodoList.new("Today's Todos")
    @list.add(@todo1)
    @list.add(@todo2)
    @list.add(@todo3)
  end

  # Your tests go here. Remember they must start with "test_"
  def test_to_a
    assert_equal(@todos, @list.to_a)
  end

  def test_size
    assert_equal(3, @list.size)
  end

  def test_first
    assert_equal(@todo1, @list.first)
  end

  def test_last
    assert_equal(@todo3, @list.last)
  end

  def test_shift
    assert_equal(@todo1, @list.shift)
  end

  def test_pop
    assert_equal(@todo3, @list.pop)
  end

  def test_done?
    refute(@todo1.done?)
  end

  def test_type_error
    assert_raises(TypeError) {@list << 1}
  end

  def test_shovel
    @list << @todo1
    @todos << @todo1
    assert_equal(@todos, @list.to_a)
  end

  def test_item_at
    assert_raises(IndexError) {@list.item_at(6)}
    assert_equal(@todo1, @list.item_at(0))
  end

  def test_mark_done_at
    assert_raises(IndexError) {@list.mark_done_at(5)}
    @list.mark_done_at(1)

    assert_equal(false,@todo1.done?)
    assert(@todo2.done?)
    refute(@todo3.done?)
  end

  def test_mark_undone_at
    @list.mark_all_done
    @list.mark_undone_at(1)

    assert(@todo1.done?)
    refute(@todo2.done?)
    assert(@todo3.done?)
  end

  def test_mark_all_done
    @list.mark_all_done
    assert_equal(true, @todo1.done?)
    assert_equal(true, @todo2.done?)
    assert_equal(true, @todo3.done?)
    assert_equal(true, @list.done?)
  end

  def test_done!
    @list.done!
    assert_equal(true, @todo1.done?)
    assert_equal(true, @todo2.done?)
    assert_equal(true, @todo3.done?)
    assert_equal(true, @list.done?)
  end

  def test_remove_at
    assert_raises(IndexError) { @list.remove_at(100)}
    @list.remove_at(0)

    assert_equal([@todo2, @todo3], @list.to_a)
  end

  def test_to_s
    output = <<-OUTPUT.chomp.gsub /^\s+/, ""
    ---- Today's Todos ----
    [ ] Buy milk
    [ ] Clean room
    [ ] Go to gym
    OUTPUT

    assert_equal(output, @list.to_s)
  end

  def test_to_s_with_one_done
    output = <<-OUTPUT.chomp.gsub /^\s+/, ""
    ---- Today's Todos ----
    [X] Buy milk
    [ ] Clean room
    [ ] Go to gym
    OUTPUT

    @list.mark_done_at(0)
    assert_equal(output, @list.to_s)
  end

  def test_to_s_with_all_done
    output = <<-OUTPUT.chomp.gsub /^\s+/, ""
    ---- Today's Todos ----
    [X] Buy milk
    [X] Clean room
    [X] Go to gym
    OUTPUT

    @list.done!
    assert_equal(output, @list.to_s)
  end

  def test_each
    arr = []
    @list.each { |todo| arr << todo}
    assert_equal(@list.to_a, arr)
  end

  def test_select
    arr = @list.select { |todo| todo.done?}
    assert_equal([], arr.to_a)

    @list.done!
    arr = @list.select { |todo| todo.done?}
    assert_equal(@list.to_a, arr.to_a)
  end
end
