print "Enter a number to factorial:"
num = gets.to_i
fac = 1
print "#{num} factorial is: "
if num == 0
  fac = 1
else
  for i in 1..num do
    fac *= i
  end
end

print fac
