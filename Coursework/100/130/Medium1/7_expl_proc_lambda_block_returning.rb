# Group 1
def check_return_with_proc
  my_proc = proc { return }
  my_proc.call
  puts "This will never output to screen."
end

# check_return_with_proc
#  produces a LocalJumpError because the return is unexpected -- we immediately exit the method

# Group 2
my_proc = proc { return }

def check_return_with_proc_2(my_proc)
  my_proc.call
end

# check_return_with_proc_2(my_proc)
#  produces a LocalJumpError because the return is unexpected -- we immediately exit the method when the Proc is called

# Group 3
def check_return_with_lambda
  my_lambda = lambda { return }
  my_lambda.call
  puts "This will be output to screen."
end

check_return_with_lambda

# Group 4
my_lambda = lambda { return }
def check_return_with_lambda(my_lambda)
  my_lambda.call
  puts "This will be output to screen."
end

check_return_with_lambda(my_lambda)
# both groups 3 and 4 work and print the output to the screen

# Group 5
def block_method_3
  yield
end

block_method_3 { return }
#  produces a LocalJumpError because the return is unexpected
