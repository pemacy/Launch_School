# circular_queue.rb

class CircularQueue
  attr_accessor :hsh, :num

  def initialize(num)
    @num = num
    @hsh = {}
    @num.times{|n| hsh[Time.now.nsec] = nil}
  end

  def enqueue(obj)
    if hsh.has_value?(nil)
      hsh.keys.sort.each do |k|
        if hsh[k] == nil
          hsh.delete(k)
          hsh[Time.now.nsec] = obj
          break
        end
      end
    else
      hsh.delete(hsh.keys.sort[0])
      hsh[Time.now.nsec] = obj
    end
  end

  def dequeue
    previous_value = nil
    hsh.keys.sort.each do |k|
      if hsh[k] != nil
        previous_value = hsh[k]
        hsh.delete(k)
        hsh[Time.now.nsec] = nil
        break
      end
    end
    previous_value
  end

  def to_s
    @hsh
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
