my_global = 'my global'

def func():
    print(my_global) # prints 'my global' - references global variable

func()

def func0():
    # print(my_global) # raises an error
    my_global = 6 # makes local variable
    print(my_global)

func0()
print(my_global) # still prints 'my global'

def func1():
    # nonlocal my_global - raises an error because no binding other than global is found for this var
    '''
    This does nothing as there is no variable named "my_global" in an outside scope that is not a global variable
    print() will print nothing
    '''
    # print(my_global)

def func2():
    global my_global
    my_global = 'foowho'
    print(my_global) # prints 'foowho'

func2()
print(my_global) # prints 'foowho'

def func3():
    global my_global
    def func3_1():
        my_global = 5
    func3_1()
    print(my_global) # prints 'foowho'

func3()

def func4():
    global my_global
    def func4_1():
        pass
        # nonlocal my_global # raises an error because only global versions of this variable exist
    func4_1()

func4()

def func5():
    my_global = 5
    def func5_1():
        nonlocal my_global
        print(my_global) # prints 5
        my_global = 'Now its a string again'
    func5_1()
    print(my_global) # prints now its a string again

func5()


