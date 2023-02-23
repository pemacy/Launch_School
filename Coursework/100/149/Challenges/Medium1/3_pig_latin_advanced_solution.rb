module PigLatin
  CONSONANT_SOUND_WORDS =
    /\b(?![xy][^aeiou])(b|ch|c|d|f|g|h|j|k|l|m|n|p|qu|q|r|sch|squ|sh|s|thr|th|v|w|x|y|z)(\w+)/i

  def self.translate(str)
    str.gsub(CONSONANT_SOUND_WORDS, '\2\1').gsub(/(\w+)/, '\1ay')
  end
end
