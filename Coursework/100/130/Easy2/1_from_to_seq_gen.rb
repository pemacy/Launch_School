# From-To_Step Sequence Generator

def step(start, stop, step, &block)
  loop do
    break if start > stop
    block.call(start)
    start += step
  end
end

step(1, 10, 3) { |value| puts "value = #{value}" }

def stepper(start, stop, incr, &block)
  return nil if start > stop
  block.call(start)
  step(start + incr, stop, incr, &block)
end

stepper(1, 10, 3) { |value| puts "value = #{value}" }
