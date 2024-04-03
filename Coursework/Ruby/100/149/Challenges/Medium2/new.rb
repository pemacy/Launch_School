class PigLatin
  REGEX = /\A(y(?=[aeiou])|ch|s?qu|s?tr|thr?|s?ch|xray|[^aeiouy])(\w*)/
  def self.translate(str)
    str.split.map do |s|
      s.gsub(REGEX,'\2\1') + 'ay'
    end.join(' ')
  end
end

p PigLatin.translate('xray string')
