users = {John: 'password', Tim: 'passWord'}

loop do
  puts "Please enter user name"
  user_name = gets.chomp.downcase
  puts "Please enter your password"
  password = gets.chomp
  break if users.any?{|k,v| k.to_s.eql?(user_name) && v.eql?(password)}
  puts "Authorization Failed!"
end
puts "Welcome!"
