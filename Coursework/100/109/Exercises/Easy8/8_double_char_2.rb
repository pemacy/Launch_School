def repeater(str)
  str.chars.map do |chr|
    if /[a-z]/i =~ chr
      unless /[aeiou]/i =~ chr
        chr += chr
      end
    end
    chr
  end.join
end

p repeater('Hello')
