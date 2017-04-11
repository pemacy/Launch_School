def missing(arr)
  p arr.to_a.each_cons(2).reduce([]) { |a, (n1, n2)| [*a, *(n1.next...n2)]}

  # h = (arr.first..arr.last).to_a
  # h.delete_if{ |e| arr.include?(e) }
  # counter = 0
  # q = []
  # loop do
  #   break if counter == h.size
  #   q << h[counter] unless arr.include?(h[counter])
  #   counter += 1
  # end
  # q
end

p missing([-3, -2, 1, 5]) == [-1, 0, 2, 3, 4]
p missing([1, 2, 3, 4]) == []
p missing([1, 5]) == [2, 3, 4]
# p missing([6]) == []
# p missing([])
