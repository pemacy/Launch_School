Clock = Struct.new(:mins) do
  singleton_class.send(:alias_method, :at, :new)
  define_method(:initialize) { |hour, min = 0| self.mins = (min + hour * 60) % 1440 }
  define_method(:==)         { |other| mins == other.mins }
  define_method(:to_s)       { format('%02d:%02d', *mins.divmod(60)) }
  %i[+ -].each { |op| define_method(op) { |min| Clock.new(0, mins.send(op, min)) } }
end
