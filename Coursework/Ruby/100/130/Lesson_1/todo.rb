# This class represents a todo item and its associated
# data: item and state. There's also a "done"
# flag to show whether this todo item is done.

class Todo
  DONE_MARKER = 'X'
  UNDONE_MARKER = ' '

  attr_accessor :item, :state, :done

  def initialize(item, state='')
    @item = item
    @state = state
    @done = false
  end

  def done!
    self.done = true
  end

  def done?
    done
  end

  def undone!
    self.done = false
  end

  def to_s
    "[#{done? ? DONE_MARKER : UNDONE_MARKER}] #{item}"
  end
end


#FINAL
# This class represents a todo item and its associated
# data: name and description. There's also a "done"
# flag to show whether this todo item is done.

class Todo
  DONE_MARKER = 'X'
  UNDONE_MARKER = ' '

  attr_accessor :title, :description, :done

  def initialize(title, description='')
    @title = title
    @description = description
    @done = false
  end

  def done!
    self.done = true
  end

  def done?
    done
  end

  def undone!
    self.done = false
  end

  def to_s
    "[#{done? ? DONE_MARKER : UNDONE_MARKER}] #{title}"
  end
end

class TodoList
  attr_accessor :title

  def initialize(title)
    @title = title
    @todos = []
  end

  def <<(*todo)
    raise TypeError, "Can only add Todo objects" if todo.any?{|t| t.class != Todo}
    todo.each{|t| @todos << t}
  end

  alias_method :add, :<<

  def size
    @todos.size
  end

  def first
    @todos.first
  end

  def last
    @todos.last
  end

  def [](num)
    @todos.fetch(num)
  end

  def mark_done_at(num)
    @todos.fetch(num).done!
  end

  def mark_undone_at(num)
    @todos.fetch(num).undone!
  end

  def to_s
    text = "----- #{title} -----\n"
    each { |todo| text << todo.to_s; text << "\n"}
    text
  end

  def to_a
    @todos
  end

  def each
    for todo in @todos
      yield(todo)
    end
    self
  end

  def select(title = "Selected Items")
    results = TodoList.new(title)
    each { |todo| results << todo if yield todo}
    results
  end
end

todo1 = Todo.new("Buy milk")
todo2 = Todo.new("Clean room")
todo3 = Todo.new("Go to gym")
list = TodoList.new("Today's Todos")



list.add(todo1, todo2, todo3)
list.each{|t| t.done!}
puts list
list[1].undone!
puts list.select{|t| !t.done?}
puts list.each{|a| puts "hey there"}


module First
end

module Second
end

module Third
end

module Fourth
end

class FirstClass
  include Third
  include Fourth
end

class SecondClass < FirstClass
  include Second
  include First
end

p SecondClass.ancestors
