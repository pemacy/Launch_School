def triangle(a,b,c)
  tri = [a,b,c].sort
  return :invalid if tri[0..1].reduce(:+) <= tri[2]
  return :equilateral if tri.uniq.size == 1
  return :isosceles if tri.uniq.size == 2
  :scalene
end

puts triangle(3,3,0)
