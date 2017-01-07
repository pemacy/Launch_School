# count_to_zero_with_recursion.rb

x = 5

def cnt_dn(x)
  if x <= 0
    puts x
  else
    puts x
    cnt_dn(x - 1)
  end
end

cnt_dn(x)
