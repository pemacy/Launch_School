'''
Using the code below, determine the method resolution order (MRO) used when invoking cat1.color. Only list the classes that are checked by Python when searching for the color attribute. Do not use the mro method.
'''

class Animal:
    def __init__(self, color):
        self.color = color

class Cat(Animal):
    pass

class Bird(Animal):
    pass

cat1 = Cat('Black')
print(cat1.color)

'''
MRO:
    class '__main__.Cat'
    class '__main__.Animal'
    class 'object'
'''
