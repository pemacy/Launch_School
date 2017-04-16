School = Class.new do
  method_names = %i[initialize add grade to_h]
  method_bodies = [ -> { @roster = Hash.new([]) },
                    -> (name, num) { (@roster[num] += [name]).sort! },
                    -> (num) { @roster[num] },
                    -> { @roster.sort.to_h } ]
  method_names.zip(method_bodies).each { |name, body| define_method(name, body) }
end

class School1
  methods = [
              %q(def initialize() @roster = Hash.new([]) end),
              %q(def add(nm, grd) (@roster[grd] += [nm]).sort! end),
              %q(def to_h() @roster.sort.to_h end),
              %q(def grade(grd) @roster[grd] end)]
  methods.each { |meth| class_eval(meth) }
end

# Re-written:

School1 = Class.new do
  methods = [ %q(def initialize() @roster = Hash.new([]) end),
              %q(def add(nm, grd) (@roster[grd] += [nm]).sort! end),
              %q(def to_h() @roster.sort.to_h end),
              %q(def grade(grd) @roster[grd] end)]
  methods.each { |meth| class_eval(meth) }
end
