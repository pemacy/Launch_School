# family_members.rb

# Given

family = {  uncles: ["bob", "joe", "steve"],
            sisters: ["jane", "jill", "beth"],
            brothers: ["frank","rob","david"],
            aunts: ["mary","sally","susan"]
          }

imm_fam = []

imm_fam = family.select do |k ,v|
  k == :brothers || k == :sisters
end

puts imm_fam

imm_fam = imm_fam.values.flatten

puts imm_fam
