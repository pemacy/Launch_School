# frozen_string_literal: true

# Write a method that determines the mean (average) of the three scores passed
# to it, and returns the letter value associated with that grade.

# Tested values are all between 0 and 100. There is no need to check for
# negative values or values greater than 100.

SCORE_CONVERSION = {
  A: (90..100),
  B: (80...90),
  C: (70...80),
  D: (60...70),
  F: (0...60)
}

def get_grade(*grades)
  score = grades.reduce(&:+) / grades.size
  SCORE_CONVERSION.select { |_grade, range| range.cover? score }.keys.first.to_s
end

p get_grade(95, 90, 93) == "A"
p get_grade(50, 50, 95) == "D"
