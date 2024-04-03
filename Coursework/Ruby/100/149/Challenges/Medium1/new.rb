class PigLatin
  REGEX = /\b(y(?=[aeiou])|ch|s?qu|s?tr|thr?|s?ch|xray|[^aeiouy])(\w*)/
  def self.translate(str)
    str.gsub(REGEX,'\2\1').gsub(/\b\w+/,'\1ay')
  end
end

p PigLatin.translate('xray string')
