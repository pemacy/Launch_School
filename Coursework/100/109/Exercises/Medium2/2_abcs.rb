BLOCKS = ['BO', 'XK', 'DQ', 'CP', 'NA', 'GT', 'RE', 'FS',
          'JW', 'HU', 'VI', 'LY', 'ZM']

def block_word?(str)
  used_block = []
  str.chars.each do |chr|
    used_block << BLOCKS.select {|blk| blk.include?(chr.upcase)}
  end
  used_block == used_block.uniq ? true : false
end

p block_word?('BATCH')
