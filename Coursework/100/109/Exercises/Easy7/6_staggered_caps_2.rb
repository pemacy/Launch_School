def staggered_case(str, bool=true, non_alpha = true)
  stagger = []
  bool ? n = 0 : n = 1
  count = 0 + n
  str.chars.each_with_index do | chr,i |
    stagger << chr.upcase if count.even?
    stagger << chr.downcase if count.odd?
    count += 1 if /[a-z]/i =~ chr
    count += 1 if non_alpha == false
  end
  stagger.join
end

p staggered_case('I Love Launch School!',false,false)
p staggered_case('ignore 77 the 444 numbers')
p staggered_case('ALL CAPS')
