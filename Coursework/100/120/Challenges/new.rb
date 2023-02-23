module VarMod
  attr_accessor :varb
end

class Closures
  attr_accessor :input
  include VarMod

  def initialize(input)
    self.input = input
  end

  def map(&block)
    counter = 0
    buffer = []
    loop do
      buffer << block.call(input[counter])
      counter += 1
      break if counter >= input.size
    end
    buffer
  end

  def times(num, &block)
    for n in (0...num)
      yield(n)
    end
    num
  end

  def select(&block)
    buffer = []
    for n in input
      buffer << n if block.call(n)
    end
    buffer
  end

  def each(&block)
    return "Empty" unless block_given?
    for e in input
      yield(e)
    end
    input
  end

  def summer(arr = input)
    return arr[0] if arr.size == 1
    arr[0] + self.summer(arr[1..-1])
  end

  def |(whatevs = nil)
    puts 'TOOTHBRUSH'
    system 'clear'
    arr = ['YOU', 'BETTER', 'GET', 'THAT', 'TOOTHBRISTLE!']
    arr.each_with_index do |word, i|
      puts "#{' ' * (i * 5)} #{word}"
    end
  end

  def reduce(arr = input, &block)
    return arr.first if arr.size == 1
    yield(arr[0], self.reduce(arr[1..-1], &block))
  end

  def +(num)
    input.first + num
  end

  protected :reduce
  public :reduce
end


sample = Closures.new([1,2,3,4])
p sample.map{|e| e * 2 }
sample.times(3){|num_passed| p num_passed + 40}
p sample.select{|e| e > 2}
sum = 0
p sample.each{|num| sum += num }
p sum
p sample.summer
p sample.reduce([3,5,9]){|sum, val| sum += val}
sample.varb = 4
p sample.varb

clample = Closures.new(['a', 'b', 'c'])
clample.varb = 6
p [sample.varb, clample.varb]

p sample + 7
sample | 7

var = 'wiley'
trun = Proc.new do |s|
  puts "I'm a Proc #{s}"
end

class Proccer
  def toot(var, &block)
    block.call(var)
  end
end



crea = Proccer.new
crea.toot(var, &trun)
var = 'zimbobwe'


a = 'ssssstrstretukhllgyjiftfbgkhb'
for idx in (0..a.size-1)
  break if a[idx] =~ /[^s]/
end
puts idx
a = a[idx..-1]
p a
