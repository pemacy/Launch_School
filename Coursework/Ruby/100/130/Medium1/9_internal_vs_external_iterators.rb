enum = Enumerator.new do |factorials|
  a = 0
  loop do
    if a.zero?
      factorials << 1
    else
      factorials << (1..a).to_a.reduce(:*)
    end
    a += 1
  end
end

p enum.take(7)
