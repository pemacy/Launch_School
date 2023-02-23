# take_block.rb

def take_block(&block)
  block.call
end

take_block do
  puts "block being called in the method"
end

def take_block_num(num, &block)
  block.call(num)
end

num = 42

take_block_num(num) do
  puts "takes the block and the number #{num}"
end
