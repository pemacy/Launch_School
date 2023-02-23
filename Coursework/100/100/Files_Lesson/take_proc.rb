# take_proc.rb

def take_proc(proc)
  proc.call
end

my_proc = Proc.new do
  puts "I am a proc being called in a method"
end

take_proc(my_proc)

def disp_name_proc(proc)
  puts "Enter your name"
  name = gets.chomp
  proc.call name
end

my_proc_name = Proc.new do name
  puts "Hello #{name}"
end

begin
  disp_name_proc(my_proc_name)
rescue
  puts "something went wrong"
end

# my_proc_name.call name
