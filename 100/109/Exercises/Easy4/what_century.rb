def century(year)
  century_year = year / 100
  century_year += 1 if year % 100 > 0
  puts century_year.to_s + century_ending(century_year.to_s)
end

def century_ending(century_year)
  if century_year.size > 1
    return "th" if ["11", "12", "13"].include?(century_year[-2..-1])
  end

  case century_year[-1]
  when '1'then 'st'
  when '2' then 'nd'
  when '3' then 'rd'
  else 'th'
  end
end

century(10103)


# LAUNCH SCHOOL ANSWER
def century(year)
  century = year / 100 + 1
  century -= 1 if year % 100 == 0
  century.to_s + century_suffix(century)
end

def century_suffix(century)
  return 'th' if [11, 12, 13].include?(century % 100)
  last_digit = century % 10

  case last_digit
  when 1 then 'st'
  when 2 then 'nd'
  when 3 then 'rd'
  else 'th'
  end
end
