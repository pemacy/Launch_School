def convert_to_base_8(n)
  p n.to_s.oct
  n.to_s.oct.to_i # replace these two method calls
end

# The correct type of argument must be used below
base8_proc = method(:convert_to_base_8).to_proc

# We'll need a Proc object to make this code work. Replace `a_proc`
# with the correct object
p [8,10,12,14,16,33].map(&base8_proc)
#
# def sym_to_proc(arr, sym)
#   arr.map do |item|
#     item.send(sym)
#   end
# end
#
# p sym_to_proc([1,2,3,4], :to_s)
