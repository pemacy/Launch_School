PADDING = 'w'
DIAMOND_CHAR = 'l'

def grid(num)
  puts PADDING * (num + 2)
  diamond(num)
  puts PADDING * (num + 2)
end

def diamond(num)
  top = num / 2 + 1
  bottom = top - 1
  (top).times do |n|
    str = DIAMOND_CHAR + DIAMOND_CHAR * n * 2
    puts str.center(num+2, PADDING)
  end
  bottom.downto(1) do |n|
    str = DIAMOND_CHAR + DIAMOND_CHAR * (n - 1).abs * 2
    puts str.center(num+2, PADDING)
  end
end

grid(9)


def empty_diamond(num)
  top = num / 2 + 1
  bottom = top - 2
  (top).times do |n|
    str = DIAMOND_CHAR
    str +=  PADDING * (n * 2 - 1) + DIAMOND_CHAR if n > 0
    puts str.center(num+2, PADDING)
  end
  bottom.downto(0) do |n|
    str = DIAMOND_CHAR
    str +=  PADDING * (n * 2 - 1) + DIAMOND_CHAR if n > 0
    puts str.center(num+2, PADDING)
  end
end
