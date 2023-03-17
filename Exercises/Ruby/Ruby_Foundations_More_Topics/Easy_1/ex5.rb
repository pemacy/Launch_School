# frozen_string_literal: true

# The following list contains the names of individuals who are pioneers in the
# field of computing or that have had a significant influence on the field.
# The names are in an encrypted form, though, using a simple (and incredibly
# weak) form of encryption called Rot13.

# Write a program that deciphers and prints each of these names .

def decipher(name)
  name.downcase.split.map do |word|
    word.codepoints.map do |cp|
      cp <= 109 ? (cp + 13).chr : (cp - 13).chr
    end.join.capitalize
  end.join(' ')
end

p decipher('nag bar')
p decipher('Nqn Ybirynpr')
p decipher('Tenpr Ubccre')
p decipher('Nqryr Tbyqfgvar')
p decipher('Nyna Ghevat')
p decipher('Puneyrf Onoontr')
p decipher('Noqhyynu Zhunzznq ova Zhfn ny-Xujnevmzv')
p decipher('Wbua Ngnanfbss')
p decipher('Ybvf Unvog')
p decipher('Pynhqr Funaaba')
p decipher('Fgrir Wbof')
p decipher('Ovyy Tngrf')
p decipher('Gvz Orearef-Yrr')
p decipher('Fgrir Jbmavnx')
p decipher('Xbaenq Mhfr')
p decipher('Fve Nagbal Ubner')
p decipher('Zneiva Zvafxl')
p decipher('Lhxvuveb Zngfhzbgb')
p decipher('Unllvz Fybavzfxv')
p decipher('Tregehqr Oynapu')
