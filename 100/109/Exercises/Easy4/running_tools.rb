def running_total(arr)
  sto_arr = []
  arr.each_with_index do |item, index|
    sto = 0
    0.upto(index) {|x| sto += arr[x]}
    sto_arr[index] = sto
  end
  sto_arr
end

p running_total([14, 11, 7, 15, 20])

def run_tot(arr)
  sum = 0
  arr.map {|el| sum += el}
end

p run_tot([14, 11, 7, 15, 20])

def inject_run_tot(arr)
  sum = 0
  arr.inject([]) do |memo, obj|
    sum += obj
    memo << sum
  end
end

p inject_run_tot([14, 11, 7, 15, 20])
