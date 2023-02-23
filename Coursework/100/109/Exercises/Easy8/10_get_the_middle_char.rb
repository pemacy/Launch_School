def center_of(str)
  if str.size.to_f % 2 == 0
    return str[str.size / 2 - 1] + str[str.size / 2]
  else
    return str[str.size / 2]
  end
end

p center_of('Launch')
