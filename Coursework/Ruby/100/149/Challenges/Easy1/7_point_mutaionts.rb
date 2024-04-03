require 'pry'

class DNA
  attr_accessor :first_strand

  def initialize(first_strand)
    @first_strand = first_strand
  end

  def hamming_distance(second_strand)
    # longer, shorter = second_strand.size >= first_strand.size ?
    #                     [second_strand, first_strand] :
    #                     [first_strand, second_strand]
    # shorter.chars.select.with_index{ |d,i| d != longer[i]}.size

    (second_strand.chars).zip(first_strand.chars)
                          .select{|s| s.first != s.last && !s.include?(nil)}
                          .size

  end

end

# dna = DNA.new ''
# p dna.hamming_distance ''

# p DNA.new('AAACTAGGGG').hamming_distance('AGGCTAGCGGTAGGAC')

# dna = DNA.new('AGGCAA')
# p dna.hamming_distance('AGACAACAGCCAGCCGCCGGATT')
