# 4_count.rb
require 'pry'
def count(*args, &block)
  args.reduce(0){ |sum, obj| block.call(obj) ? sum + 1 : sum }
  # sum = 0
  # args.each { |e| sum += 1 if block.call(e)}
  # sum
end

p count(1, 3, 6, 8) { |value| value.odd? } == 2
p count(1, 3, 6) { |value| value.odd? }

# Recursive
def count_rec(*args, &block)
  return 0 if args.empty?
  (block.call(args.first) ? 1 : 0) + count_rec(*args.drop(1), &block)
end


p count_rec(1, 3, 6, 8) { |value| value.odd? } == 2
p count_rec(1, 3, 6) { |value| value.odd? }
