def star(num)
    # Test for bad input
    begin
        num.integer?
    rescue NoMethodError
        return 'Input was not a number'
    end

    return 'Input not 7 or greater' if num < 7

    # Star algorithm
    star = []
    spacing = num / 2 - 1
    spacing.downto(0) do |n|
        star << ('*' + ' ' * n + '*' + ' ' * n + '*').center(num)
    end
    star << '*' * num
    0.upto(spacing) do |n|
        star << ('*' + ' ' * n + '*' + ' ' * n + '*').center(num)
    end
    star
end

puts star(7)
