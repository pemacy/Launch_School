CONST = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
          'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
          'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
          'nineteen']

CONVERT = CONST.each_with_index.with_object(Hash.new(0)) do |(v, i), hash|
          hash[i] = v
        end

def alphabetic_number_sort(arr)
  # alph_arr = []
  # alph_arr = arr.map { | el | CONVERT[el] }
  # alph_arr.sort!
  # alph_arr.map! { |el| CONVERT.key(el) }
  arr.sort_by do |num|
    CONST[num]
  end
end

p alphabetic_number_sort((0..19).to_a)
