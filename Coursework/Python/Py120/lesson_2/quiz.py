# class Cat:
#     _total_cats = 0

#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name

#     def jump(self):
#         return f'{self.name} is jumping!'

#     @classmethod
#     def total_cats(cls):
#         return cls._total_cats

# mitzi = Cat('Mitzi')
# print(mitzi.jump())                  # Mitzi is jumping!
# print(Cat.total_cats())              # 1
# print(f"The cat's name is {mitzi}")  # The cat's name is Mitzi

# fluffy = Cat('Fluffy')
# print(Cat.total_cats())               # 2

# class Student:
#     # class body:
#     def __init__(self, name, grade=None):
#         self.name = name
#         self.grade = grade

#     # def __str__(self):
#     #     return f'{self.__class__.__name__} {self.name}'

#     def __repr__(self):
#         return f'{self.__class__.__name__} {self.name}'

# ade = Student('Adewale')
# print(ade)        # Student Adewale

# class FarmAnimal:
#     def speak(self):
#         return f'{self.__class__.__name__} says '

# class Sheep(FarmAnimal):
#     def speak(self):
#         return super().speak() + 'baa!'

# class Lamb(Sheep):
#     def speak(self):
#         return super().speak() + 'baaaaaaa!'

# class Cow(FarmAnimal):
#     def speak(self):
#         return super().speak() + 'mooooooo!'

# print(Sheep().speak())        # Sheep says baa!
# print(Lamb().speak())         # Lamb says baa!baaaaaaa!
# print(Cow().speak())          # Cow says mooooooo!

class Character:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'{name} is speaking.'

class Thief(Character):
    pass
    # def speak(self):
    #     return f'{self.name} is whispering.'

sneak = Thief('Sneak')
print(sneak.name)             # Sneak
print(sneak.speak())          # Sneak is whispering.
