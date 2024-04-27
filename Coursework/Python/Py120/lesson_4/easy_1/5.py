'''
Which of the following classes would create objects that have an instance
variable. How do you know?
'''

class Fruit:
    def __init__(self, name):
        my_name = name

class Pizza:
    def __init__(self, name):
        self.my_name = name

'''
class Pizza creates an instance variable when initialized because it uses
self.my_name, which it how instance variables are created
my_name in the Fruit class is a local variable to the method __init__
'''
