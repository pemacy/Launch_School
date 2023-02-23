OPERATORS = [:+, :-, :*, :/, :%, :**]

def do_operations(arr, result)
  OPERATORS.each do |operator|
    result << "==> #{arr[0]} + #{arr[1]} = #{arr.reduce(operator)}"
  end
end

arr = []
result = []
puts "Enter the first number"
arr << gets.chomp.to_i
puts "Enter the second number"
arr << gets.chomp.to_i

do_operations(arr, result)
result.each {|operation| puts operation}
