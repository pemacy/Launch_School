def sum_sq_diff(num)
    counter = 1
    num_arr = []
    loop do
        num_arr << counter
        break if counter == num
        counter += 1
    end
    sum_squared = num_arr.reduce(:+) ** 2
    sum_of_squares = num_arr.map{ |n| n**2 }.reduce(:+)
    sum_squared - sum_of_squares
end

p sum_sq_diff(10)
p sum_sq_diff(3)
