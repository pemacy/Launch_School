class School
  def initialize
    @all_students = Hash.new([])
  end

  def add(name, grade)
    (@all_students[grade] += [name]).sort!
  end

  def to_h
    @all_students.sort.map { |grade, list| [grade, list.sort]}.to_h
  end

  def grade(grade)
    @all_students[grade]
  end
end

# sch = School.new
# sch.add('Frank', 4)
# sch.add('Alan', 4)
# sch.add('AAlbert', 4)
# sch.add('Tom', 3)
# sch.add('Sue', 2)
# p sch.grade(4)
# p sch.to_h
