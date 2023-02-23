#multiply.rb
def multiply(a, b)
a * b
end
p "Enter 2 numbers to muliply: "
num1 = gets.to_i
num2 = gets.to_i
p "#{num1} * #{num2} = #{multiply(num1, num2)}"
