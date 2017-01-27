def halvsies(arr)
  sz = arr.size
  el_len, remainder  = sz.divmod(2)
  first = (0..el_len + remainder - 1)
  second = (el_len + remainder .. sz - 1)
  [arr[first], arr[second]]
end
p halvsies([1, 5, 2, 4, 3])

def halvsies(array)
  first_half = array.slice(0, (array.size / 2.0).ceil)
  second_half = array.slice(first_half.size, array.size - first_half.size)
  [first_half, second_half]
end
