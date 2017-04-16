class InvalidCodonError < StandardError
  # def initialize(msg = "Either wrong number of nucleotides, or wrong code")
  #   super
  # end
end

class Translation
  CODON_TABLE = { ['AUG']	=> 'Methionine',
                ['UUU', 'UUC'] => 'Phenylalanine',
                ['UUA', 'UUG'] => 'Leucine',
                ['UCU', 'UCC', 'UCA', 'UCG'] => 'Serine',
                ['UAU', 'UAC'] => 'Tyrosine',
                ['UGU', 'UGC'] => 'Cysteine',
                ['UGG'] => 'Tryptophan',
                ['UAA', 'UAG', 'UGA'] => 'STOP' }

  def self.of_codon(codon)
    validate(codon)
    result = parse_codon(codon).map { |cdn| match_cdn?(cdn) }
                                .map{|m| CODON_TABLE[m] }.compact
    result = result[0] if result.size == 1
    idx = result.index('STOP')
    idx ? result[0..idx - 1] : result
  end

  def self.of_rna(codon)
    of_codon(codon)
  end

  def self.validate(codon)
    raise InvalidCodonError unless /\b[AUGC]{3}+\b/.match(codon)
  end

  def self.match_cdn?(cdn)
    CODON_TABLE.each { |list, _| return list if list.include?(cdn)}
  end

  def self.match_codon?(list, codon)
    codon.each { |cdn| return list if list.include?(cdn) }
  end

  def self.parse_codon(codon)
    storage = []
    0.upto((codon.size / 3) - 1) { |i| storage << codon[i * 3,3]}
    storage
  end
end
