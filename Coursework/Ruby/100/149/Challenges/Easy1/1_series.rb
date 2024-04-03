require 'pry'

class Series
  attr_accessor :number, :arr, :num_consecs

  def initialize(num)
    @number = num
  end

  def slices(n)
    raise ArgumentError, 'Wrong Size' if n > (number.size) || n < 1
    number.each_char.map(&:to_i).each_cons(n).to_a
  end

  def n_series(arr, num_consecs)
    self.arr = arr
    self.num_consecs = num_consecs
    consecs = []
    (arr.size - num_consecs + 1).times { |n| consecs << arr[n, num_consecs]}
    consecs.keep_if { |el|  check_consecs(el) }
  end

  def check_consecs(consecs)
    (consecs.size - 1).downto(1) do |i|
      return false if (consecs[i] - consecs[i-1] != 1)
    end
    true
  end

  private :check_consecs
end

con = Series.new(%(123451234512345))
p con.slices(4)
p con.n_series([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5], 4)
