def featured(num)
    bool = [false,false,false]
    loop do
        num += 1
        bool[0] = num.odd?
        bool[1] = num % 7 == 0
        bool[2] = num.to_s.chars.uniq.size == num.to_s.size
        break if bool.all? { |b| b == true }
    end
    num
end

puts featured(997)
