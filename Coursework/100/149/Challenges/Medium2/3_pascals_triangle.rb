# 3_pascals_triangle.rb
require 'pry'

class Triangle
	def initialize(num)
		@num = num
		@arr = [[1],[1,1]]
	end

	def rows
		first_iteration if @num > 2
		@arr.first(@num)
	end

	def first_iteration
		(@num - 2).times do |n|
			a = @arr.last.dup
			@arr << [1, second_iteration(a), 1].flatten
		end
	end	

	def second_iteration(a)
		b = []
		(a.size - 1).times do |n|
			b << (a[n] + a[n+1])
		end
		b
	end
end

result = Triangle.new(8)

result.rows.each do |el|
puts el.join(' ').center(result.rows.last.size * 2 + 2)
end	
