# rotating_matrixes.rb

def rotate90(matrix)
	new_matrix = Array.new(matrix.first.size) { [] }
	matrix.reverse.each do |row|
		row.each_with_index do |el,i|
			new_matrix[i] << el
		end
	end

	new_matrix

end

p rotate90([[1,2],[3,4],[4,5]])
p rotate90([[1, 5, 8],
					 [4, 7, 2],
					 [3, 9, 6]])
