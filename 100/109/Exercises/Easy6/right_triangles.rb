def triangle(num)
  num.times do |n|
    puts ('*' * (n+1)).rjust(num, ' ')
  end
end

triangle(20)
