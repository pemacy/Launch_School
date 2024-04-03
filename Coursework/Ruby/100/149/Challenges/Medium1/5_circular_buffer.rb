# 5_circular_buffer.rb
require 'pry'

p ARGV

class BufferEmptyException < StandardError; end
class BufferFullException < StandardError; end

class CircularBuffer
  def initialize(num)
    @buffer = Array.new(num, [])
  end

  def write(obj)
    raise BufferFullException unless any_empty?
    @buffer[find_empty] = [Element.new(obj)] unless obj.nil?
  end

  def write!(obj)
    @buffer[find_oldest] = [Element.new(obj)] unless any_empty? || obj.nil?
    write(obj) if any_empty?
  end

  def read
    raise BufferEmptyException if all_empty?
    content, @buffer[find_oldest] = @buffer[find_oldest].first.content, []
    content
  end

  def clear; @buffer.map! { [] } end

  private

  def find_oldest
    @buffer.index(@buffer.map{|n| n.first.nil? ? [Element.new(nil)] : n}
                          .min_by{|n| n.first.age}).to_i
  end

  def find_empty; @buffer.find_index(&:empty?) end

  def all_empty?; @buffer.all?(&:empty?) end

  def any_empty?; @buffer.any?(&:empty?) end
end

class Element
  attr_accessor :content, :age
  @@counter = 0

  def initialize(content = [])
    @content = content
    @age = @@counter
    @@counter += 1
  end
end


bi = CircularBuffer.new(7)
bi.write(5)
p bi.read
