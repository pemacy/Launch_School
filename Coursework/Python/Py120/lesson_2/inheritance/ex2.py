import unittest

class Pet:
    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'

    def sleep(self):
        return 'sleeping!'

class Dog(Pet):
    def speak(self):
        return 'bark!'

    def fetch(self):
        return 'fetching'

class Cat(Pet):
    def speak(self):
        return 'meow!'

class Bulldog(Dog):
    def sleep(self):
        return 'snoring!'

'''
method resolution order:
    BullDog > Dog > Pet > object
'''

class TestInheritance(unittest.TestCase):
    def test_bulldog_inherits_dog(self):
        b = Bulldog()
        b_class = b.__class__
        b_class_class = b.__class__.mro()[1]
        self.assertEqual(b_class_class, Dog)

unittest.main()
