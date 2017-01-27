def staggered_case(str, bool=true)
  stagger = []
  bool ? n = 0 : n = 1
  str.chars.each_with_index do | chr,i |
    stagger << chr.upcase if (i+n).even?
    stagger << chr.downcase if (i+n).odd?
  end
  stagger.join
end

p staggered_case('I Love Launch School!',false)
p staggered_case('ignore 77 the 444 numbers')
