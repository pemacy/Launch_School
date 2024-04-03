# 5_drop_while.rb

def drop_while(arr)
  return [] if arr.empty?
  arr.each_with_index do |e, i|
    if yield(e)
      next
    else
      return arr[i..-1]
    end
  end
end

p drop_while([1, 3, 5, 6]) { |value| value.odd? }
p drop_while([1, 3, 5, 6]) { |value| false }
p drop_while([]) { |value| true }

# Recursive
def drop_while_rec(arr, &block)
  (arr.empty? || !block.call(arr.first)) ? arr : drop_while_rec(arr.drop(1), &block)
end

p drop_while_rec([1, 3, 5, 6]) { |value| value.even? }
p drop_while_rec([1, 3, 5, 6]) { |value| false }
p drop_while_rec([]) { |value| true }
