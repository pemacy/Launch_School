require 'pry'

class CircularBuffer
  %w[Empty Full].each { |e| const_set("Buffer#{e}Exception", Class.new(IOError)) }

  def initialize(size)
    clear && @full = -> { @buffer.size == size }
    binding.pry
  end

  def clear; @buffer = [] end

  def read
    @buffer.shift.tap { |elem| elem.nil? && raise(BufferEmptyException) }
  end

  def write(elem)
    !elem.nil? && (@full[] ? raise(BufferFullException) : @buffer.push(*elem))
  end

  def write!(elem)
    @full[] ? @buffer.tap { |b| !elem.nil? && read }.push(*elem) : write(elem)
  end
end

buffer.write '1'
buffer.write '2'
buffer.write! 'A'
p buffer.read
p buffer.read
