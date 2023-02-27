# frozen_string_literal: true

# A 3 x 3 matrix can be represented by an Array of Arrays in which the main
# Array and all of the sub-Arrays has 3 elements.

# The transpose of a 3 x 3 matrix is the matrix that results from exchanging
# the columns and rows of the original matrix. For example, the transposition
# of the array shown above is:

# Write a method that takes a 3 x 3 matrix in Array of Arrays format and
# returns the transpose of the original matrix. Note that there is a Array
# #transpose method that does this -- you may not use it for this exercise.
# You also are not allowed to use the Matrix class from the standard library.
# Your task is to do this yourself.

# Take care not to modify the original matrix: you must produce a new matrix
# and leave the original matrix unchanged.

def transpose(matrix)
  matrix.each_with_index.with_object(Array.new(3) {[]}) do |(arr, idx), trans_arr|
    arr.each_with_index do |el, i|
      trans_arr[i] << el
    end
  end
end

matrix = [
  [1, 5, 8],
  [4, 7, 2],
  [3, 9, 6]
]

new_matrix = transpose(matrix)
p new_matrix
p matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]]
