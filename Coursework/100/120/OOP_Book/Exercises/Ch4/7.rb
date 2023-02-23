class Student
  attr_accessor :name

  def initialize(n, g)
    self.name = n
    self.grade = g
  end

  def grade=(num)
    @grade = num
  end

  def grade_better_than?(student)
    grade > student.grade
  end

  protected

  def grade
    @grade
  end

end

joe = Student.new('Joe', 97)
bob = Student.new('Bob', 85)
p joe.grade_better_than?(bob)
