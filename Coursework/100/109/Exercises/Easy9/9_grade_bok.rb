GRADE = {'A' => (90..100), 'B' => (80..89), 'C' => (70..79), 'D' => (60..69), 'F' => (0..59)}

def get_grade(score1, score2, score3)
  average = ((score1 + score2 + score3) / 3.0).round
  GRADE.each do |key, value|
    return key if value.include?(average)
  end
end

p get_grade(50, 50, 95)
