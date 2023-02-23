# merged_sorted_lists.rb

def merge(arr1, arr2)
	mrg = [arr1, arr2].each_with_object([]) { |lst, mrg| lst.each { |e| mrg << e}}
	
	mrg.size.times do |n|
		for cnt in (0...mrg.size)
		 	mrg[n], mrg[cnt] = mrg[cnt], mrg[n] if mrg[cnt] > mrg[n]
		end	
	end
	mrg
end

p merge([1, 5, 9], [2, 6, 8])
p merge([1, 1, 3], [2, 2])
p merge([], [1, 4, 5])
