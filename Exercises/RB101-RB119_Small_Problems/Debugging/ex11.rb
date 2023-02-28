# frozen_string_literal: true

# Josh wants to print an array of numeric strings in reverse numerical order.
# However, the output is wrong. Without removing any code, help Josh get the
# expected output.

arr = ["9", "8", "7", "10", "11"]

p arr

p arr.map(&:to_i).sort { |x, y| y <=> x }.map(&:to_s)
# prints ["11", "10", "9", "8", "7"]

p arr.map(&:to_i).sort do |x, y|
  y <=> x
end.map(&:to_s)
# [7, 8, 9, 10, 11]

p arr.sort
# ["10", "11", "7", "8", "9"]

p arr.sort do |x, y|
    y.to_i <=> x.to_i
  end
# ["10", "11", "7", "8", "9"]

a = arr.sort do |x, y|
      y.to_i <=> x.to_i
    end

p a
# prints ["11", "10", "9", "8", "7"]

# Expected output: ["11", "10", "9", "8", "7"]
# Actual output: ["10", "11", "7", "8", "9"]
