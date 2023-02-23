InvalidCodonError = Class.new(TypeError)

module Translation
  CODONS = { %w[AUG]     => 'Methionine', %w[UUU UUC]         => 'Phenylalanine',
             %w[UUA UUG] => 'Leucine',    %w[UCU UCC UCA UCG] => 'Serine',
             %w[UAU UAC] => 'Tyrosine',   %w[UGU UGC]         => 'Cysteine',
             %w[UGG]     => 'Tryptophan', %w[UAA UAG UGA]     => 'STOP' }

  def self.of_codon(codon)
    CODONS.find { |k, _| k.include?(codon) }&.last || (raise InvalidCodonError)
  end

  def self.of_rna(strand)
    strand.scan(/.{1,3}/).map { |c| of_codon(c) }.take_while { |c| c != 'STOP' }
  end
end

p Translation.of_codon('UUA')


class Item
  def initialize
    @name = 'item name'
  end

  private

  def to_s
    "This is the to s method in a private setting. #{@name}"
  end
end

puts Item.new
