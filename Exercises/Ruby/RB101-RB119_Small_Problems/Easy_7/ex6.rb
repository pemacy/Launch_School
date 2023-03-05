# frozen_string_literal: false

# Modify the method from the previous exercise so it ignores non-alphabetic
# characters when determining whether it should uppercase or lowercase each
# letter. The non-alphabetic characters should still be included in the return
# value; they just don't count when toggling the desired case.

def staggered_case(str)
  upcase = true
  str.chars.each_with_object('') do |c, str_2|
    unless c =~ /[a-zA-Z]/
      str_2 << c
      next
    end

    if upcase
      str_2 << c.upcase
      upcase = false
    else
      str_2 << c.downcase
      upcase = true
    end
  end
end

puts staggered_case('I Love Launch School!') == 'I lOvE lAuNcH sChOoL!'
puts staggered_case('ALL CAPS') == 'AlL cApS'
puts staggered_case('ignore 77 the 444 numbers') == 'IgNoRe 77 ThE 444 nUmBeRs'
