class Dog:
    def __init__(self):
        self.__name = 'Ted'

    def speak(self):
        print(f"Dog {self.__name} says woof")

d = Dog()
d.speak()

d.__name = 'Fred'
print('Name changed to Fred...')
print(f"Name: {d.__name}")
d.speak()
