class School
  method_names = [:initialize, :add, :to_h, :grade]
  actions = [ -> { @roster = Hash.new([]) },
              -> (nm, grd) { (@roster[grd] += [nm]).sort! },
              -> { @roster.sort.to_h },
              -> (grd) { @roster[grd] } ]
  method_names.zip(actions).map { |mthd, actn| define_method(mthd, actn) }
end

# sch = School.new
# sch.add('Frank', 4)
# sch.add('Alan', 4)
# sch.add('AAlbert', 4)
# sch.add('Tom', 3)
# sch.add('Sue', 2)
# p sch.grade(4)
# p sch.to_h


School1 = Class.new do
  methods = [ %q(def initialize() @roster = Hash.new([]) end),
              %q(def add(nm, grd) (@roster[grd] += [nm]).sort! end),
              %q(def to_h() @roster.sort.to_h end),
              %q(def grade(grd) @roster[grd] end)]
  methods.each { |meth| class_eval(meth) }
end

sch = School1.new
sch.add('Franklen', 4)
sch.add('Alan', 4)
sch.add('AAlbert', 4)
sch.add('Tom', 3)
sch.add('Sue', 2)
p sch.grade(4)
p sch.to_h
