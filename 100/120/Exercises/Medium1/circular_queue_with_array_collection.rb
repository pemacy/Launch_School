# circular_queue.rb

class CircularQueue
  attr_accessor :arr
  def initialize(num)
    @num = num
    @arr = Array.new(@num, nil)
  end

  def enqueue(obj)
    @arr << obj
    enq = @arr.shift
    sort_arr
    enq
  end

  def dequeue
    @arr << nil
    return @arr.shift if @arr.all? { |el| el == nil}

    idx = []
    @arr.each_with_index { |el,i| idx << i if el != nil}
    deq = @arr.delete_at(idx[0])
    sort_arr
    deq
  end

  private

  def sort_arr
    num_nil = @arr.count(nil)
    @arr.delete_if { |el| el == nil}
    num_nil.times { @arr.unshift(nil) }
  end
end

queue = CircularQueue.new(3)
puts queue.dequeue == nil

queue.enqueue(1)
queue.enqueue(2)
puts queue.dequeue == 1

queue.enqueue(3)
queue.enqueue(4)
puts queue.dequeue == 2

queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
puts queue.dequeue == 5
puts queue.dequeue == 6
puts queue.dequeue == 7
puts queue.dequeue == nil

queue = CircularQueue.new(4)
puts queue.dequeue == nil

queue.enqueue(1)
queue.enqueue(2)
puts queue.dequeue == 1

queue.enqueue(3)
queue.enqueue(4)
puts queue.dequeue == 2

queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
puts queue.dequeue == 4
puts queue.dequeue == 5
puts queue.dequeue == 6
puts queue.dequeue == 7
puts queue.dequeue == nil
