def letter_case_count(str)
  case_count = str.chars.each_with_object(Hash.new(0)) do | s,case_count |
    if /[a-z]/ =~ s
      case_count[:lowercase] += 1
    elsif /[A-Z]/ =~ s
      case_count[:uppercase] += 1
    else
      case_count[:neither] += 1
    end
  end
  case_count
end

p letter_case_count('abCdef 123')
