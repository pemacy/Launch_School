# 8_max_by.rb

def max_by(arr)
  largest = arr.first
  arr.each do |obj|
    yield(largest) > yield(obj) ? next : largest = obj
  end
  largest
end

p max_by([1, 5, 3]) { |value| value + 2 }
p max_by([1, 5, 3]) { |value| 9 - value } #== 1
p max_by([1, 5, 3]) { |value| (96 - value).chr } == 1
p max_by([[1, 2], [3, 4, 5], [6]]) { |value| value.size } == [3, 4, 5]
p max_by([-7]) { |value| value * 3 } == -7
p max_by([]) { |value| value + 5 } == nil


# Recursive
def max_r(arr, &block)
  return arr.first if arr.size <= 1
  block.call(arr.first) > max_r(arr.drop(1), &block) ? arr.first : max_r(arr.drop(1), &block)
end


p max_r([1, 5, 3]) { |value| value + 2 }


# Reduce method

def max_red(arr)
  arr.reduce { |largest, obj| yield(obj) > yield(largest) ? obj : largest}
end

p max_red([1, 5, 3]) { |value| value + 2 }
p max_red([1, 5, 3]) { |value| 9 - value } #== 1
p max_red([1, 5, 3]) { |value| (96 - value).chr } == 1
p max_red([[1, 2], [3, 4, 5], [6]]) { |value| value.size } == [3, 4, 5]
p max_red([-7]) { |value| value * 3 } == -7
p max_red([]) { |value| value + 5 } == nil

# sort_by method

def max_sb(arr)
  arr.sort_by{|e| yield(e)}.last
end


p max_sb([1, 5, 3]) { |value| value + 2 }
p max_sb([1, 5, 3]) { |value| 9 - value } #== 1
p max_sb([1, 5, 3]) { |value| (96 - value).chr } == 1
p max_sb([[1, 2], [3, 4, 5], [6]]) { |value| value.size } == [3, 4, 5]
p max_sb([-7]) { |value| value * 3 } == -7
p max_sb([]) { |value| value + 5 } == nil
