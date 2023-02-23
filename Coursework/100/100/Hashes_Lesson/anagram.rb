# anagram.rb

words =  ['demo', 'none', 'tied', 'evil', 'dome', 'mode', 'live', 'fowl', 'veil', 'wolf', 'diet', 'vile', 'edit', 'tide', 'flow', 'neon']


arr = []
letters = []
anagrams = []

words.each do |item|
  for i in (0..item.length - 1)
    arr.push([item[i]])
  end
  for i in (0..arr.length-1)
    arr[i]=arr[i][0]
  end
  letters.push(arr.sort)
  arr.clear
end

letters.each do |item|
  arr.push(letters.each_index.select{|o| letters[o] == item})
end

arr.uniq!
anagrams = arr

for i in (0..arr.length-1)
  for j in (0..arr[i].length - 1)
    anagrams[i][j] = words[arr[i][j]]
  end
end

anagrams.each do |item|
  p item
end


# LAUNCH SCHOOL SOLUTION

result = {}

words.each do |word|
  key = word.split('').sort.join
  if result.has_key?(key)
    result[key].push(word)
  else
    result[key] = [word]
  end
end

p result

result.each do |k, v|
  puts "------"
  p v
end
