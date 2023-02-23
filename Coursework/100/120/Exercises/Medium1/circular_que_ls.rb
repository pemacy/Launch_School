# circular_queue.rb

class CircularQueue
  attr_accessor :buffer, :oldest, :next
  def initialize(num)
    @buffer = Array.new(num)
    @oldest = 0
    @next = 0
  end

  def enqueue(obj)
    unless @buffer[@next].nil?
      @oldest = increment(@next)
    end

    @buffer[@next] = obj
    @next = increment(@next)
  end

  def dequeue
    value = @buffer[@oldest]
    @buffer[@oldest] = nil
    @oldest = increment(@oldest) unless value.nil?
    value
  end

  private

  def increment(position)
    (position + 1) % buffer.size
  end
end

queue = CircularQueue.new(3)
puts queue.dequeue == nil
p [queue.buffer, queue.oldest, queue.next]

queue.enqueue(1)
queue.enqueue(2)
puts queue.dequeue == 1
p [queue.buffer, queue.oldest, queue.next]

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
p [queue.buffer, queue.oldest, queue.next]

puts queue.dequeue == 1

queue.enqueue(3)
queue.enqueue(4)
puts queue.dequeue == 2
p [queue.buffer, queue.oldest, queue.next]

queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
puts queue.dequeue == 4
puts queue.dequeue == 5
p [queue.buffer, queue.oldest, queue.next]

puts queue.dequeue == 6
puts queue.dequeue == 7
puts queue.dequeue == nil
