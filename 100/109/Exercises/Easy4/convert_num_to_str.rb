def num_to_str(num)
  count = 1
  num2 = num
  while num2 > 10
    num2 /= 10
    count += 1
  end

  num_arr=[]
  count.times {|n| num_arr << ((num/10**n)%10)}
  num_arr.reverse.join
end


p num_to_str(123)

Further Exploration

One thing to note here is the String#prepend method; unlike most string mutating methods, the name of this method does not end with a !. However, it is still a mutating method - it changes the string in place.

This is actually pretty common with mutating methods that do not have a corresponding non-mutating form. chomp! ends with a ! because the non-mutating chomp is also defined. prepend does not end with a ! because there is no non-mutating form of prepend.

How many mutating String methods can you find that do not end with a !. Can you find any that end with a !, but don't have a non-mutating form? Does the Array class have any methods that fit this pattern? How about the Hash class?
