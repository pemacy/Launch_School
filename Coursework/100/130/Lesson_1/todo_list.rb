# todo_list.rb

require_relative 'todo'

class TodoList
  attr_accessor :title

  def initialize(title)
    @title = title
    @list = []
  end

  def to_s
    text = "---- #{title} ----\n"
    text << @list.map(&:to_s).join("\n")
    text
  end

  def add(todo)
    if todo.class == Todo
      @list << todo
    else
      raise TypeError, "Can only add Todo objects"
    end
  end

  alias :<< :add

  def size
    @list.size
  end

  def to_a
    @list
  end

  def [](num)
    @list.fetch(num)
  end

  def first
    @list.first
  end

  def last
    @list.last
  end

  def item_at(index)
    @list.fetch(index)
  end

  def mark_done_at(index)
    @list.fetch(index).done!
  end

  def mark_undone_at(index)
    @list.fetch(index).undone!
  end

  def shift
    @list.shift
  end

  def pop
    @list.pop
  end

  def remove_at(index)
    @list.fetch(index)
    @list.delete_at(index)
  end

  def each
    counter = 0
    while counter < size
      yield(@list.fetch(counter))
      counter += 1
    end
    self
  end

  def select(select_title = title)
    arr = TodoList.new(select_title)
    each { |el| arr << el if yield(el) }
    arr
  end

  def find_by_title(search)
    select("Find by title") { |todo| todo.item == search }
  end

  def done?
    @list.all? { |todo| todo.done? }
  end


  def all_done
    select("All Done Items") { |todo| todo.done? }
  end

  def all_not_done
    select("Still Left ToDo") { |todo| !todo.done? }
  end

  def mark_done(todo_item)
    matched_items = select { |todo| todo.item == todo_item }
    matched_items[0].done!
  end

  def mark_all_done
    each { |todo| todo.done! }
  end

  alias :done! :mark_all_done

  def mark_all_undone
    each { |todo| todo.undone! }
  end
end

# # given
# todo1 = Todo.new("Buy milk")
# todo2 = Todo.new("Clean room")
# todo3 = Todo.new("Go to gym")
# list = TodoList.new("Today's Todos")
#
# # add
# list.add(todo1)                 # adds todo1 to end of list, returns list
# list.add(todo2)                 # adds todo2 to end of list, returns list
# list.add(todo3)                 # adds todo3 to end of list, returns list
#
# list.to_s
#
# list.mark_done_at(1)
#
# list.to_s
#
#
# list.each do |todo|
#   puts todo
# end
#
# results = list.select { |todo| todo.done? }    # you need to implement this method
#
# results.to_s
#
# list.find_by_title("Buy milk").to_s
# list.all_done.to_s
# list.all_not_done.to_s
# list.mark_done("Buy milk")
# list.to_s
#
# list.mark_all_done
# list.to_s
# list.mark_all_undone
# list.to_s
