def crunch(str)
  no_rpt_chars = ''
  str.scan(/(.)\1*/) { |w| no_rpt_chars << w[0] }
  no_rpt_chars
end

p crunch('ddaaiillyy ddoouubbllee')
