def bubble_sort(array)
    arr_iter = array.size - 2
    counter = 0
    loop do
        done = counter
        0.upto(arr_iter) do |i|
            if array[i] > array[i+1]
              counter += 1
              array[i..i+1] = array[i+1],array[i]
            end
        end
        break if  done == counter
    end
    array
end

array = %w(Sue Pete Alice Tyler Rachel Kim Bonnie)
p bubble_sort(array)

array = [5, 3]
bubble_sort(array)
p array == [3, 5]

array = [6, 2, 7, 1, 4]
bubble_sort(array)
p array == [1, 2, 4, 6, 7]
