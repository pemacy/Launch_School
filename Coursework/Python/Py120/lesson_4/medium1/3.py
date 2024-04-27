class Animal:
    def speak(self, message):
        print(message)

class Dog(Animal):
    def bard(self):
        self.speak('Woof')

class Cat(Animal):
    def meow(self):
        self.speak('Meow')
