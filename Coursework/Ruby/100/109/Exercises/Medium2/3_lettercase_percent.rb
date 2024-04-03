def ltr_per(str)
  hsh = {upper: 0, lower: 0, neither: 0}
  total = str.chars.count
  str.chars.each do |chr|
    hsh[:upper] += 1 if /[A-Z]/ =~ chr
    hsh[:lower] += 1 if /[a-z]/ =~ chr
    hsh[:neither] += 1 if /[^a-zA-z]/ =~ chr
  end
  hsh.each { |key,val| hsh[key] = val.to_f / total * 100 }
  hsh
end

puts ltr_per('AbCd +Ef')
