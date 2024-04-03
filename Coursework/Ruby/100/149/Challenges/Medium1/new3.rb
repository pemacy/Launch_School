def find_next_square(sq)
  # Return the next square if sq is a perfect square, -1 otherwise
  sq_test = -> (num){(Math.sqrt num) - (Math.sqrt num).to_i == 0}
  return -1 unless sq_test.call(sq)
  loop do
    sq += 1
    return sq if sq_test.call(sq)
  end
end

p find_next_square(8)
