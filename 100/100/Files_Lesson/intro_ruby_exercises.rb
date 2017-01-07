# intro_ruby_exercises.rb

loop do
  puts "Select exercise to execute:"
  puts "1. Use the each method of Array to iterate over [1..10] and print out each value"
  puts "2. Same as above, but only print values > 5"
  puts "3. Using same Array as 2, use the select method to extract all odd numbers"
  puts "Append 11 to the end of the original array.  Prepend 0 to the beginning"
  puts "Get rid of 11 and append 3"
  puts "6. Get rid of duplicates without specifically removing any one value"
  puts "7. What's the major difference between an Array and a Hash?"
  puts "8. Creat a Hash using both Ruby syntax styles"
  puts "9. Suppose you have a hash h = {a:1, b:2, c:3, d:4}, \n\t1. Get the value of key :b\n\t2. add to this hash the key:value pair {e:5}\n\t3. Remove all key:value pairs whose value is less than 3.5"
  puts "10.  Can hash values be arrays?  Can you have an array of hashes? (give examples)"
  puts "11. Look at several Rails/Ruby only API sources and say which one you like best and why"
  puts "12. Given the following data structures.  Write a program that moves the information from the array in the empty hash that applies to the correct person.\n\tcontact_data = [[\"joe@email.com\", \"123 Main st.\", \"555-123-4567\"], [\"sally@email.com\", \"404 Not Found Dr.\", \"123-234-3454\"]]\n\n\tcontacts = {\"Joe Smith\" => {}, \"Sally Johnson\" => {}}"
  puts "13. Using the hash you created from the previous exercise, demonstrate how you would access Joe's email and Sally's phone number"
  puts "14. In ex 12, we manually set the contacts has values one by one.  Now, programmatically loop or iterate over the contacts hash from ex 12, and populate the associated data from the contact_data array.\nThis is only suuposed to be for 1 entry in the contacts.  As a bonus, see if you can figure out how to make it work with multiple entries in the contacts hash."
  puts "15. Use Ruby's Array method delete_if and String method Start_with? to delete all of the words that begin with an 's' in the following array : arr = ['snow', 'winter', 'ice', 'slippery', 'salted roads', 'white trees'].\nThen recreate the arr and get rid of all the words that start with 's' or 'w'"
  puts "16. Take the following array:\n\ta = ['white snow', 'winter wonderland', 'melting ice', 'slippery sidewalk', 'salted roads', 'white trees']\n and turn it into a new array that consists of strings containing one word. (ex: ['white snow'] => ['white', 'snow'])"
  puts "Press 'n' to quit"
  repeat = gets.chomp
  if repeat == 'n'
    break
  end
  case repeat.to_i
  when 1
    Array(1..10).each {|i| puts i}
  when 2
    Array(1..10).each {|i| puts i if i > 5}
  when 3
    arr = Array(1..10)
    arr.select {|i| puts i if i.odd?}
  when 4
    arr = Array(1..10)
    arr.push(11)
    arr.unshift(0)
    puts arr
  when 5
    arr = Array(1..10)
    arr.pop()
    arr.push(3)
    puts arr
  when 6
    arr = Array(1..10)
    arr.pop()
    arr.push(3)
    arr.uniq!
    puts arr
  when 7
    puts "Arrays store values in an ordered index, a hash stores key:value pairs, not necessarily in order"
  when 8
    newhash = {}
    newhash1 = Hash.new
    puts "newhash = {}, newhash1 = Hash.new"
    puts "#{newhash}, #{newhash1}"
  when 9
    h = {a:1, b:2, c:3, d:4}
    puts "a. key value of b is h[:b], #{h[:b]}"
    puts "b. Add {e:5} to h: h[:e]=5, #{h[:e]=5}"
    puts "c. remove all key:value pairs less than 3.5: h.delete_if {|k,v| h[k]<3.5} #{h.delete_if {|k,v| h[k]<3.5}}"
  when 10
    puts "Yes: a=[1,2,3], h[a]=\"first\"}; arr = [{a:1,b:2}, {c:3,d:4}]"
  when 12
    contact_data = [["joe@email.com", "123 Main st.", "555-123-4567"],["sally@email.com", "404 Not Found Dr.", "123-234-3454"]]
    contacts = {"Joe Smith" => {}, "Sally Johnson" => {}}
    keys = contacts.keys
    keys.each_index {|i| contacts[keys[i]] = contact_data[i]}
    puts contacts
  when 13
    contact_data = [["joe@email.com", "123 Main st.", "555-123-4567"],["sally@email.com", "404 Not Found Dr.", "123-234-3454"]]
    contacts = {"Joe Smith" => {}, "Sally Johnson" => {}}
    keys = contacts.keys
    keys.each_index {|i| contacts[keys[i]] = contact_data[i]}

    puts "Phone numbers: contacts[\"Joe Smith\"][2]: #{contacts["Joe Smith"][2]}\ncontacts[\"Sally Johnson\"][2]: #{contacts["Sally Johnson"][2]}"
  when 14
    contact_data = ["joe@email.com", "123 Main st.", "555-123-4567"]
    contacts = {"Joe Smith" => {}}
    keys = contacts.keys
    keys.each_index {|i| contacts[keys[i]] = contact_data[i]}
  when 15
    arr = ['snow', 'winter', 'ice', 'slippery', 'salted roads', 'white trees']
    arr.delete_if {|i| i.start_with?("s", "w")}
  when 16
    a = ['white snow', 'winter wonderland', 'melting ice',
     'slippery sidewalk', 'salted roads', 'white trees']
     arr2 = a.map { |e| e.split }.flatten
  end



end
